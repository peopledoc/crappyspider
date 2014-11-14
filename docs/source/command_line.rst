Documentation of the command line
=================================

A few options are avaible via the command line.

Each option is to be preceeded by the `-a` argument. See examples below.

Config
------
This option is used to set the path of the configuration file.
It is not required, but
if not specified, you will need to enter the start_urls and allowed_domains parameters via the command line.
Usage example:

.. code-block:: bash

    scrapy crawl crappyspider -a config=my_rule.json


Output format
-------------
This option is used to set the formating of the generated report.
Default value is json.
Supported formats are json and yaml.
Usage example:

.. code-block:: bash

    scrapy crawl crappyspider -a config=my_rule.json -a output_format=json

Output filename
---------------
This option is used to set the name of the report file.
Default value is `output` (and is thus saved in the current directory).
Usage example:

.. code-block:: bash

    scrapy crawl crappyspider -a config=my_rule.json output_filename=$HOME/visited_url.json

Start urls
----------
This option is used to set the page where the crawler will start.
Usage example:

.. code-block:: bash

    scrapy crawl crappyspider -a  start_urls=http://test.com -a allowed_domains=test.com
    scrapy crawl crappyspider -a  start_urls="http://foo.com http://bar.com" -a allowed_domains="foo.com bar.com baz.com"

Allowed domains
---------------
This option is used to set the allowed domains, to which the crawl will be restricted.
Usage example:

.. code-block:: bash

    scrapy crawl crappyspider -a  start_urls=http://test.com -a allowed_domains=test.com
