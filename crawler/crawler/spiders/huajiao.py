# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class HuaJiaoSpider(CrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'huajiao'
    """Spider that reads urls from redis queue when idle."""

    allowed_domains = ['huajiao.com']
    start_urls = ["http://www.huajiao.com"]

    rules = (
        Rule(LinkExtractor("l/([\d]+)")),
        Rule(LinkExtractor("user/([\d]+)"), callback='parse_user'),
        Rule(LinkExtractor("category/([\d]+)/pageno=([\d]+)")),
    )

    def parse_user(self, response):
        data = {
            'name': response.xpath('//*[@id="userInfo"]/div[2]/div/h3/text()').extract_first(),
            'level': response.xpath('//*[@id="userInfo"]/div[2]/div/h3/span/text()').extract_first(),
            'about': response.xpath('//*[@id="userInfo"]/div[2]/div/p[2]/text()').extract_first(),
            'follower_count': response.xpath('//*[@id="userInfo"]/div[2]/div/ul/li[1]/p/text()').extract_first(),
            'fans_count': response.xpath('//*[@id="userInfo"]/div[2]/div/ul/li[2]/p/text()').extract_first(),
            'like_count': response.xpath('//*[@id="userInfo"]/div[2]/div/ul/li[3]/p/text()').extract_first(),
            'exp_count': response.xpath('//*[@id="userInfo"]/div[2]/div/ul/li[4]/p/text()').extract_first(),
            'user_id': response.url.split("/")[-1],
            'url': response.url,
        }
        return data