#  Copyright (C) 2023 Airbus CyberSecurity (SAS)
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from iris_interface.IrisModuleInterface import IrisModuleInterface
from iris_interface.IrisModuleInterface import IrisModuleTypes
import iris_interface.IrisInterfaceStatus as InterfaceStatus
from iris_httpsend_module import VERSION
import json
from app.schema.marshables import CaseSchema
from app.schema.marshables import CaseAssetsSchema
from app.schema.marshables import CaseAddNoteSchema
from app.schema.marshables import IocSchema
from app.schema.marshables import EventSchema
from app.schema.marshables import CaseEvidenceSchema
from app.schema.marshables import CaseTaskSchema

_POSTLOAD_HOOKS = [
    'on_postload_case_create', 'on_postload_case_delete',
    'on_postload_asset_create', 'on_postload_asset_delete', 'on_postload_asset_update',
    'on_postload_note_create', 'on_postload_note_delete', 'on_postload_note_update',
    'on_postload_ioc_create', 'on_postload_ioc_delete', 'on_postload_ioc_update',
    'on_postload_event_create', 'on_postload_event_delete', 'on_postload_event_update',
    'on_postload_evidence_create', 'on_postload_evidence_delete', 'on_postload_evidence_update',
    'on_postload_task_create', 'on_postload_task_delete', 'on_postload_task_update',
    'on_postload_report_create', 'on_postload_activities_report_create'
]

_HOOKS_TO_SCHEMAS = {
    'on_postload_case_create': CaseSchema(),
    'on_postload_case_delete': CaseSchema(),
    'on_postload_asset_create': CaseAssetsSchema(),
    'on_postload_asset_delete': CaseAssetsSchema(),
    'on_postload_asset_update': CaseAssetsSchema(),
    'on_postload_note_create': CaseAddNoteSchema(),
    'on_postload_note_delete': CaseAddNoteSchema(),
    'on_postload_note_update': CaseAddNoteSchema(),
    'on_postload_ioc_create': IocSchema(),
    'on_postload_ioc_delete': IocSchema(),
    'on_postload_ioc_update': IocSchema(),
    'on_postload_event_create': EventSchema(),
    'on_postload_event_delete': EventSchema(),
    'on_postload_event_update': EventSchema(),
    'on_postload_evidence_create': CaseEvidenceSchema(),
    'on_postload_evidence_delete': CaseEvidenceSchema(),
    'on_postload_evidence_update': CaseEvidenceSchema(),
    'on_postload_task_create': CaseTaskSchema(),
    'on_postload_task_delete': CaseTaskSchema(),
    'on_postload_task_update': CaseTaskSchema()
}

class IrisHttpSendInterface(IrisModuleInterface):
    _module_name = 'Iris Http Send'
    _module_description = 'Sends notifications to http endpoints on every postload hooks'
    _interface_version = 1.1
    _module_version = VERSION
    _pipeline_support = False
    _pipeline_info = {}
    _module_configuration = []
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

    def hooks_handler(self, hook_name: str, hook_ui_name: str, data):
        self.log.info(f'Received {hook_name} {hook_ui_name}')
        self.log.info(f'Received data of type {type(data)}')
        if isinstance(data, list):
            length = len(data)
            self.log.info(f'Received data is a list with {length} element(s)')
            if length > 0:
                self.log.info(f'First element has type type {type(data[0])}')
                self.log.info(f'Printing content: {data[0]}')

        if hook_name not in _HOOKS_TO_SCHEMAS:
            return InterfaceStatus.I2Success(data=data, logs=list(self.message_queue))

        schema = _HOOKS_TO_SCHEMAS[hook_name]

        for element in data:
            element_as_dict = schema.dump(element)
            self.log.info(f'Trying to dump with marshables: {json.dumps(element_as_dict, indent=2)}')

        return InterfaceStatus.I2Success(data=data, logs=list(self.message_queue))

