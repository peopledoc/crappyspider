Sample configuration file
=========================

.. code-block:: json

    {
        "start_urls": ["http://example.com/dashboard"],
        "allowed_domains": ["example.com"],
        "patterns": [
            "/article/[0-9]+",
            "/user/.+",
            "/search/\\?"
        ],
        "excluded_patterns": [
            "/logout/"
        ],
        "credential": {
            "email": "myemail",
            "password": "mypassword"
        },
        "login_error_selector": ".errorlist"
    }

Parameters
==========

Start urls
----------
A set of urls the crawler will start.

Allowed domains
---------------
A set of domains to which the crawl will be restricted.

Patterns
--------
A set of regex representing url patterns to visit only once.

Excluded patterns
-----------------
A set of regex representing url patterns to ignore.

Credential
----------
The credential hash is optional since it is used for sites requiring login.
The underlying hashes are used as names for the login form inputs, so you might have to change them.

Example:

.. code-block:: json

    {
        "credential": {
            "email": "myemail",
            "password": "mypassword"
        },
    }

There's another credential scheme, take a list, with the name of the field.

Example:

.. code-block:: json

    {
        "credential": ["email", "password"]
    }

Then add in your environnement two variables.

Example:

.. code-block:: bash

    export CRAPPYSPIDER_EMAIL=test@test.com
    export CRAPPYSPIDER_PASSWORD=my_password


Login error selector
--------------------
The selector where the crawler should look for errors after a login attempt.
