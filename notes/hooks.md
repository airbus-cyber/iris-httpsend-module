# Documentation

* https://docs.dfir-iris.org/development/hooks/

# Postload Hooks

## Case

| hook name               | data type                   |
|:------------------------|-----------------------------|
| on_postload_case_create | app.models.cases.Cases list |
| on_postload_case_delete | ?                           |

Note: `on_postload_case_delete` does not seem to call the module `hooks_handler` method.
Maybe because the object is already removed from the database?

## Asset
| hook name                | data type                         |
|--------------------------|-----------------------------------|
| on_postload_asset_create | app.models.models.CaseAssets list |
| on_postload_asset_delete | ?                                 |
| on_postload_asset_update | app.models.models.CaseAssets list |

Note: `on_postload_asset_delete` does not seem to call the module `hooks_handler` method. 
(see behavior with `iris_check_module`)

## Note

| hook name               | data type                    |
|-------------------------|------------------------------|
| on_postload_note_create | app.models.models.Notes list |
| on_postload_note_delete | ?                            |
| on_postload_note_update | app.models.models.Notes list |

Note: `on_postload_note_delete` does not seem to call the module `hooks_handler` method.

## IOC

| hook name              | data type                  |
|------------------------|----------------------------|
| on_postload_ioc_create | app.models.models.Ioc list |
| on_postload_ioc_delete | ?                          |
| on_postload_ioc_update | app.models.models.Ioc list |

Notes: 
* `on_postload_ioc_delete` does not seem to call the module `hooks_handler` method.
* export/import csv does not work
* even when importing a csv with two IOCs, hook `on_postload_ioc_create` is called twice with a list of 1 element. 
  I was expecting the hook to be called once with two elements. Is it ever a list of more than one element?

## Event

| hook name                | data type                        |
|--------------------------|----------------------------------|
| on_postload_event_create | app.models.cases.CasesEvent list |
| on_postload_event_delete | ?                                |
| on_postload_event_update | app.models.cases.CasesEvent list |

Note: `on_postload_event_delete` does not seem to call the module `hooks_handler` method.

## Evidence

| hook name                   | data type                               |
|-----------------------------|-----------------------------------------|
| on_postload_evidence_create | app.models.models.CaseReceivedFile list |
| on_postload_evidence_delete | ?                                       |
| on_postload_evidence_update | app.models.models.CaseReceivedFile list |

Note: `on_postload_evidence_delete` does not seem to call the module `hooks_handler` method.

## Task

| hook name               | data type                        |
|-------------------------|----------------------------------|
| on_postload_task_create | app.models.models.CaseTasks list |
| on_postload_task_delete | ?                                |
| on_postload_task_update | app.models.models.CaseTasks list |

Note: `on_postload_task_delete` does not seem to call the module `hooks_handler` method.

## Report

| hook name                            | data type |
|--------------------------------------|-----------|
| on_postload_report_create            | ?         |
| on_postload_activities_report_create | ?         |

Note: got an exception when trying to generate any kind of reports...
