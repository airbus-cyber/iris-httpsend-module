# Notes for iris-web issue dfir-iris/iris-web#252
* https://github.com/dfir-iris/iris-web/issues/252
* the study is done on v2.3.1
* dfir-iris uses [Flask-Login](https://flask-login.readthedocs.io/en/latest/) for user session management and Flask-SQLAlchemy to access the database

# Design decision
Interesting discussion here https://sqa.stackexchange.com/questions/15133/should-username-login-id-be-case-sensitive.
An answer states "For usability reasons, if a username is case sensitive it shouldn't be allowed to create accounts with the same name but different capitalization. This part I'd definitely see as a bug.", another that "From a UX perspective usernames should NEVER be case sensitive."

# Analysis

## Modules
* app.blueprints.login.login_routes: /login route implementation
* app.iris_engine.access_control.ldap_handler: for ldap authentication and automatic provisioning when AUTHENTICATION_CREATE_USER_IF_NOT_EXIST is set
* app.util
    * performs login in the case of open id connect (oidc), using the user email (which should also be a unique identifier I guess)
    * method is_user_authenticated, to check is the user is already authenticated
    * used in the definition of annotations api_login_required, ac_case_requires, ac_socket_requires, ac_requires, ac_api_case_requires and ac_api_requires
* app.datamgmt.manage.manage_users_db: user management in database, in particular it provides method create_user
* app.models.authorization contains the User database definition, field user is the login (Unique), field name is the displayed name (not Unique), email (Unique), uuid, api_key and external_key fields are Unique too, id is the primary key (so necessarily unique too)

## User creation and update
* User creation (calls to method create_user) is performed in two places: user creation endpoint /manage/users/add (app.blueprints.manage.manage_users.add_user) and in case of automatic ldap user provisioning (app.iris_engine.access_control.ldap_handler)
* app.datamgmt.manage.manage_users_db.update_user

## User retrieval
Calls to get_active_user_by_login and get_user_by_username (and other calls User.query.filter)
* password authentication gets the user by login (https://github.com/dfir-iris/iris-web/blob/v2.3.1/source/app/blueprints/login/login_routes.py#L97)
* ldap authentication gets the user by login after authentication (https://github.com/dfir-iris/iris-web/blob/v2.3.1/source/app/blueprints/login/login_routes.py#L86)
* to check if the user exists, ldap automatic provisioning searches the user by login (https://github.com/dfir-iris/iris-web/blob/v2.3.1/source/app/iris_engine/access_control/ldap_handler.py#L45)
* Carefull, there is all app.schema.marshables.UserSchema, verify_username!!! (https://github.com/dfir-iris/iris-web/blob/v2.3.1/source/app/schema/marshables.py#L713)
* API route /manage/users/lookup/login/<string:login> (https://github.com/dfir-iris/iris-web/blob/v2.3.1/source/app/blueprints/manage/manage_users.py#L467)


# Conclusion

The option "case insensitive comparison so database fields can keep their initial case and would be shown that way in the interface" is appealing because there wouldn't be any need for migration. 
Still, a tool must be run to check there are no two accounts with the same login once in lower case. This is our starting assumption.
This avoids the problematic scenario: the application will have no way to tell which user to pick, if they have the same login once in lower case. If the application retrieves the an arbitrary user, it could result into a user login into the other's account.
We have to find a way to retrieve all users based on their login once converted to lower case (https://stackoverflow.com/questions/16573095/case-insensitive-flask-sqlalchemy-query). It is feasible but not as direct as retrieving the user by its login.

So it seems preferable to enforce all logins to lower case in database. This can be done in two ways either at the boundaries of the database, or at the boundaries of the application. I think I prefer at the boundaries of the application. Because we can enforce lower case once at the entry point rather than at each database operation. To enforce unicity at the database level, we could still https://stackoverflow.com/questions/50056605/how-to-add-uniqueconstraint-in-sqlalchemy.

We could still implement an hybrid solution according to the IRIS_AUTHENTICATION_TYPE. Implementation for local authentification would not change and only in ldap would the users be created with a lower case login. However, we have to keep in mind, that in ldap, users can either be created automatically or by the API. So it would make for a more complex implementation (enforcing lower case according to some configuration flags). Also the possibility of having the IRIS_AUTHENTICATION_TYPE change during the life of the product can not be entirely excluded. This options seems perilous.

We chose to keep the users case in the database and perform case-insensitive checks/retrieval on the login.

## Implementation hints
Application boundaries:
* API user creation https://github.com/dfir-iris/iris-web/blob/v2.3.1/source/app/blueprints/manage/manage_users.py#L105
* user loging https://github.com/dfir-iris/iris-web/blob/v2.3.1/source/app/blueprints/login/login_routes.py#L126
* user update https://github.com/dfir-iris/iris-web/blob/v2.3.1/source/app/blueprints/manage/manage_users.py#L361
* user update view? https://github.com/dfir-iris/iris-web/blob/v2.3.1/source/app/blueprints/profile/profile_routes.py#L136


To implement the case "insensitive comparison", all the retrieval points should be modified to get the user by login in a case insensitive way (this should be all the code places listed in paragraph [User retrieval](#user-retrieval), it can also be seen by looking at all the calls to `User.query.filter`).
Look all `User.query.filter`, transform `User.user ==` into `User.user.ilike`). Should also group calls to `User.query.filter` in `app.datamgmt.manage.manage_users_db`.

