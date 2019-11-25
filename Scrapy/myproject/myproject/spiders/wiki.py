# -*- coding: utf-8 -*-
import scrapy

from myproject.items import BodyContent


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    # 크롤링 대상 도메인 리스트
    # allowed_domains = ['ko.wikipedia.org']
    allowed_domains = ['en.wikipedia.org']
    # 크롤링을 시작하는 URL 리스트
    # start_urls = ['https://ko.wikipedia.org/']
    start_urls = ['https://en.wikipedia.org/']

    def parse(self, response):
        """
        메인 페이지의 토픽 목록에서 링크를 추출하고 출력합니다.
        """
        link = ['/wiki/Korea', '/wiki/United_States', '/wiki/China', '/wiki/Japan']
        print(link)
        for url in link:
            yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        item = BodyContent()
        item['body'] = " ".join(response.xpath('//*[@id="mw-content-text"]/div/p')
                                .xpath('string()').extract())
        yield item
