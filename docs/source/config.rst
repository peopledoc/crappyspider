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

Login error selector
--------------------
The selector where the crawler should look for errors after a login attempt.