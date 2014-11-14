.. Crappyspider documentation master file, created by
   sphinx-quickstart on Thu Nov 13 11:58:41 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Crappyspider's documentation!
========================================

* source: https://github.com/novapost/crappyspider
* ticketing: https://github.com/novapost/crappyspider/issues
* documentation: http://crappyspider.readthedocs.org/en/latest/


.. toctree::
   :maxdepth: 2

   config

   command_line

   devguide

What is it?
===========

crappyspider is a generic scrapy spider:

- it crawls a website
- logs on the standard output the visited urls and their http codes
- generates a log file with the visited urls (more data coming soon, such as http codes ;) )

Features
=========

- a login step
- restric crawling through urls patterns (see 'patterns' in the 'config' doc page)
- exclude patterns of urls (see 'excluded_patterns' in the 'config' doc page)

Usage
=====

.. code-block:: bash

	scrapy crawl crappyspider -a start_urls=http://example.com -a allowed_domains=example.com
	scrapy crawl crappyspider -a conf=conf.json -a output=outputfile -a output_format=json

Use cases
=========

After deployment:
-----------------

You will be able to read through the standard input to pick up any HTTP error such as 500's (pink highlight <3 )

.. code-block:: bash

	scrapy crawl crappyspider -a start_urls=http://deployed-site.com -a allowed_domains=deployed-site.com

After code change:
------------------

Feed any functional testing script with this crawler output file.

.. code-block:: bash

	scrapy crawl crappyspider -a config=config.json -a output_filename=log.json


Acknowledgements
================
Thanks to Peopledoc for freeing the project.
