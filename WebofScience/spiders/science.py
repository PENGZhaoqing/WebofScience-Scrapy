from scrapy.selector import Selector
from bs4 import BeautifulSoup

try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from WebofScience.items import PaperDataItem
import re
import os
import ast
import json

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
        "http://apps.webofknowledge.com/summary.do;jsessionid=A9D618BE59DD93A1B8225931330AF5E4?product=UA&doc=1&qid=1&SID=5Afv1eg5hfB1pJv7Owq&search_mode=AdvancedSearch&update_back2search_link_param=yes"
    ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r'.*page=\d+&doc=\d+.*')), follow=True, callback='parse_page')
    ]

    def parse_page(self, response):
        body = BeautifulSoup(response.body, 'html.parser')

        # title
        try:
            title = body.find('div', 'title').value.get_text()
        except:
            return

        if title in endpoint:
            return

        # ISSN
        try:
            ISSN = body.find(text=re.compile("ISSN")).parent.next_sibling.next_sibling.get_text()
        except:
            ISSN = ""

        # document type, note the page must be English
        try:
            doc_type = body.find(text=re.compile("Document Type")).parent.next_sibling
        except:
            doc_type = ""

        # journal
        try:
            journal = body.find('p', 'sourceTitle').value.get_text()
        except:
            journal = ""

        # author
        author_str = ""
        try:
            for i in body.find(text=re.compile("By:")).parent.parent.strings:
                author_str += i.replace(' ', '').replace('\n', '')
        except:
            pass

        # address and correspond_adds
        correspond_addrs = []
        addrs = []
        try:
            addr_tables = body.find_all("table", "FR_table_noborders")
            if len(addr_tables) > 0:
                for addr in addr_tables[0].select('td.fr_address_row2'):
                    correspond_addrs.append(addr.get_text().replace('\n', ''))

            if len(addr_tables) > 1:
                for addr in addr_tables[1].select('td.fr_address_row2'):
                    addrs.append(addr.get_text().replace('\n', ''))
        except:
            pass

        # save
        item = PaperDataItem()
        item['title'] = title
        item['author'] = author_str
        item['journal'] = journal
        item['doc_type'] = doc_type
        item['correspond_adds'] = correspond_addrs
        item['address'] = addrs
        item['ISSN'] = ISSN
        endpoint.add(title)
        yield item
