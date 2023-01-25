
# Development

* when overriding a method of `IrisModuleInterface`, parameters' names must conform their parent's prototype. 
  For instance, parameter of `register_hooks` should be called `module_id`

# Build and deployment

The list of module installed and registered by default is documented here: https://docs.dfir-iris.org/operations/modules/.
We want to build an instance of iris with another list of modules installed, registered and enabled by default.

## Installation

For the time being, to have an additional module pre-installed during the build:
* copy the module's wheel in `source/dependencies`,
* declare it in the requirement file (`source\requirements.txt`)

It would be nice to have a more legitimate way to achieve this goal.
For instance, the docker build could accept as argument the path to an additional `requirements.txt` file.
This would allow additional dependencies to be installed (either from a wheel or from the python package index).

## Registration

In order to specify the list of modules to register by default, one should modify the `modules` list in 
the [post_init code](https://github.com/dfir-iris/iris-web/blob/v2.0.0-beta-1/source/app/post_init.py#L1015).

It would be nice to have a more legitimate way to do this. 
For instance, via a variable in the `.env` file to specify a custom list of modules to register.

## Activation

It seems that no module is active (enabled) by default. This action should be done manually by the administrator.

It would be nice to be able to specify which module should be active, or more simple for all pre-registered modules 
to be active by default.
