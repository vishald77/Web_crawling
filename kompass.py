import json

import requests
import re
import sys
from bs4 import BeautifulSoup
import xlsxwriter
import os,glob
# This is a sample Python script.


def product_url():

    for x in range(0 , 10):
        k=x+1
        url="https://sg.kompass.com/searchCompanies/scroll?tab=cmp&pageNbre=" + str(k)
        page_name='medical equipment and instruments' + str(url.split('pageNbre=')[1])

        headers={'authority':'sg.kompass.com',
                 'method':'GET',
                 'path':'/searchCompanies?acClassif=&localizationCode=SG&localizationLabel=Singapore&localizationType=country&text=medical+equipment+and+instruments&searchType=SUPPLIER',
                 'scheme':'https',
                 'accept-encoding':'gzip, deflate, br',
                 'accept-language':'en-GB,en;q=0.5',
                 'content-length':'45',
                 'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
                 'cookie':'timezoneoffset=-330; route=1666022303.093.173.795420|1ca372b33d2bad9524c20eaf607b64ca; JSESSIONID=0570A6892A9185647BE80E554B9117B9; _k_cty_lang=en_SG; ROUTEID=.; timezoneoffset=-330; axeptio_authorized_vendors=,,; axeptio_cookies={"$$token":"53sasvklj4xjijls53dg","$$date":"2022-10-17T15:59:04.035Z","SnapEngage":false,"Double_Click":false,"facebook_pixel":false,"ShinyStat":false,"$$completed":true}; axeptio_all_vendors=,SnapEngage,Double_Click,facebook_pixel,ShinyStat,; kp_uuid=393f3151-0648-45b0-a83f-73af5fdd9ab4; datadome=mBjGiFZMN0gNhmYLSx3TLxoCQF-ix4mjsV1wxrOtwBt5UUDR4~VZwXx7BZIJWO1_Vr1mE67c7WFiXKqhYnaAhx2KtosX0YlDGob5QND3tg8xchulltj6IZLOaz-e~n2',
                 'origin':'https://www.sg.kompass.com.com',
                 'referer':'https://sg.kompass.com/searchCompanies/scroll?tab=cmp&pageNbre=1',
                 'sec-fetch-dest':'document',
                 'sec-fetch-mode':'navigate',
                 'sec-fetch-site':'same-origin',
                 'sec-gpc':'1',
                 'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                 'x-requested-with':'XMLHttpRequest'}

        payload = {'acClassif':'','localizationCode':'SG','localizationLabel':'Singapore','localizationType':'country','text':'Beauty Products','searchType':'SUPPLIER'}



        proxy = {"http": 'http://47.74.152.29:8888'}

        data=requests.get(url,headers=headers,data=payload,proxies=proxy).content
        Html_file = open("/Users/vishaldiwase/PycharmProjects/Web_crawling/sg_kompass/HTML_pages/" + str(page_name) + ".html",
            "wb")
        Html_file.write(data)
        Html_file.close()
        print("File saved")
        # sys.exit()


def Crawl():
    folder_path='/Users/vishaldiwase/PycharmProjects/Web_crawling/sg_kompass/HTML_pages/'
    for filename in glob.glob(os.path.join(folder_path, '*.html')):
        print(filename)
        file=str(filename.split('HTML_pages/')[1]).replace('.html','')
        print(file)
        # filename='C:\\Users\\visha338\\Desktop\\Manufacturer\\new_project\\sgelectronics\\HTML\\esel_pte_ltd.html'
        with open(filename, 'rb') as f:
            text = f.read()
            soup = BeautifulSoup(text,features="html.parser")
            chunk=soup.find_all('div',{'class':'col col-left company-container'})
            for c in chunk:
                l=re.search(r'<a href="(.*?)"',str(c),re.M|re.I)[1]
                l_name=l.split('/')[2]
                main_url= 'https://sg.kompass.com' + l
                print(main_url)
                headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate, br',

                           'Accept-Language': 'en-US,en;q=0.5',
                           'accept-encoding': 'gzip, deflate, br',
                           'Connection': 'keep-alive',
                           'cookie': 'datadome=QYDfOVWVd0S8A3WDPoW~XAtHTvRS6lalt5HVuXYxdQI-RXKktcQV_zjUsCHsMa.HdrSY.CykiPBPmPzpjQp4T2QKnn34yRAhHWUoMokqd~ycRca62aHUm1Xw5U7erTq; _gcl_au=1.1.406303079.1665079549; kp_uuid=d1f50c66-cb16-4a7d-9e17-93596a64f52c; axeptio_cookies={%22$$token%22:%2258d9amek2hp7leqh54c02w%22%2C%22$$date%22:%222022-10-06T18:05:49.503Z%22%2C%22$$completed%22:false}; axeptio_authorized_vendors=%2C%2C; axeptio_all_vendors=%2C%2C; _ga=GA1.3.2032164895.1665079550; __gads=ID=41e19836448ca43a-22aed38fe3d6003c:T=1665079550:RT=1665079550:S=ALNI_MYGx8gNIvXOL5Td38OEwiBUMJyXdg; __gpi=UID=00000a1dd1dfe827:T=1665079550:RT=1666023022:S=ALNI_MZXKfIrcFViGC9h-2SIo_z4I7V09g; JSESSIONID=EB21D2451C4E217109594C4FBB519101; _k_cty_lang=en_SG; ROUTEID=.; route=1666023020.69.172.252839|1ca372b33d2bad9524c20eaf607b64ca; timezoneoffset=-330; _gid=GA1.3.9794255.1666023021',
                           'Host': 'sg.kompass.com',
                           'Sec-Fetch-Dest': 'document',
                           'Sec-Fetch-Mode': 'navigate',
                           'Sec-Fetch-Site': 'none',
                           'Sec-Fetch-User': '?1',
                           'Upgrade-Insecure-Requests': '1',
                           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
                           }
                proxy = {"http": 'http://118.107.44.181:80'}
                data = requests.get(main_url,proxies=proxy,headers=headers).content
                # print(data)
                Html_file = open('/Users/vishaldiwase/PycharmProjects/Web_crawling/sg_kompass/HTML_pages/company/' + str(file)+ '_' + str(l_name) + ".html", "wb")
                Html_file.write(data)
                Html_file.close()



