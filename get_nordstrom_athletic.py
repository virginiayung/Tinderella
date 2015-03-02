from bs4 import BeautifulSoup
import requests
import re


base_url = 'http://shop.nordstrom.com/c/womens-athletic-shoes-shop?origin=leftnav#category=b6012093'

num_pages = 3




counter = 0
product_dict_name = {}
product_dict_url  = {}

for u in xrange(1,num_pages+1):
# # Category = 'athletic'
    params = { 'page' : u }
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_lst = soup.select('div.fashion-photo')
    product_lst = soup.select('div.info.default.women.adult')

    for image_item in img_lst:
        try:
            image_link = image_item.img['data-original']
            title = image_item.img['alt']

            if image_link.startswith('http'):
                product_id = re.search(r"\_(?P<product_id>\d+)\.", image_link).group("product_id")
                product_dict_name[product_id] = title

                image = requests.get(image_link).content

                counter += 1

                print counter, ',', product_id
                f = open('/Users/heymanhn/Virginia/Zipfian/Capstone_Project/nordstrom/images/athletic_%s.png' % str(product_id)
                         , 'w')
                b = open('/Users/heymanhn/Virginia/Zipfian/Capstone_Project/nordstrom/text/ProductNames_athletic.txt','w')
        
                f.write(image)
                b.write(str(product_dict_name))
        except:
            pass

    for product_item in product_lst:
        try: 
            product_id = re.search(r"\/(?P<product_id>\d+)\?", product_item.a['href']).group("product_id")
            product_link = product_item.a['href']
            product_dict_url [product_id] = product_link

            if product_link.startswith('http'):
                product_dict_url [product_id] = product_link

                w = open('/Users/heymanhn/Virginia/Zipfian/Capstone_Project/nordstrom/text/ProductURL_athletic.txt', 'w')
                w.write(str(product_dict_url))
        except:
            pass




# test = 'http://www.barneys.com/tabitha-simmons-jenny-wedge-espadrilles-503694705.html'
# re.search(r"\-(?P<product_id>\d+)\.", test).group("product_id")

# ''
# test = 'http://product-images.barneys.com/is/image/Barneys/503741202_1_shoeside?$grid_flexH$'
# re.search(r"\/(?P<product_id>\d+)\_(\d+)", test).group("product_id")
