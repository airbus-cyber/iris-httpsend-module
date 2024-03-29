# This file is part of IRIS HTTP Send Module.
#
# Copyright (C) 2023 Airbus CyberSecurity (SAS)
#
# IRIS HTTP Send Module is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# IRIS HTTP Send Module is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with IRIS HTTP Send Module. If not, see <https://www.gnu.org/licenses/>.

from iris_interface.IrisModuleInterface import IrisModuleInterface
from iris_interface.IrisModuleInterface import IrisModuleTypes
import iris_interface.IrisInterfaceStatus as InterfaceStatus
from iris_httpsend_module import VERSION
import json
import requests
from app.schema.marshables import CaseSchema
from app.schema.marshables import CaseAssetsSchema
from app.schema.marshables import CaseNoteSchema
from app.schema.marshables import IocSchema
from app.schema.marshables import EventSchema
from app.schema.marshables import CaseEvidenceSchema
from app.schema.marshables import CaseTaskSchema
from app.models import IocLink
from app.models import Cases

_POSTLOAD_HOOKS = [
    'on_postload_case_create', 'on_postload_case_delete', 'on_postload_case_update',
    'on_postload_asset_create', 'on_postload_asset_delete', 'on_postload_asset_update',
    'on_postload_note_create', 'on_postload_note_delete', 'on_postload_note_update',
    'on_postload_ioc_create', 'on_postload_ioc_delete', 'on_postload_ioc_update',
    'on_postload_event_create', 'on_postload_event_delete', 'on_postload_event_update',
    'on_postload_evidence_create', 'on_postload_evidence_delete', 'on_postload_evidence_update',
    'on_postload_task_create', 'on_postload_task_delete', 'on_postload_task_update',
]

_HOOK_OBJECTS_TO_SCHEMAS = {
    'case': CaseSchema(),
    'asset': CaseAssetsSchema(),
    'note': CaseNoteSchema(),
    'ioc': IocSchema(),
    'event': EventSchema(),
    'evidence': CaseEvidenceSchema(),
    'task': CaseTaskSchema(),
}


class IrisHttpSendInterface(IrisModuleInterface):
    _module_name = 'Iris Http Send'
    _module_description = 'Sends notifications to http endpoints on every postload hooks'
    _interface_version = 1.1
    _module_version = VERSION
    _pipeline_support = False
    _pipeline_info = {}
    _module_configuration = [{
        'param_name': 'url',
        'param_human_name': 'Notification URL',
        'param_description': 'Base URL to send notifications to',
        'default': None,
        'mandatory': True,
        'type': 'string'
    }]
    _module_type = IrisModuleTypes.module_processor

    def _register_to_hook(self, module_identifier, hook_name):
        status = self.register_to_hook(module_identifier, iris_hook_name=hook_name)

        if status.is_failure():
            self.log.error(status.get_message())

        else:
            self.log.info(f'Successfully subscribed to {hook_name} hook')

    def register_hooks(self, module_id: int):
        for hook_name in _POSTLOAD_HOOKS:
            self._register_to_hook(module_id, hook_name)

    def _parse_hook_object(self, hook_name):
        result = hook_name.split('_')[2]
        if result not in _HOOK_OBJECTS_TO_SCHEMAS:
            message = f'Unexpected hook object {result}.'
            self.log.error(message)
            raise ValueError(message)
        return result

    def _parse_hook_action(self, hook_name):
        result = hook_name.split('_')[-1]
        if result not in ['create', 'delete', 'update']:
            message = f'Unexpected hook action {result}.'
            self.log.error(message)
            raise ValueError(message)
        return result

    def _notify_create_element(self, url, element):
        self.log.info(f'Sending POST {url} {json.dumps(element, indent=2)}')
        return requests.post(f'{url}', json=element)

    def _notify_update_element(self, url, element):
        self.log.info(f'Sending PUT {url} {json.dumps(element, indent=2)}')
        return requests.put(f'{url}', json=element)

    def _notify_delete_element(self, url, element):
        self.log.info(f'Sending DELETE {url} {element}')
        return requests.delete(url, json=element)

    def _notify_element(self, hook_action, element, url):
        if hook_action == 'create':
            response = self._notify_create_element(url, element)
        elif hook_action == 'update':
            response = self._notify_update_element(url, element)
        else:
            response = self._notify_delete_element(url, element)
        self.log.info(f'Server returned: {response.status_code}')
        if response.text:
            self.log.info(f'Server answered: {response.json()}')

    def _handle_hook(self, hook_name: str, data):
        hook_object = self._parse_hook_object(hook_name)
        hook_action = self._parse_hook_action(hook_name)

        schema = _HOOK_OBJECTS_TO_SCHEMAS[hook_object]

        base_url = self.module_dict_conf['url']
        url = f'{base_url}/{hook_object}'
        for element in data:
            # In case of delete we get an int here (the identifier), otherwise it is some object
            if hook_action != 'delete':
                dumped_element = schema.dump(element)
                if hook_object == 'ioc':
                    result = IocLink.query.join(
                        IocLink.case
                    ).with_entities(
                        Cases.case_id
                    ).filter(
                        IocLink.ioc_id == element.ioc_id
                    ).first()
                    self.log.info(f'Found case identifier for IOC: {result.case_id}')
                    dumped_element['case_id'] = result.case_id
                if hook_object == 'evidence':
                    dumped_element['case_id'] = element.case_id
                if hook_object == 'note':
                    dumped_element['case_id'] = element.note_case_id
            self._notify_element(hook_action, dumped_element, url)

    def hooks_handler(self, hook_name: str, hook_ui_name: str, data):
        self.log.info(f'Received {hook_name} {hook_ui_name}')
        self.log.info(f'Received data of type {type(data)}')
        if isinstance(data, list):
            length = len(data)
            self.log.info(f'Received data is a list with {length} element(s)')
            if length > 0:
                self.log.info(f'First element has type type {type(data[0])}')
                self.log.info(f'Printing content: {data[0]}')

        try:
            self._handle_hook(hook_name, data)
            return InterfaceStatus.I2Success(data=data, logs=list(self.message_queue))
        except ValueError:
            return InterfaceStatus.I2Error(data=data, logs=list(self.message_queue))

