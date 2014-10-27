import ipdb
import re

from scrapy.exceptions import IgnoreRequest
from scrapy import log

class PeoplePattern(object):
    patterns = [
        '/article/',
        '/requests/',
        '/category/',
        '/manager/\?',
        '/manager/article/\?',
        '/administration/form/\?',
        '/administration/form/[0-9]+',
        '/administration/manager/[0-9]+',
        '/administration/role/[0-9]+'
    ]
    visited_patterns = set()

    def process_request(self, request, spider):
        # ipdb.set_trace()
        for pattern in self.patterns:
            if re.search(pattern, request.url):
                if pattern in self.visited_patterns:
                    raise IgnoreRequest()
                else:
                    self.visited_patterns.add(pattern)
                    break
