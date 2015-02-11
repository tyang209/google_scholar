# -*- coding: utf-8 -*-

# Scrapy settings for google_scholar project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'google_scholar'

SPIDER_MODULES = ['google_scholar.spiders']
NEWSPIDER_MODULE = 'google_scholar.spiders'
DOWNLOAD_DELAY=45
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'google_scholar (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED=True
# LOG_ENABLED = True
# LOG_LEVEL = 'INFO' # Levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
# LOG_FILE = './scholar.log'