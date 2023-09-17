import scrapy
from scrapy.http import FormRequest

class GetFormSpider(scrapy.Spider):
    name = 'post_form'
    allowed_domains = ['pythonscraping.com']

    def start_requests(self):
        names = ['Sonya', 'Plamen', 'Mihaela']
        quests = ['to go on vacation', 'to win the game', 'to go to school']
        return [FormRequest(
            'http://pythonscraping.com/linkedin/formAction2.php',
            formdata={'name': name, 'quest': quest, 'color': 'blue'},
            callback=self.parse) for name in names for quest in quests]

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}