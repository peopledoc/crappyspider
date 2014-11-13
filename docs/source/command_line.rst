Documentation of the command line
=================================

Few option is avaible via the command line some explain here.

Config
------
This option is to set the path of the configuration file, is not required, but
if not present need start_urls and allowed_domains. Usage example:

.. code-block:: bash

    scrapy crawl crappyspider -a config=my_rule.json


Output format
-------------
This option is to set the format used to generate the report, default value is
json. Support serializer is json and yaml. Usage example:

.. code-block:: bash

    scrapy crawl crappyspider -a config=my_rule.json output_format=json

Output filename
---------------
This option is to set the name of the report file, default value is output and
is saved in the current directory. Usage example:

.. code-block:: bash

    scrapy crawl crappyspider -a config=my_rule.json output_filename=$HOME/visited_url.json

Start urls
----------
This option is to set the start url, the first page to parse, can be set in the
configuration file also. Usage example:

.. code-block:: bash

    scrapy crawl crappyspider -a  start_urls=http://test.com -a allowed_domains=test.com

Allowed domains
---------------
This option is to set the allowed domains, authorized domain parse, can be set
in the configuration file also. Usage example:

.. code-block:: bash

    scrapy crawl crappyspider -a  start_urls=http://test.com -a allowed_domains=test.com
