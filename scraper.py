from bs4 import BeautifulSoup
import requests

def CarousellScrape(keyword):
    Cdata = []
    keyword = keyword.replace(" ","%20")
    ## need to make filter for other symbols like ' , !@$_)(*^%$#)
    url = "https://www.carousell.sg/search/" + keyword + "/?sort_by=3";
    page = requests.get(url, timeout=(2, 30)).text
    parse = BeautifulSoup(page, 'lxml')


    products = parse.find_all('div', class_ = 'D_HM D_QX')
    # print(products)
    for product in products:
            product_name  = product.find('p', class_ = 'D_in M_gZ D_gr M_fl D_io M_ha D_ir M_he D_it M_hg D_ix M_hk D_i_ M_hn D_ik').text
            product_price = product.find('p', class_ = 'D_in M_gZ D_gr M_fl D_io M_ha D_ir M_he D_it M_hg D_ix M_hk D_iz M_hm D_ij').text
            product_link = product.find('a', {'class' : 'D_hG M_iC'})['href']
            profile_link = product.find('a', { 'class': 'D_Rk M_acV D_hG M_iC'})['href']
            username = product.find('p', class_ = 'D_in M_gZ D_gt M_fn D_io M_ha D_ir M_he D_it M_hg D_ix M_hk D_i_ M_hn D_ik').text
        # thumbnail = 
            Cprofile = {
            "name": username,
            "profilelink" : profile_link,
            "link": product_link,
            "productname": product_name,
            "productprice": product_price,
            }
            Cdata.append(Cprofile)
    # print(Cdata)
    return Cdata
    
print(CarousellScrape("espresso machine"))


# def AmazonSearch(keyword):
#     url 