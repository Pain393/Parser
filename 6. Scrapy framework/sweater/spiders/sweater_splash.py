import scrapy
from scrapy_splash import SplashRequest

class SweaterSplashSpider(scrapy.Spider):
    name = 'sweater_splash'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/']

    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return splash:html()   
        end
    '''

    def start_requests(self):
        yield SplashRequest(
            url='https://scrapingclub.com/exercise/detail_sign/',
            callback=self.parse,
            endpoint='execute',
            args={
                'lua_source': self.script
            }
        )

    def parse(self, response):
        yield {
            'image': response.urljoin(response.xpath('//img[contains(@class, "card-img-top")]/@src').get()),
            'title': response.xpath('//h4[@class="card-title"]/text()').get(),
            'price': response.xpath('//h4[@class="card-price"]/text()').get(),
            'description': response.xpath('//p[@class="card-description"]/text()').get()
        }
