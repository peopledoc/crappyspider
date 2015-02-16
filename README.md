# Introduction

Crappyspider is a generic cralwer. The goal is to stay kiss and simple, test
easily your site. A report is generate with all visited url and can be used by
other tool to make functional test.

# Install

The project is available on pypi:

    pip install crappyspider

Or from source:

    python setup.py install

# USAGE

Then you can run a spider:

    scrapy crawl crappyspider -a config=my_rule.json

See http://crappyspider.readthedocs.org/en/latest/ for further information.
