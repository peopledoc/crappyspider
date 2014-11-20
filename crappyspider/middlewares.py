import re

from scrapy.exceptions import IgnoreRequest


class CrappyPattern(object):
    visited_patterns = []

    def process_request(self, request, spider):
        patterns = spider.config.get('patterns', [])
        excluded_patterns = spider.config.get('excluded_patterns', [])

        for pattern in patterns:
            if bool(re.search(str(pattern), request.url)):
                if pattern in self.visited_patterns:
                    raise IgnoreRequest()
                else:
                    self.visited_patterns.append(pattern)
                    spider._url_seen.append({'url': request.url})
                    break

        for excluded_pattern in excluded_patterns:
            if bool(re.search(str(excluded_pattern), request.url)):
                raise IgnoreRequest()
