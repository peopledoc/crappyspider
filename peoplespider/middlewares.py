# import ipdb
import re
import json

from scrapy.exceptions import IgnoreRequest

class PeoplePattern(object):

    visited_patterns = []

    def __init__(self):
        with open('peoplespider/configs/peopleask_manager.json') as fil:
            data = json.load(fil)

        self.patterns = data['patterns']
        self.excluded_patterns = data['excluded_patterns']

    def process_request(self, request, spider):
        for pattern in self.patterns:
            # print(pattern, request.url, bool(re.search(str(pattern), request.url)))
            if bool(re.search(str(pattern), request.url)):
                if pattern in self.visited_patterns:
                    raise IgnoreRequest()
                else:
                    self.visited_patterns.append(pattern)
                    break

        for excluded_pattern in self.excluded_patterns:
            if bool(re.search(str(excluded_pattern), request.url)):
                raise IgnoreRequest()