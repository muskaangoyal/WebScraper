# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.ssense.com/en-us/men"]
    #start_urls= ['https://www.ssense.com/en-us/men?page=2']
    start_urls = ['https://www.ssense.com/en-us/men?page=%s' % page for page in range(2,264)]
    rules = (Rule(LinkExtractor(allow=(), restrict_css=('router-link-active',)),
             callback="parse",
             follow=True),)

    def parse(self, response):
        for href in response.css(" > li > a::attr('href')"):
            url = response.urljoin(href.extract()
            yield scrapy.Request(url, callback = self.parse_dir_contents)

    def parse_detail_page:
        title = response.css('h2::text').extract()[0].strip()
        price = response.css("h3 > span").extract()[0].split()[1]

        item = SsenseItem()
        item['title'] = title
        item['price'] = price
        item['url'] = response.url
        yield item


        //*[@id="wrap"]/div/div[1]/section/div[1]/div/figure[2]/a
        #wrap > div > div.span12.browsing-column.browsing-center-column.tablet-landscape-full-fluid-width > section > div.browsing-product-content > div > figure:nth-child(2) > a
