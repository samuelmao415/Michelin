from scrapy import Spider,Request
from michelin.items import michelinItem
#import urllib.request


class michelin(Spider):
    name="michelin_spider"
    allowed_urls=["https://guide.michelin.com/us/new-york/restaurants"]
    start_urls=["https://guide.michelin.com/us/new-york/restaurants/page/1?max=30&sort=relevance&order=desc"]
    def parse(self,response):
        result_urls=['https://guide.michelin.com/us/new-york/restaurants/page/{}?max=30&sort=relevance&order=desc'.format(x) for x in range(1,19)]
        for url in result_urls:
            yield Request(url=url, callback=self.parse_clothing_page)
        print("parse"*20)


    def parse_clothing_page(self,response):
        #extract product link from the first pages
        michelinurl="https://guide.michelin.com"
        #list comprehension to concat domain with sublinks
        product = response.xpath('//div[@class="grid-restaurants-new_right_item nested-link"]/a/@href').extract()
        # response.xpath('//span[@class="regular"]').extract()
        # response.xpath('normalize-space(//span[@class="regular"])').extract()
        # ' '.join(s.strip() for s in response.xpath('//span[@class="regular"]')).extract()
        res=[michelinurl+s for s in product]
        for url in res:
            yield Request(url=url, callback=self.parse_item_page)
        print("parse_michelin_page"*20)
#image
# -name
# -product description (all of it)
# -price
# -material description (if any)

    def parse_item_page(self,response):
        #name=response.xpath('.//h1[@itemprop="name"]').extract()
        item=michelinItem()
        # main_image=response.xpath('//li[@class="main-image swiper-slide"]/img/@src').extract()
        # other_images=response.xpath('//li[@class="main-image swiper-slide"]/img/@data-src').extract()
        # #except the main image, the page usually comes with two more images
        # try:
        #     other_image_1=other_images[0]
        #     other_image_2=other_images[1]
        #     item["other_image_1"]=other_image_1
        #     item["other_image_2"]=other_image_2
        # except:
        #     pass
        # prodcut_description=response.xpath('//p[@class="reset-font c-margin-1v"]/text()').extract()
        # material_description=response.xpath('//ul[@data-auto="product-description-bullets"]/li/text()').extract()
        product_name=response.xpath('//h2[@class="content-title"]/text()').extract_first().strip()
        price=response.xpath('//div[@class="restaurant-criteria"]/div[@class="restaurant-criteria__desc"]/text()').extract()[2].strip()
        distinction=response.xpath('//div[@class="restaurant-criteria"]/div[@class="restaurant-criteria__desc"]/text()').extract()[0].strip()
        classification=response.xpath('//div[@class="restaurant-criteria"]/div[@class="restaurant-criteria__desc"]/text()').extract()[1].strip()
        website=response.xpath('//div[@class="location-item__desc"]/a/@href')[1].extract()
        description=response.xpath('//div[@class="restaurant-desc"]/text()').extract_first().strip()
        #download image
        # full_file_name=list("./pics/sm{}.tif".format(x) for x in range(1,100))
        # urllib.request.urlretrieve(main_image,full_file_name)


        #
        # item["main_image"]=main_image
        #
        # item["prodcut_description"]=prodcut_description
        # item["material_description"]=material_description

        item["product_name"]=product_name
        item["price"]=price
        item["distinction"]=distinction
        item["website"]=website
        item["description"]=description
        item["classification"]=classification
        yield item
        print("item"*20)
