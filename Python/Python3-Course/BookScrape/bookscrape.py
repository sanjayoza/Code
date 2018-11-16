# http://books.toscrape.com
# We are writing a spider to scrape pages by following links

# TO RUN THIS USE THE FOLLOWING COMMAND:
# you can write it to .json or .csv file
# /home/soza/.local/bin/scrapy runspider -o books.csv bookscrape.py  # name of file

import scrapy

class BookSpider(scrapy.Spider):
    name ='bookspider'
    urls = ["http://books.toscrape.com"] # can have multiple here
    
    # scrapy looks for this method to pass data back
    def parse(self, response):
        for article in response.css("article.product_pod"):   # from html page
            yield {
                'price' : article.css(".price_color::text").extract_first(),
                'title' : article.css("h3 > a::attr(title)").extract_first()
                }
            # look for the next button on the bottom of the page to get to 
            # the next link
            next = response('.next > a::attr(href))').extract_first()
            # if next is present then call parse again
            if next:
                yield response.follow(next, self.parse)
    

	