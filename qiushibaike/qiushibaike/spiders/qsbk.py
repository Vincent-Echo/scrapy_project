# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from qiushibaike.items import QiushibaikeItem

class QsbkSpider(CrawlSpider):
    name = "qsbk"
    allowed_domains = ["qiushibaike.com"]
    start_urls = (
        'http://www.qiushibaike.com/late',
    )

    rules = (
        Rule(LinkExtractor(allow=['late/page/\d+']), callback='parse_item'),
    )

    def parse_item(self, response):
		item = QiushibaikeItem()
		item['image_urls'] = response.xpath('//div[@class="thumb"]/a/img/@src').extract()
		return item