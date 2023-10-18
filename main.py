import time
from selenium import webdriver
import json
import requests
import lxml.html
import pyperclip
import base64


afiedolsun = """

              __   _              _      ____    _                       
     /\      / _| (_)            | |    / __ \  | |                      
    /  \    | |_   _    ___    __| |   | |  | | | |  ___   _   _   _ __  
   / /\ \   |  _| | |  / _ \  / _` |   | |  | | | | / __| | | | | | '_ \ 
  / ____ \  | |   | | |  __/ | (_| |   | |__| | | | \__ \ | |_| | | | | |
 /_/    \_\ |_|   |_|  \___|  \__,_|    \____/  |_| |___/  \__,_| |_| |_|
                                                                         
                                                                         

"""
print(afiedolsun)

kopyalanan_metin = pyperclip.paste()
print(kopyalanan_metin)


cookies = None
token = None
decoded = None
link = None
def token_gir():
    global token
    global decoded
    global link

    if "=" in kopyalanan_metin:
        decoded = str(base64.standard_b64decode(kopyalanan_metin).decode("utf-8"))
        link = decoded
        print("token bulundu")
    else:
        print("panoda bulunamadı")
        token = input("Token giriniz: ")
        link = str(base64.standard_b64decode(token).decode("utf-8"))



def linkten_cookie_al():
    global cookies
    response = requests.get(link)
    time.sleep(1)
    tree = lxml.html.fromstring(response.text)
    link_icerigi = tree.xpath('//*[@id="txt-doc"]/text()')[0]
    cookies = json.loads(link_icerigi)
    print(cookies)


def token_import():
    user_agent_string = "user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument(f'--user-agent = {user_agent_string}')
    driver = webdriver.Chrome(options=options)
    #ayarlar falanlar
    driver.get("https://www.migros.com.tr")
    print("driver.get çalıştı")
    time.sleep(3)
    for i in cookies:
        i.pop("sameSite")
        driver.add_cookie(i)
    print("cookie eklendi")
    time.sleep(3)
    driver.refresh()
    time.sleep(3600)

token_gir()
linkten_cookie_al()
token_import()