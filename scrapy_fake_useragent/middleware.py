from fake_useragent import UserAgent
from scrapy import log

class RandomUserAgentMiddleware(object):
    def __init__(self):
        super(RandomUserAgentMiddleware, self).__init__()

        self.ua = UserAgent()

    def process_request(self, request, spider):
    	ua = self.ua.random
        request.headers.setdefault('User-Agent', ua)
        spider.log(u'Headers: %s' % request.headers.to_string(), level = log.INFO)
