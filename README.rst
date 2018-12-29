OpenDHT REST v0.1.0
=============================
OpenDHT REST is an API allowing for RESTful interaction with the `OpenDHT library <https://github.com/savoirfairelinux/opendht/>`_.

Documentation
----------------------------------
After `building the OpenDHT library <https://github.com/savoirfairelinux/opendht/wiki/Build-the-library>`_ and enabling Python Bindings, install the dependencies ::


    pip install -r requirments.txt


This should install `Flask <https://github.com/pallets/flask>`_ and `Connexion <https://github.com/zalando/connexion>`_ if they have not been installed already.
Flask is used to create a simple web server using their framework. Connexion will allow
OpenDHT REST to access the `Swagger <https://swagger.io/docs/specification/basic-structure/>`_ specification with Flask.
Once installed, start the web server ::
    cd opendht_rest && python core.py
This will start the web server which serves the REST API endpoints specified in the ``swagger.yml`` file

Endpoints
----------------------------------

+---------+------------+---------------------------------------+------------------------------------+
| Method  | Endpoint                                           | Description                        |
+=========+====================================================+====================================+
| GET     | ``localhost:5000/v1/fetch/{key}``                  | Fetch value data for provided key  |
+---------+----------------------------------------------------+------------------------------------+
| POST    | ``localhost:5000/v1/post/key{key}/value/{value}``  | Append provided key-value pair     |
+---------+----------------------------------------------------+------------------------------------+