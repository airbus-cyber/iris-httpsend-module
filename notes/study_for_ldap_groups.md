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

