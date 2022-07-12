import scrapy


class ClothesScrapeSpider(scrapy.Spider):
    name = 'clothes_scrape'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    def parse(self, response):
        cards = response.xpath('//div[@class="card"]')
        for card in cards:
            yield {
                'title': card.xpath('.//h4[@class="card-title"]/a/text()').get(),
                'price': card.xpath('.//div[@class="card-body"]/h5/text()').get(),
                'image': response.urljoin(card.xpath('.//img[contains(@class, "card-img-top")]/@src').get())
            }
        next_page = response.xpath("//a[contains(text(), 'Next')]/@href").get()
        if next_page:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
