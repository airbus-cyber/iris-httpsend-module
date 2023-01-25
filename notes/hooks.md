# Documentation

* https://docs.dfir-iris.org/development/hooks/

# Postload Hooks

## Case

| hook name               | type  |
|-------------------------|-------|
| on_postload_case_create | list  |
| on_postload_case_delete | |

## Asset
  'on_postload_asset_create', 'on_postload_asset_delete', 'on_postload_asset_update',

## Note
  'on_postload_note_create', 'on_postload_note_delete', 'on_postload_note_update',

## IOC
  'on_postload_ioc_create', 'on_postload_ioc_delete', 'on_postload_ioc_update',

## Event
  'on_postload_event_create', 'on_postload_event_delete', 'on_postload_event_update',

## Evidence
  'on_postload_evidence_create', 'on_postload_evidence_delete', 'on_postload_evidence_update',

## Task
  'on_postload_task_create', 'on_postload_task_delete', 'on_postload_task_update',

## Report
  'on_postload_report_create', 'on_postload_activities_report_create'