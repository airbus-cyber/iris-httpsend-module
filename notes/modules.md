
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

It is possible to register a module at execution time via the [rest api](rest_api.md#register-a-module).

## Activation

It seems that no module is active (enabled) by default. 
A module can be [enabled](rest_api.md#enable-a-module) and also [configured](rest_api.md#configure-a-module) by the administrator via the REST API (see https://github.com/dfir-iris/iris-web/issues/182).

