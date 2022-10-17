import json

import requests
import re
import sys
from bs4 import BeautifulSoup
# This is a sample Python script.


def product_url():
    url="https://www.sg-electronics.com/searchresult/loadcompanypage"

    headers={'authority':'www.sg-electronics.com',
             'method':'POST',
             'path':'/searchresult/loadcompanypage',
             'scheme':'https',
             'accept-encoding':'gzip, deflate, br',
             'accept-language':'en-US,en;q=0.9',
             'content-length':'45',
             'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
             'cookie':'ASP.NET_SessionId=mq5tcspb33qc2gtxdlvuye0f; MCBIHomePopup=yes; MCBI_Cookie=462fb602-0b87-479b-ae55-e6eea2fae892; sf-prs-ss=638010925349550000; sf-prs-lu=https://www.sg-electronics.com/',
             'origin':'https://www.sg-electronics.com',
             'referer':'https://www.sg-electronics.com/search?t=PS&q=electronic%20company',
             'sec-fetch-dest':'empty',
             'sec-fetch-mode':'cors',
             'sec-fetch-site':'same-origin',
             'sec-gpc':'1',
             'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
             'x-requested-with':'XMLHttpRequest'}

    payload = [{'query':'electronic company','Type':'PS','PageNumber':'1'},{'query': 'electronic company', 'Type': 'PS', 'PageNumber': '2'},{'query': 'electronic company', 'Type': 'PS', 'PageNumber': '3'}]

    for p in payload:
        print(p)
        data=requests.post(url,headers=headers,data=p).text
        output=json.loads(data)
        # print(output)

        for o in output['CompanyResultItems']:
            print(o['LinkCompany'])

def Crawl():

    myList = ["/companies/interflux-singapore-pte-ltd","/companies/sm-system-control-pte-ltd","/companies/spm-refinery-pte-ltd","/companies/pca-technology-limited",
    "/companies/esel-pte-ltd",
    "/companies/dniv-international-pte-ltd",
    "/companies/megachem-limited",
    "/companies/tes-amm(singapore)-pte-ltd",
    "/companies/micro-aire-care-pte-ltd",
    "/companies/ltc-precision-pte-ltd",
    "/companies/mitsubishi-electric-asia-pte-ltd",
    "/companies/island-optical-systems-(s)-pte-ltd",
    "/companies/d-mark-technologies-(s)-pte-ltd",
    "/companies/globalink-electronics-(s)-pte-ltd",
    "/companies/mccoy-pte-ltd",
    "/companies/tassin-industrial-pte-ltd",
    "/companies/mapletree-industrial-trust",
    "/companies/seah-yong-heng-trading-pte-ltd",
    "/companies/capitaland-limited",
    "/companies/air-liquide-singapore-private-limited",
    "/companies/ppt-vision-(s)-pte-ltd",
    "/companies/alex-corporation-(s)-pte-ltd",
    "/companies/marian-asia-pte-ltd",
    "/companies/mieux-pte-ltd",
    "/companies/vigor-precision-engineering-pte-ltd",
    "/companies/add-plus-electronic-pte-ltd",
    "/companies/iso-dynamique-microsystems-pte-ltd",
    "/companies/reddot-production-pte-ltd",
    "/companies/rokko-holdings-ltd",
    "/companies/asmpt-smt-singapore-pte-ltd-"]

    for l in myList:
        main_url= 'https://www.sg-electronics.com/' + l
        data = requests.get(main_url).content
        soup=BeautifulSoup(data)

        Comp_name=soup.find('div',{'class':'col-md-9 company-details'}).find('h3')
        print(Comp_name)

        crn = soup.find('p', {'class': 'company-reg'})
        print(crn)

        address = soup.find('div', {'class': 'col-md-7 company-contact'})
        print(address)

        phone = soup.find('div', {'class': 'valuephone'})
        print(phone)

        website = soup.find('div', {'class': 'valuewebsite'})
        print(website)

        description = soup.find('div', {'class': 'company-description'})
        print(website)


















# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # product_url()
    Crawl()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
