# -*- coding: utf-8 -*-

# Scrapy settings for peoplespider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'peoplespider'

SPIDER_MODULES = ['peoplespider.spiders']
NEWSPIDER_MODULE = 'peoplespider.spiders'
DOWNLOADER_MIDDLEWARES = {'peoplespider.middlewares.PeoplePattern': 100}
LOG_LEVEL = 'INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'peoplespider (+http://www.yourdomain.com)'
