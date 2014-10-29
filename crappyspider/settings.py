# -*- coding: utf-8 -*-

# Scrapy settings for crappyspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crappyspider'

SPIDER_MODULES = ['crappyspider.spiders']
NEWSPIDER_MODULE = 'crappyspider.spiders'
DOWNLOADER_MIDDLEWARES = {'crappyspider.middlewares.CrappyPattern': 100}
LOG_LEVEL = 'INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crappyspider (+http://www.yourdomain.com)'
