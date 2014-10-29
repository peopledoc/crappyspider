# import ipdb
import re

from scrapy.exceptions import IgnoreRequest


class PeoplePattern(object):
    visited_patterns = []

    def process_request(self, request, spider):
        for pattern in spider.config['patterns']:
            if bool(re.search(str(pattern), request.url)):
                if pattern in self.visited_patterns:
                    raise IgnoreRequest()
                else:
                    self.visited_patterns.append(pattern)
                    break

        for excluded_pattern in spider.config['excluded_patterns']:
            if bool(re.search(str(excluded_pattern), request.url)):
                raise IgnoreRequest()
