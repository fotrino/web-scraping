import scrapy
import json


class Articles(scrapy.Spider):
    name = 'articles'
    start_urls = []

    with open('../articles/world-links.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for link in data:
            start_urls.append(link['url'])

    def parse(self, response):
        for article in response.css('article.article-full'):
            yield {
                'section': "economy",
                'date': article.css('time').attrib['datetime'].split('T')[0],
                'deck': article.css('h4::text').get(),
                'title': article.css('h1::text').get(),
                'lead': article.css('h3::text').get(),
                'tags': article.css('a.tag::text').getall(),
                'author': article.css('.author-name::text').get(default='Por ').replace('Por ', ''),
                'article': " ".join(paragraph.strip() for paragraph in article.css('.article-text').css('p *::text').getall()),
            }
