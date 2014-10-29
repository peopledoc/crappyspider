#import ipdb

from scrapy.spider import Spider
from scrapy.http import FormRequest, Request
from scrapy.selector import Selector
from scrapy import log


class PeopleAskEmployee(Spider):
    name = 'peopleask_employee'
    allowed_domains = ['peopleask.local']
    start_urls = ['http://peopleask.local/employee']

    def parse(self, response):
        return [FormRequest.from_response(
            response, formdata={'email': 'bernard', 'password': 'abcd1234'},
            callback=self.after_login)]

    def after_login(self, response):
        # check login succeed before going on
        sel = Selector(response)
        # ipdb.set_trace()
        if sel.css('.alert-error'):
            log.msg('Login failed', level=log.ERROR)
            return

        # continue scraping with authenticated session
        log.msg('Login success', level=log.INFO)

        for url in sel.css('a::attr(href)').extract():
            if url != '/logout/':
                yield Request(url='http://peopleask.local' + url,
                              callback=self.parse_page)

    def parse_page(self, response):
        sel = Selector(response)
        for url in sel.css('a::attr(href)').extract():
            if url != '/logout/':
                yield Request(url='http://peopleask.local' + url,
                              callback=self.parse_page)


class PeopleAskManager(Spider):
    name = 'peopleask_manager'
    allowed_domains = ['peopleask.local']
    start_urls = ['http://peopleask.local/manager']

    def parse(self, response):
        return [FormRequest.from_response(
            response, formdata={'email': 'admin', 'password': 'admin1234'},
            callback=self.after_login)]

    def after_login(self, response):
        # check login succeed before going on
        sel = Selector(response)
        # ipdb.set_trace()
        if sel.css('.errorlist'):
            log.msg('Login failed', level=log.ERROR)
            return

        # continue scraping with authenticated session
        log.msg('Login success', level=log.INFO)

        for url in sel.css('a::attr(href)').extract():
            yield Request(url='http://peopleask.local' + url,
                          callback=self.parse_page)

    def parse_page(self, response):
        log.msg('Status code page {status_code} for {url}'.format(
            status_code=response.status, url=response.url), level=log.INFO)
        sel = Selector(response)
        for url in sel.css('a::attr(href)').extract():
            yield Request(url='http://peopleask.local' + url,
                          callback=self.parse_page)
