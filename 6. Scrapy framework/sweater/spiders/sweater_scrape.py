import scrapy


class SweaterScrapeSpider(scrapy.Spider):
    name = 'sweater_scrape'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/']

    def parse(self, response):
        # sweater = response.xpath('.//div[contains(@class, "card")]')
        # for el in sweater:
        yield {
            'image': response.urljoin(response.xpath('//img[contains(@class, "card-img-top")]/@src').get()),
            # 'title': response.xpath('//h4[@class="card-title"]/text()').get(),
            # 'price': response.xpath('//h4[@class="card-price"]/text()').get(),
            # 'description': response.xpath('//p[@class="card-description"]/text()').get()
        }
