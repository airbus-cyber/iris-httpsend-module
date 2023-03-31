# Installation

* https://docs.dfir-iris.org/getting_started/
* to find the administrator password
  docker-compose logs | grep create_safe_admin
* login to https://127.0.0.1
* to reset everything and start afresh these commands may be useful
```
  docker volume prune
  docker system prune --volumes
```

# Configuration

* file .env
* administrator API KEY can be configured with variable IRIS_ADM_API_KEY
* variables CERT_FILENAME and KEY_FILENAME which are use in the nginx configuration (docker/nginx/nginx.conf)

# Troubleshooting

* In case you get the following error at startup, this is a network connection error from the webapp to the database. Try pruning the network:
```
iriswebapp_app | 2023-03-31 07:17:58 :: INFO :: post_init :: run_post_init :: IRIS v2.0.0
iriswebapp_app | 2023-03-31 07:17:58 :: INFO :: post_init :: run_post_init :: Running post initiation steps
iriswebapp_app | 2023-03-31 07:17:58 :: INFO :: post_init :: run_post_init :: Adding pgcrypto extension
iriswebapp_app | 2023-03-31 07:17:58 :: ERROR :: views :: <module> :: Post init failed. IRIS not started
iriswebapp_app | Traceback (most recent call last):
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3250, in _wrap_pool_connect
iriswebapp_app |     return fn()
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 310, in connect
iriswebapp_app |     return _ConnectionFairy._checkout(self)
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 868, in _checkout
iriswebapp_app |     fairy = _ConnectionRecord.checkout(pool)
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 476, in checkout
iriswebapp_app |     rec = pool._do_get()
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 146, in _do_get
iriswebapp_app |     self._dec_overflow()
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 70, in __exit__
iriswebapp_app |     compat.raise_(
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
iriswebapp_app |     raise exception
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 143, in _do_get
iriswebapp_app |     return self._create_connection()
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 256, in _create_connection
iriswebapp_app |     return _ConnectionRecord(self)
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 371, in __init__
iriswebapp_app |     self.__connect()
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 666, in __connect
iriswebapp_app |     pool.logger.debug("Error on connect(): %s", e)
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 70, in __exit__
iriswebapp_app |     compat.raise_(
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
iriswebapp_app |     raise exception
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 661, in __connect
iriswebapp_app |     self.dbapi_connection = connection = pool._invoke_creator(self)
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/engine/create.py", line 590, in connect
iriswebapp_app |     return dialect.connect(*cargs, **cparams)
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 597, in connect
iriswebapp_app |     return self.dbapi.connect(*cargs, **cparams)
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/psycopg2/__init__.py", line 122, in connect
iriswebapp_app |     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
iriswebapp_app |   File "/opt/venv/lib/python3.9/site-packages/eventlet/support/psycopg2_patcher.py", line 46, in eventlet_wait_callback
iriswebapp_app |     state = conn.poll()
iriswebapp_app | psycopg2.OperationalError: could not connect to server: Connection refused
iriswebapp_app | 	Is the server running on host "db" (172.18.0.2) and accepting
iriswebapp_app | 	TCP/IP connections on port 5432?
```
