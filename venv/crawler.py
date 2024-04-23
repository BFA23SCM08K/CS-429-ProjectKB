import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class WebCrawler(scrapy.Spider):
    name = "web_crawler"

    def __init__(self, seed_url, max_pages, max_depth):
        super(WebCrawler, self).__init__()
        self.start_urls = [seed_url]
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.crawled_pages = 0

        self.custom_settings = {
            'DEPTH_LIMIT': self.max_depth,
            'CLOSESPIDER_PAGECOUNT': self.max_pages,
            'AUTOTHROTTLE_ENABLED': True,
            'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        }

    def parse(self, response):
        yield {
            'url': response.url,
            'html_content': response.text
        }
        links = response.css('a::attr(href)').getall()
        for link in links:
            if link.startswith("/"):
                link = response.urljoin(link)
            elif not link.startswith("http"):
                continue
            if self.crawled_pages < self.max_pages:
                self.crawled_pages += 1
                yield response.follow(link, callback=self.parse)

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(WebCrawler, seed_url='https://stackoverflow.com/questions/tagged/api', max_pages=100, max_depth=3)
    process.start()
