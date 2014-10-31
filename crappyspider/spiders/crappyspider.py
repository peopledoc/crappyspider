import json
import urlparse

from scrapy.spider import Spider
from scrapy.http import FormRequest, Request
from scrapy.selector import Selector
from scrapy import log


class CrappySpider(Spider):
    name = 'crappyspider'

    def __init__(self, config=None):
        super(CrappySpider, self).__init__()

        if config:
            with open(config) as fil:
                data = json.load(fil)
        else:
            raise ValueError('The config option is required, for example:'
                             ' scrapy crawl crappyspider -a '
                             ' config=my_rule.json')

        self.config = data
        self.start_urls = data['start_urls']
        self.allowed_domains = data['allowed_domains']

    def parse(self, response):
        credential = self.config.get('credential', None)

        if credential:
            return [FormRequest.from_response(
                response, formdata=self.config['credential'],
                callback=self.after_login, errback=self.login_error)]

        return Request(response.url, callback=self.parse_page)

    def login_error(self, response):
        log.msg("Can't reach targeted page! (login ok)", level=log.ERROR)
        return

    def after_login(self, response):
        # check login succeed before going on
        sel = Selector(response)
        if sel.css(self.config['login_error_selector']):
            log.msg('Login failed', level=log.ERROR)
            return

        # continue scraping with authenticated session
        log.msg('Login success', level=log.INFO)

        return self.parse_page(response)

    def parse_page(self, response):
        log.msg('Status code page {status_code} for {url}'.format(
            status_code=response.status, url=response.url), level=log.INFO)
        sel = Selector(response)
        url_prefix = urlparse.urlparse(response.url)

        for url in sel.css('a::attr(href)').extract():
            try:
                yield Request(url, callback=self.parse_page)
            except ValueError:
                url_final = '{scheme}://{netloc}{path}'.format(
                    scheme=url_prefix.scheme, netloc=url_prefix.netloc,
                    path=url)
                yield Request(url_final, callback=self.parse_page)
