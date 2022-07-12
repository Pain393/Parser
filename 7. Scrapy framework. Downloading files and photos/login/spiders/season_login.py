import scrapy


class SeasonLoginSpider(scrapy.Spider):
    name = 'season_login'
    allowed_domains = ['scrape.world']
    start_urls = ['https://scrape.world/login/']

    def parse(self, response):
        csrf_token = response.xpath('//input[@id="csrf_token"]/@value').get()
        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//form',
            formdata={
                'csrf_token': csrf_token,
                'username': 'admin',
                'password': 'admin',
                'next': '/season'
            },
            callback=self.after_login
        )

    def after_login(self, response):
        global division
        tables = response.xpath('//tr')
        for row in tables:
            divis = row.xpath('.//strong/text()').get()
            rk = row.xpath('.//th[@scope="row"]/text()').get()
            if divis != None:
                division = divis
            elif rk != None:
                yield {
                    'Division': division,
                    'RK': rk,
                    'Team': row.xpath('.//td[@data-stat="team_name"]/text()').get(),
                    'W': row.xpath('.//td[@data-stat="wins_avg"]/text()').get(),
                    'L': row.xpath('.//td[@data-stat="losses_avg"]/text()').get(),
                    'OL': row.xpath('.//td[@data-stat="losses_ot_avg"]/text()').get(),
                    'PTS': row.xpath('.//td[@data-stat="points_avg"]/text()').get()
                }

