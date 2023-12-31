# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook
from pymongo import MongoClient

#we can clean,convert,formate the data.
class BookscraperPipeline:
    def open_spider(self, spider):
        self.workbook=Workbook()
        self.sheet=self.workbook.active
        self.sheet.title='bookspider'
        self.sheet.append(spider.cols)

        # self.client=MongoClient(
        #     host="mongodb+srv://sonya_deanova:88888888@bookspider.bhiq57r.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp",
        #     connect=False
        # )
        # self.collection=self.client.get_database("bookspider").get_collection("books_data")

    def process_item(self, item, spider):
        adapter= ItemAdapter(item)
        # # removing the white space from the string
        # field_names = adapter.field_names()
        # for field_name in field_names:
        #     if field_name != 'description':
        #         value= adapter.get(field_name)
        #         adapter[field_name] = value[0].strip()
        #
        # ## Category & Product Type --> switch to lowercase
        # lowercase_keys = ['category', 'product_type']
        # for lowercase_key in lowercase_keys:
        #     value = adapter.get(lowercase_key)
        #     adapter[lowercase_key] = value.lower()
        #
        # ## Price --> convert to float
        # price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        # for price_key in price_keys:
        #     value = adapter.get(price_key) #getting the values
        #     value = value.replace('£', '') #symbols removing  ".replace"
        #     adapter[price_key] = float(value) #convert it to float using adapter
        #
        # ## Availability --> extract number of books in stock
        # availability_string = adapter.get('availability') #getting the string of avai field
        # split_string_array = availability_string.split('(') #split from "("
        # if len(split_string_array) < 2:
        #     adapter['availability'] = 0
        # else:
        #     availability_array = split_string_array[1].split(' ')
        #     adapter['availability'] = int(availability_array[0])
        #
        # ## Reviews --> convert string to number
        # num_reviews_string = adapter.get('num_reviews')
        # adapter['num_reviews'] = int(num_reviews_string)
        #
        # ## Stars --> convert text to number
        # stars_string = adapter.get('stars')
        # split_stars_array = stars_string.split(' ')
        # stars_text_value = split_stars_array[1].lower()
        #
        # if stars_text_value == "zero":
        #     adapter['stars'] = 0
        # elif stars_text_value == "one":
        #     adapter['stars'] = 1
        # elif stars_text_value == "two":
        #     adapter['stars'] = 2
        # elif stars_text_value == "three":
        #     adapter['stars'] = 3
        # elif stars_text_value == "four":
        #     adapter['stars'] = 4
        # elif stars_text_value == "five":
        #     adapter['stars'] = 5

        self.sheet.append([
            item['url'],
            item['title'],
            item['upc'],
            item['product_type'],
            item['price_excl_tax'],
            item['price_incl_tax'],
            item['tax'],
            item['availability'],
            item['num_reviews'],
            item['stars'],
            item['category'],
            item['description'],
            item['price']
        ])

        #adding dictionary-stored data into MongoDB
        # self.collection.insert_one({
        #     'url': item['url'],
        #     'title' :item['title'],
        #     'upc':item['upc'],
        #     'product_type':item['product_type'],
        #     'price_excl_tax':item['price_excl_tax'],
        #     'price_excl_tax':item['price_excl_tax'],
        #     'tax':item['tax'],
        #     'availability':item['availability'],
        #     'availability':item['availability'],
        #     'stars':item['stars'],
        #     'category':item['category'],
        #     'description':item['description'],
        #     'price':item['price']}
        # )

        # #adding data into Mongodb database
        # self.collection.insert_one(
        #     ItemAdapter(item).asdict()
        # )
        # return item


    def close_spider(self, spider):
        self.workbook.save('bookspider.xlsx')
