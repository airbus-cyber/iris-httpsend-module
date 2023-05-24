# Documentation

* https://docs.dfir-iris.org/development/hooks/

# Postload Hooks

## Case

| hook name                    | data type                   |
|:-----------------------------|-----------------------------|
| on_postload_case_create      | app.models.cases.Cases list |
| on_postload_case_delete      | int list                    |
| on_postload_case_info_update | app.models.cases.Cases list |

Note: `on_postload_case_delete` does not seem to call the module `hooks_handler` method.
Maybe because the object is already removed from the database?

Example data:
```json
{
  "status_id": 0,
  "owner_id": 1,
  "user_id": 1,
  "closing_note": null,
  "case_name": "#4 - AA",
  "close_date": null,
  "case_description": "BB",
  "classification_id": 8,
  "case_customer": 1,
  "modification_history": {
    "1683871842.666619": {
      "user": "administrator",
      "user_id": 1,
      "action": "created"
    }
  },
  "case_id": 2,
  "open_date": "2023-01-27",
  "case_uuid": "32396d24-fdcc-4da0-a660-d4f2e5c91ce1",
  "custom_attributes": {},
  "case_soc_id": ""
}
```

## Asset
| hook name                | data type                         |
|--------------------------|-----------------------------------|
| on_postload_asset_create | app.models.models.CaseAssets list |
| on_postload_asset_delete | int list                          |
| on_postload_asset_update | app.models.models.CaseAssets list |

Note: `on_postload_asset_delete` does not seem to call the module `hooks_handler` method. 
(see behavior with `iris_check_module`)

Example data:
```json
{
  "analysis_status_id": 1,
  "asset_domain": "",
  "asset_id": 1,
  "asset_info": "",
  "asset_description": "",
  "asset_tags": "",
  "asset_type_id": 13,
  "asset_compromise_status_id": 0,
  "date_update": "2023-01-27T09:37:37.866665",
  "custom_attributes": {},
  "user_id": 1,
  "asset_name": "name",
  "asset_uuid": "d65043c5-9c5d-4b5e-b501-c70f181039d8",
  "date_added": "2023-01-27T09:37:37.866655",
  "case_id": 2,
  "asset_ip": "",
  "asset_enrichment": null,
  "asset_type": {
    "asset_name": "Linux Account",
    "asset_description": "Linux Account",
    "asset_icon_compromised": "ioc_user.png",
    "asset_id": 5,
    "asset_icon_not_compromised": "user.png"
  }
}
```

## Note

| hook name               | data type                    |
|-------------------------|------------------------------|
| on_postload_note_create | app.models.models.Notes list |
| on_postload_note_delete | int list                     |
| on_postload_note_update | app.models.models.Notes list |

Note: `on_postload_note_delete` does not seem to call the module `hooks_handler` method.

Example data:
```json
{
  "note_id": 1,
  "note_content": "## Edit me with the right pencil button",
  "note_title": "Untitled note",
  "custom_attributes": {}
}
```

## IOC

| hook name              | data type                  |
|------------------------|----------------------------|
| on_postload_ioc_create | app.models.models.Ioc list |
| on_postload_ioc_delete | int list                   |
| on_postload_ioc_update | app.models.models.Ioc list |

Notes: 
* `on_postload_ioc_delete` does not seem to call the module `hooks_handler` method.
* export/import csv does not work
* even when importing a csv with two IOCs, hook `on_postload_ioc_create` is called twice with a list of 1 element. 
  I was expecting the hook to be called once with two elements. Is it ever a list of more than one element?

Example data:
```json
{
  "ioc_id": 1,
  "ioc_uuid": "fcc7fdd4-21d4-4c92-b2b5-a93cd08499d0",
  "ioc_description": "Description",
  "ioc_value": "value",
  "user_id": 1,
  "ioc_tags": "",
  "ioc_type_id": 4,
  "ioc_tlp_id": 2,
  "ioc_misp": null,
  "ioc_enrichment": null,
  "ioc_type": {
    "type_id": 1,
    "type_name": "AS",
    "type_validation_expect": null,
    "type_description": "Autonomous system",
    "type_taxonomy": null,
    "type_validation_regex": null
  },
  "custom_attributes": {}
}
```

## Event

| hook name                | data type                        |
|--------------------------|----------------------------------|
| on_postload_event_create | app.models.cases.CasesEvent list |
| on_postload_event_delete | ?                                |
| on_postload_event_update | app.models.cases.CasesEvent list |

Note: `on_postload_event_delete` does not seem to call the module `hooks_handler` method.

Example data:
```json
{
  "event_tags": "",
  "event_id": 1,
  "event_in_summary": false,
  "event_color": "#6861CE99",
  "event_added": "2023-01-27T09:40:14.423013",
  "custom_attributes": {},
  "user_id": 1,
  "event_raw": "",
  "case_id": 2,
  "event_tz": "+00:00",
  "event_content": "",
  "event_uuid": "85f99ba0-5c83-4a6b-9c99-23ea0ccd1f2c",
  "modification_history": {
    "1674812414.423076": {
      "user": "administrator",
      "action": "created",
      "user_id": 1
    }
  },
  "event_date_wtz": "2023-01-27T00:00:00.000000",
  "event_is_flagged": false,
  "event_source": "",
  "event_in_graph": true,
  "event_date": "2023-01-27T00:00:00.000000",
  "event_title": "title"
}
```

## Evidence

| hook name                   | data type                               |
|-----------------------------|-----------------------------------------|
| on_postload_evidence_create | app.models.models.CaseReceivedFile list |
| on_postload_evidence_delete | ?                                       |
| on_postload_evidence_update | app.models.models.CaseReceivedFile list |

Note: `on_postload_evidence_delete` does not seem to call the module `hooks_handler` method.

Example data:
```json
{
  "id": 1,
  "file_description": "",
  "filename": "filename",
  "file_hash": "",
  "file_uuid": "447084c4-6f72-46e3-bc0e-6fd34233673c",
  "file_size": 123,
  "custom_attributes": {},
  "date_added": "2023-01-27T09:40:53.974245"
}
```

## Task

| hook name               | data type                        |
|-------------------------|----------------------------------|
| on_postload_task_create | app.models.models.CaseTasks list |
| on_postload_task_delete | ?                                |
| on_postload_task_update | app.models.models.CaseTasks list |

Note: `on_postload_task_delete` does not seem to call the module `hooks_handler` method.

Example data:
```json
{
  "id": 1,
  "task_close_date": null,
  "task_userid_close": null,
  "task_open_date": "2023-01-27T09:41:33.025923",
  "task_description": "",
  "task_userid_open": 1,
  "task_status_id": 2,
  "task_title": "title",
  "custom_attributes": {},
  "task_last_update": "2023-01-27T09:41:33.025923",
  "task_case_id": 2,
  "task_uuid": "96223aad-c4f0-40fa-b10d-cf4321172e20",
  "task_userid_update": 1,
  "task_tags": ""
}
```

## Report

| hook name                            | data type |
|--------------------------------------|-----------|
| on_postload_report_create            | ?         |
| on_postload_activities_report_create | ?         |

Note: 
* got an exception when trying to generate any kind of reports...
* anyway we probably do not need to hook these events
