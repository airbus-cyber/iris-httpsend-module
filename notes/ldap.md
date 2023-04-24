# Setting up a ldap service

```
  opendldap:
    image: bitnami/openldap:2
    networks:
      - iris_frontend
    ports:
      - '1389:1389'
    container_name: iris_ldap
    environment:
      - LDAP_ADMIN_USERNAME=admin
      - LDAP_ADMIN_PASSWORD=adminpassword
      - LDAP_USERS=administrator,user1,user2
      - LDAP_PASSWORDS=password0,password1,password2
```

To check ldap is up and running
* from the host
```
apt install ldap-utils
ldapsearch -H ldap://127.0.0.1:1389 -b "dc=example,dc=org" -D "cn=admin,dc=example,dc=org" -w adminpassword
```

* from the docker
```
docker exec -ti iriswebapp_app /bin/bash
apt install ldap-utils
ldapsearch -H ldap://iris_ldap:1389 -b "dc=example,dc=org" -D "cn=admin,dc=example,dc=org" -w adminpassword
```

* with python from the docker
```
from ldap3 import Server
from ldap3 import Connection
server = Server('ldap://iris_ldap:1389')
c = Connection(server, user="cn=user1,ou=users,dc=example,dc=org", password="password1")
c.bind()    # should be True
```

## Fill ldap from a .ldif file

We may want to instead fill the ldap with a .ldif file. This is useful, for instance, to be able to set a mail and displayName to users.
```
  opendldap:
    image: bitnami/openldap:2
    networks:
      - iris_frontend
    ports:
      - '1389:1389'
    container_name: iris_ldap
    environment:
      - LDAP_ADMIN_USERNAME=admin
      - LDAP_ADMIN_PASSWORD=adminpassword
    volumes:
      - ./ldifs:/ldifs
```

The local `ldifs` directory contains the .ldif file that will be loaded. See [users.ldif](users.ldif) for an example.
Then to retrieve the mail and displayName attributes with python:
```
from ldap3 import Server
from ldap3 import Connection
server = Server('ldap://iris_ldap:1389')
c = Connection(server, user='cn=user1,ou=users,dc=example,dc=org', password='password1')
c.bind()
c.search('cn=user1,ou=users,dc=example,dc=org', '(objectClass=*)', attributes=['mail', 'displayName'])
entry = c.entries[0]
display_name = entry['displayName'].value
mail = entry['mail'].value
print(f'Found user "{display_name}" with email "{mail}"')
```

# Iris LDAP configuration

```
IRIS_AUTHENTICATION_TYPE=ldap
LDAP_SERVER=iris_ldap
LDAP_AUTHENTICATION_TYPE=SIMPLE
LDAP_PORT=1389
LDAP_USER_PREFIX=cn=
LDAP_USER_SUFFIX=ou=users,dc=example,dc=org
LDAP_USE_SSL=False
```

# Notes

* there is no official documentation yet
* variable `LDAP_AUTHENTICATION_TYPE` is not present in the .env.model
* the user `administrator` must necessarily be present in the ldap
* except for `administrator`, all users must be manually created in Iris before login.
  This should be possible using the REST API through the [add user endpoint](https://docs.dfir-iris.org/_static/iris_api_reference_v1.0.3.html#operation/post-manage-users-add).
* when creating users, a password must be set. Even though it is not necessary with ldap

