# Implementation notes

* the implementation uses python package ldap3, version 2.9.1
* It seems the bind account is only necessary to provision user. 
  What's the point of binding and getting the user's information if he is already present in IRIS?
  Are we really suppose to do things this way? In particular are we supposed to bind twice, once with the bind account and once with the user?
  Can't we check the user authentication with just the bind accound and some query?
* would be better to code with classes, rather than just public method. Would allow to factor code more (for instance app.config.get('LDAP_AUTHENTICATION_TYPE') could rather be stored in a private field in ldap_handler)
* in ldap_handler, why this (unnecessary and remove?):
```
    except Exception as e:
        raise Exception(e.__str__())
```
* should we remove groups in IRIS when they disappear from LDAP_GROUP_BASE?
* seems to me, configuration of LDAP is getting too complex: should try to eliminate variables
* to create a group, it we need to set field group_permissions. The set of all permissions can be retrieved with `from app.iris_engine.access_control.utils import ac_get_mask_full_permissions`
* Thus, I believe we shouldn't be trying to create groups in IRIS. We can/remove them from user, but not create them. There is missing information in the LDAP. Or should we create with group_permissions set to 0 (no permissions at all, this will require an administrator intervention to update, anyway so what's the point). Note, that if we have IRIS create/remove groups, we need two additional configuration variables: LDAP_GROUP_BASE and LDAP_GROUP_OBJECT_CLASS (respectively equal to ou=IRIS,ou=groups,dc=example,dc=org and groupOfUniqueNames in my use case)
* carefull with this update, there is a breaking change, since variable IRIS_NEW_USERS_DEFAULT_GROUP has been removed in .env

# Test cases

## Group to add to user
* user has a group in LDAP, but not yet in IRIS
* at first login, the group should be added to the user

## Group to remove from user
* user has a group in IRIS, but not anymore in LDAP
* at first login, the group should be removed to the user

## User without any groups should not fail at login

## Non IRIS groups
* user has a group from another application, which does not belong to the LDAP_GROUP_BASE_DN
* check the user does not belong to the other application's group

## Group not already in IRIS should be created from LDAP
* user has a group which is not yet in IRIS
* group should be automatically create in IRIS with no permissions

