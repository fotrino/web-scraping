import scrapy


class Links(scrapy.Spider):
    name = 'links'
    start_urls = ['https://www.pagina12.com.ar/secciones/sociedad?page=1']

    def parse(self, response):
        for link in response.css('h4.title-list'):
            yield {'url': 'https://www.pagina12.com.ar' + link.css('a').attrib['href']}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