def parse():
    folder_path='/Users/vishaldiwase/PycharmProjects/Web_crawling/sg_kompass/HTML_pages/company/'
    file_path='/Users/vishaldiwase/PycharmProjects/Web_crawling/sg_kompass/HTML_pages/Untitled.xlsx'
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Comp_name')
    worksheet.write('B1', 'address')
    worksheet.write('C1', 'phone_num')
    worksheet.write('D1', 'website')
    worksheet.write('E1', 'description')
    worksheet.write('F1', 'Search')


    ii = 1
    col = 0
    for filename in glob.glob(os.path.join(folder_path, '*.html')):
        print(filename)
        search=filename.split('/company/')[1].split('_')[0]
        print(search)

        with open(filename, 'rb') as f:
            text = f.read()
            soup = BeautifulSoup(text)

        try:
            Comp_name=soup.find('h1',{'itemprop':'name'}).text.strip().replace('\r','').replace('\n','')
            print(Comp_name)
        except:
            Comp_name=''

        try:
            address = soup.find('span', {'itemprop': 'streetAddress'}).text.strip().replace('\r','').replace('\n','')
            print(address)
        except:
            address=''

        try:
            phone = soup.find('div', {'id': 'companyContact'})
            phone_num=re.search(r'value="\+65(.*?)"',str(phone),re.M|re.I|re.S)[1]
            phone_num='+65' + phone_num
            print(phone_num)
        except:
            phone_num=''

        try:
            website = soup.find('a', {'id': 'webSite_presentation_0'}).text.strip()
            print(website)
        except:
            website=''

        try:
            description = soup.find('div', {'class': 'containerWhite containerWhiteInt containerLazy'}).text.strip().replace('\r','').replace('\n',' ')
            print(description)
        except:
            description=''



        worksheet.write(ii, col, Comp_name)
        worksheet.write(ii, col + 1, address)
        worksheet.write(ii, col + 2, phone_num)
        worksheet.write(ii, col + 3, website)
        worksheet.write(ii, col + 4, description)
        worksheet.write(ii, col + 5, search)

        ii += 1
    workbook.close()
        # sys.exit()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # product_url()
    # Crawl()
    parse()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
