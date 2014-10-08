# -*- coding: utf-8 -*-
import scrapy
import string
import urlparse
from yoryor.items import ArtistItem
from uuid import uuid1


class YoryorspiderSpider(scrapy.Spider):
    name = "yoryorspider"
    allowed_domains = ["yoryor.com"]
    start_urls = (
        'http://www.yoryor.com/',
    )

    def start_requests(self):
        start_urls = ['http://www.yoryor.com/artists/%s' % i for i in string.lowercase]
        return [scrapy.http.Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        hxs = scrapy.Selector(response)
        artists = hxs.xpath('//*[@class="row sqs-row"]/div[@class="col sqs-col-3 span-3"]//p[@class="text-align-center"]')
        for artist in artists:
            name = artist.xpath('a/text()').extract()
            link = artist.xpath('a/@href').extract()
            if len(link) > 0:
                # item['name'] = name[0]
                # item['link'] = self.start_urls[0][:-1] + link[0]
                yield scrapy.http.Request(url=self.start_urls[0][:-1]+link[0], callback=self.get_artist)

    def get_artist(self, response):
        hxs = scrapy.Selector(response)
        item = ArtistItem()
        item['id'] = str(uuid1())
        item['name'] = response.xpath('//header//h1/text()').extract()[0]
        item['link'] = response.url
        item['cover'] = response.xpath('//div[@class="album-cover content-fill"]/img/@data-src').extract()[0]
        # songs = response.xpath('//ul[@class="tracks"]/li[@class="track"]')
        # song_links = response.xpath('//ul[@class="tracks"]/li/div/div/a/@href')
        # for song in songs:
        #     print "Link to song --> ", song.xpath('/a/@href')
        #     name = song.xpath('/text()').extract()
        #     link = song.xpath('/@href').extract()
        #     item['songs'] = dict({"name": name, "link": link})

        # item['songs'] = [dict({"name": n}) for n in response.xpath('//ul[@class="tracks"]/li/div/div/a/text()').extract()]
        song_names = response.xpath(
            '//ul[@class="tracks"]/li/div/div/a/text()'
        ).extract()
        song_links = response.xpath(
            '//ul[@class="tracks"]/li/div/div/a/@href'
        ).extract()
        item['songs'] = [dict(zip(song_names, song_links))]
        yield item
