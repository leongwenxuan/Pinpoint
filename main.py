from bs4 import BeautifulSoup
import requests

# https://www.carousell.sg/search/espresso/?addRecent=false&canChangeKeyword=false&includeSuggestions=false&sc=0a0208301a0408bbe172220c0a08657370726573736f78013204080378013a02180742060801100118004a0620012801400150015a020801&searchId=Ec8fpn&sort_by=3
# https://www.carousell.sg/ + search / category + word / category id 


# https://www.carousell.sg/search/nespresso/?sort_by=3
# https://www.carousell.sg/ + search + productkeyword + sort type 
# Sort Type: 1 = Best Match ,3 = Recent ,4 = Low to High, 5 = High to Low ,  6 = Nearby
# https://www.carousell.sg/ds/search/cf/4.0/search/?_path=%2Fcf%2F4.0%2Fsearch%2F

data = []
images = []
# class CarousellProfile:
#     def __init__(self, username, link, product_name, product_price):
#         self.username = username
#         self.link = link
#         self.product_name = product_name
#         self.product_price = product_price

url = "https://www.carousell.sg/search/espresso%20machine/?searchId=uWZzGE&sort_by=3";
page = requests.get(url, timeout=(2, 30)).text
parse = BeautifulSoup(page, 'lxml')

products = parse.find_all('div', class_ = 'D_HM D_QX')
for product in products:
    product_name  = product.find('p', class_ = 'D_in M_gZ D_gr M_fl D_io M_ha D_ir M_he D_it M_hg D_ix M_hk D_i_ M_hn D_ik').text
    product_price = product.find('p', class_ = 'D_in M_gZ D_gr M_fl D_io M_ha D_ir M_he D_it M_hg D_ix M_hk D_iz M_hm D_ij').text
    product_link = product.find('a', {'class' : 'D_hG M_iC'})['href']
    profile_link = product.find('a', { 'class': 'D_Rk M_acV D_hG M_iC'})['href']
    username = product.find('p', class_ = 'D_in M_gZ D_gt M_fn D_io M_ha D_ir M_he D_it M_hg D_ix M_hk D_i_ M_hn D_ik').text
    # thumbnail = 



    profile = {
        "name": profile_link,
        "link": product_link,
        "productname": product_name,
        "productprice": product_price,
    }
    data.append(profile)


    # print(product)
    # print(images)
    # print(product_name)
    # print(product_price)
    # print(link)
    # print(user_name)

# print(len(products))
# print(data[5])
# print(image)