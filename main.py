import json

import requests
import re
import sys
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
    payload={'query':'electronic company','Type':'PS','PageNumber':'1'}

    data=requests.post(url,headers=headers,data=payload).text


    output=json.loads(data)
    # print(output)

    for o in output['CompanyResultItems']:
        print(o['LinkCompany'])





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    product_url()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
