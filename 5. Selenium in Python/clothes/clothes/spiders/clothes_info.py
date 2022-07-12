import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ClothesInfoSpider(CrawlSpider):
    name = 'clothes_info'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[contains(text(), "Next")]'), follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="card"]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//h3[@class="card-title"]/text()').get()
        item['price'] = response.xpath('//div[@class="card-body"]/h4/text()').get()
        item['image'] = response.urljoin(response.xpath('//img[contains(@class, "card-img-top")]/@src').get())
        item['text'] = response.xpath('//p[@class="card-text"]/text()').get()
        return item
