
# Development

* when overriding a method of `IrisModuleInterface`, parameters' names must conform their parent's prototype. 
  For instance, parameter of `register_hooks` should be called `module_id`

# Build and deployment

The list of module installed and registered by default is documented here: https://docs.dfir-iris.org/operations/modules/.
We want to build an instance of iris with another list of modules installed, registered and enabled by default.

## Installation

For the time being, to have an additional module pre-installed during the build:
* copy the module's wheel in `source/dependencies`,
* declare it in the requirement file (`source/requirements.txt`)

It would be nice to have a more legitimate way to achieve this goal.
For instance, the docker build could accept as argument the path to an additional `requirements.txt` file.
This would allow additional dependencies to be installed (either from a wheel or from the python package index).

## Registration

In order to specify the list of modules to register by default at build time, one should modify the `modules` list in 
the `register_default_modules` method of the [post_init code](https://github.com/dfir-iris/iris-web/blob/v2.0.0-beta-3/source/app/post_init.py#L1113).

It is possible to register a module at execution time via the [rest api](rest_api.md#register-module).

## Activation

It seems that no module is active (enabled) by default. This action can be done by the administrator via the REST API (see https://github.com/dfir-iris/iris-web/issues/182). The endpoints are:

| method | url                                           | body                                                            |
|--------|-----------------------------------------------|-----------------------------------------------------------------|
| POST   | /manage/modules/enable/<int:module_id>        | -                                                               |
| POST   | /manage/modules/import-config/<int:module_id> | a JSON similar to the one when clicking on Export configuration |

Example:
```
curl --header 'Authorization: Bearer '${API_KEY} --header 'Content-Type: application/json' --request POST --url http://127.0.0.1:8000/manage/modules/enable/3
```

