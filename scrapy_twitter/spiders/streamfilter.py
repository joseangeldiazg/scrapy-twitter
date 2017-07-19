import scrapy

from scrapy_twitter.twitterutils import TwitterStreamFilterRequest, to_item

class StreamFilterSpider(scrapy.Spider):
    name = "stream-filter"
    allowed_domains = ["twitter.com"]

    def __init__(self, track = None, *args, **kwargs):
        if not track:
            raise scrapy.exceptions.CloseSpider('Argument track not set.')
        super(StreamFilterSpider, self).__init__(*args, **kwargs)
        self.track = track.split(',')

    def start_requests(self):
        return [ TwitterStreamFilterRequest(track = self.track) ]

    def parse(self, response):
        for tweet in response.tweets:
            yield to_item(tweet)
