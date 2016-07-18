from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider

class CrawlerRedis(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'crawler_redis'
    redis_key = 'crawler:start_urls'

    """Spider that reads urls from redis queue when idle."""

    rules = (
        # follow all links
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(CrawlerRedis, self).__init__(*args, **kwargs)

    def parse_page(self, response):
        data = {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
        import  pprint
        pprint.pprint(data)
        return data