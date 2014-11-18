import json
import urlparse
import os

from scrapy.spider import Spider
from scrapy.http import FormRequest, Request
from scrapy.selector import Selector
from scrapy.xlib.pydispatch import dispatcher
from scrapy import log
from scrapy import signals


class CrappySpider(Spider):
    name = 'crappyspider'

    def __init__(self, config=None, output_format='json',
                 output_filename='output', start_urls=None,
                 allowed_domains=None):
        super(CrappySpider, self).__init__()

        if output_format not in ('json', 'yaml'):
            raise ValueError('Format {extension} is not supported'
                             '(json or yaml)'.format(
                                 extension=output_format))

        if not config and (not start_urls or not allowed_domains):
            raise ValueError('Requires the start_urls and allowed_domains '
                             ' parameters which can be'
                             ' configured in the config file or using the'
                             ' command line. For example:'
                             ' scrapy crawl crappyspider -a '
                             ' start_urls=http://test.com'
                             ' -a allowed_domains=test.com')

        if output_filename == 'output':
            output_filename = '{current_directory}/output.{ext}'.format(
                current_directory=os.getcwd(), ext=output_format)

        if config:
            with open(config) as fil:
                data = json.load(fil)
        else:
            data = {}

        self.output_format = output_format
        self.output_filename = output_filename
        self.config = data
        self.start_urls = start_urls.split() \
            if start_urls else data['start_urls']
        self.allowed_domains = allowed_domains.split() \
            if allowed_domains else data['allowed_domains']
        self._url_seen = []

        dispatcher.connect(self.engine_stopped, signals.engine_stopped)

    def parse(self, response):
        """Check if need login."""
        credential = self.config.get('credential', None)

        if credential:
            if isinstance(credential, dict):
                return [FormRequest.from_response(
                    response, formdata=self.config['credential'],
                    callback=self.after_login, errback=self.login_error)]

            # Get the crendetial from environnement
            data = {}
            for field in credential:
                data[field] = os.environ['CRAPPYSPIDER_' + field.upper()]

            return [FormRequest.from_response(
                response, formdata=data, callback=self.after_login,
                errback=self.login_error)]

        return Request(response.url, callback=self.parse_page)

    def login_error(self, response):
        """To display a message if the login failed."""
        log.msg("Can't reach targeted page! (login ok)", level=log.ERROR)
        return

    def after_login(self, response):
        """After the login check the credential."""
        # check login succeed before going on
        sel = Selector(response)
        if sel.css(self.config['login_error_selector']):
            log.msg('Login failed', level=log.ERROR)
            return

        # continue scraping with authenticated session
        log.msg('Login success', level=log.INFO)

        return self.parse_page(response)

    def parse_page(self, response):
        """Parse the page."""
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

    def engine_stopped(self):
        """Call in the end, to generate a report with all visited url."""
        if self.output_format == 'json':
            with open(self.output_filename, 'w') as outfile:
                json.dump(self._url_seen, outfile)
        else:
            import yaml

            with open(self.output_filename, 'w') as outfile:
                yaml.dump(self._url_seen, outfile)
