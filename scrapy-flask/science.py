from scrapy.selector import Selector

try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from WebofScience.items import PaperDataItem

import os
import ast

print os.getcwd()
endpoint = set()

try:
    file = open('papers.json', 'r')
    for line in file:
        line = ast.literal_eval(line)
        endpoint.add(line['title'])
except:
    pass
print len(endpoint)


class PaperSpider(CrawlSpider):
    name = "science"
    allowed_domains = ["apps.webofknowledge.com"]

    start_urls = [
        'http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=AdvancedSearch&parentQid=&qid=1&SID=6AfnEOMoEwhVXDmA5Ec&&update_back2search_link_param=yes'
    ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r'.*page=\d+&doc=\d+.*')), follow=True, callback='parse_page')
    ]

    def parse_page(self, response):
        url = response.request.url
        title = response.css('div.title > value::text').extract()
        author = response.css('p.FR_field > a::text').extract()
        journal = response.css('p.sourceTitle > value::text').extract()
        doc_type = response.css(
            'div.block-record-info.block-record-info-source > p:nth-child(6)::text').extract()
        affiliate = response.css('preferred_org::text').extract()

        if len(title) > 0 and title[0] not in endpoint:
            item = PaperDataItem()
            item['title'] = title[0]
            item['author'] = author
            item['journal'] = journal
            item['doc_type'] = doc_type[1] if len(doc_type) > 1 else ''
            item['affiliate'] = affiliate
            item['url'] = url
            endpoint.add(title[0])
            yield item
