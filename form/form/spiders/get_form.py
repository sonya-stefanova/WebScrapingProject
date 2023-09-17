import scrapy

def generate_start_urls():
    names = ['Sonya', 'Plamen', 'Mihaela']
    quests = ['to go on vacation', 'to win the game', 'to go to school']
    return ['http://pythonscraping.com/linkedin/formAction.php?name={}&quest={}&color=green'.format(name, quest.replace(' ', '%20')) for name in names for quest in quests]
    return quests


class GetFormSpider(scrapy.Spider):
    name = 'get_form'
    allowed_domains = ['pythonscraping.com']
    start_urls = generate_start_urls()

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}