from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def scrapeBukaLapak(jumlahHalaman):
    product_list = []
    for page in range(0, jumlahHalaman):
        page = page + 1
        base_url = 'https://www.bukalapak.com/c/perawatan-kecantikan/perawatan-wajah/masker-wajah-wanita?from=navbar_categories&source=navbar&page=' + str(page)
        # print(base_url)

        req = requests.get(base_url)
        soup = BeautifulSoup(req.text, "html.parser")

        produk_kecantikan = soup.find_all('div', class_="product-card")
       
        for item in produk_kecantikan:
            produk = {}
            product_name = item.find("a", {"class":"product__name"})
            produk['nama_produk'] = product_name.text.replace('\n', "").strip()  
            #produk['url']= 'https://www.bukalapak.com' + str(product_name.get('href'))        
            produk['harga']= item.find("span", {"class":"amount"}).text.replace('\n', "").strip()
            # review
            product_review = item.find("a", {"class":"review__aggregate"})
            try:
                product_review = product_review.text
                produk['review'] = int(product_review)
            except:
                produk['review'] = 0


            product_list.append(produk)

    return (product_list)

#download 3 halaman saja
dataset = pd.DataFrame.from_records(scrapeBukaLapak(2))
#simpan di excel
dataset.to_excel("output.xlsx") 