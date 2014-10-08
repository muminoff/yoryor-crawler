# -*- coding: utf-8 -*-

# Scrapy settings for yoryor project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yoryor'

SPIDER_MODULES = ['yoryor.spiders']
NEWSPIDER_MODULE = 'yoryor.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'YorYorSpider (+http://www.yoryor.com)'

CONCURRENT_REQUESTS=64

