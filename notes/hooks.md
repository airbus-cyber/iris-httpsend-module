# Documentation

* https://docs.dfir-iris.org/development/hooks/

# Postload Hooks

## Case

| hook name               | data type                                  |
|:------------------------|--------------------------------------------|
| on_postload_case_create | app.models.cases.Cases list (of 1 element) |
| on_postload_case_delete | ?                                          |

Note: `on_postload_case_delete` does not seem to call the module `hooks_handler` method.
Maybe because the object is already removed from the database?

## Asset
| hook name                | data type |
|--------------------------|-----------|
| on_postload_asset_create | ? list    |
| on_postload_asset_delete | ?         |
| on_postload_asset_update | ? list    |

Note: `on_postload_asset_delete` does not seem to call the module `hooks_handler` method. 
(see behavior with `iris_check_module`)

## Note

| hook name               | data type |
|-------------------------|-----------|
| on_postload_note_create | ?         |
| on_postload_note_delete | ?         |
| on_postload_note_update | ?         |

## IOC

| hook name              | data type |
|------------------------|-----------|
| on_postload_ioc_create | ?         |
| on_postload_ioc_delete | ?         |
| on_postload_ioc_update | ?         |

## Event

| hook name                | data type |
|--------------------------|-----------|
| on_postload_event_create | ?         |
| on_postload_event_delete | ?         |
| on_postload_event_update | ?         |

## Evidence

| hook name                   | data type |
|-----------------------------|-----------|
| on_postload_evidence_create | ?         |
| on_postload_evidence_delete | ?         |
| on_postload_evidence_update | ?         |

## Task

| hook name               | data type |
|-------------------------|-----------|
| on_postload_task_create | ?         |
| on_postload_task_delete | ?         |
| on_postload_task_update | ?         |

## Report

| hook name                            | data type |
|--------------------------------------|-----------|
| on_postload_report_create            | ?         |
| on_postload_activities_report_create | ?         |
