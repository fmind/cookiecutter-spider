#!/usr/bin/env python3
"""Documentation of the spider."""

import argparse

import scrapy
import scrapy.http
import scrapy.crawler
import scrapy.settings

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("-l", "--level", default="INFO", help="log level")
parser.add_argument("-f", "--format", default="csv", help="feed format")
parser.add_argument("-o", "--output", default="items.csv", help="feed uri")
parser.add_argument("-j", "--thread", type=int, default=16, help="concurrent")
parser.add_argument("-c", "--cache", action="store_true", help="cache enabled")


class Spider(scrapy.Spider):
    name = "{{cookiecutter.name}}"
    allowed_domains = ["{{cookiecutter.site}}"]
    start_urls = ["https://{{cookiecutter.site}}"]

    def parse(self, response):
        for link in response.css("a"):
            yield {
                "text": link.css("::text").extract_first(),
                "href": link.css("::attr(href)").extract_first(),
            }


def main(args=None):
    opts = parser.parse_args(args)

    settings = scrapy.settings.Settings(
        {
            "LOG_LEVEL": opts.level,
            "FEED_URI": opts.output,
            "FEED_FORMAT": opts.format,
            "HTTPCACHE_ENABLED": opts.cache,
            "CONCURRENT_REQUESTS": opts.thread,
        }
    )

    process = scrapy.crawler.CrawlerProcess(settings)
    process.crawl(Spider)
    process.start()


if __name__ == "__main__":
    main()
