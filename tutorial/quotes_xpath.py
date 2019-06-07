import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield {
                'quote': quote.xpath('.//span[@class="text"]/text()').get(),
                'author': quote.xpath('.//small[@class="author"]/text()').get()
            }
