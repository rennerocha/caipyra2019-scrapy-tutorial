import scrapy


class QuotesSpider(scrapy.Spider):
  name = 'quotes'

  start_urls = ['http://quotes.toscrape.com/']

  def parse(self, response):
    quotes = []
    for quote in quotes:
      yield {
        'quote': "",
        'author': "",
      }

     next_page_url = "/page/4/"
     yield scrapy.Request(url=reponse.urljoin(next_page_url))
