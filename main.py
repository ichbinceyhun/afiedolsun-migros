import subprocess
import time
try:
    from selenium import webdriver

except ImportError:
    print("Gerekli dosyalar yükleniyor. selenium")
    subprocess.check_call(['pip', 'install', 'selenium'])
import json
try:
    import requests

except ImportError:
    print("Gerekli dosyalar yükleniyor. req")
    subprocess.check_call(['pip', 'install', 'requests'])

try:
    import lxml.html

except ImportError:
    print("Gerekli dosyalar yükleniyor. lxml")
    subprocess.check_call(['pip', 'install', 'lxml'])

import base64
time.sleep(5)



afiedolsun = """

              __   _              _      ____    _                       
     /\      / _| (_)            | |    / __ \  | |                      
    /  \    | |_   _    ___    __| |   | |  | | | |  ___   _   _   _ __  
   / /\ \   |  _| | |  / _ \  / _` |   | |  | | | | / __| | | | | | '_ \ 
  / ____ \  | |   | | |  __/ | (_| |   | |__| | | | \__ \ | |_| | | | | |
 /_/    \_\ |_|   |_|  \___|  \__,_|    \____/  |_| |___/  \__,_| |_| |_|
                                                                         
                                                                         

"""
print(afiedolsun)



cookies = None
token = None
decoded = None
link = None
def token_gir():
    global token
    global decoded
    global link
    token = input("Token giriniz: ")
    try:
        link = str(base64.standard_b64decode(token).decode("utf-8"))
    except:
        print("hatalı token girdiniz")
        token_gir()
    if "textdoc" in link:
        print("TOKENİNİZ ALINDI, HESAP BİRAZDAN YÜKLENECEK")
        pizza = """"

        _....._
    _.:`.--|--.`:._
  .: .'\o  | o /'. '.
 // '.  \ o|  /  o '.\
//'._o'. \ |o/ o_.-'o\\
|| o '-.'.\|/.-' o   ||
||--o--o-->|                                  

        """
        pizza_dilimi = """// ""--.._
||  (_)  _ "-._
||    _ (_)    '-.
||   (_)   __..-'
 \\__..--"""""
        burger = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡤⠶⠶⠚⠛⠛⠻⠿⢷⣶⡶⢾⣿⢿⣿⣷⣶⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠛⠉⠀⡀⠴⣏⡧⠐⠚⢛⡛⠓⠺⣿⣮⡿⠦⢤⡀⠀⠈⣭⠉⠛⠻⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣶⠟⠉⣤⡄⠀⣠⡛⠃⢠⣦⡄⠀⠀⡛⠛⠀⠰⠿⠟⢧⡀⠀⠻⠦⠀⠀⠀⠶⠀⢠⣦⡙⢿⣶⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠋⠑⠀⠀⠉⠀⠐⠟⠁⢀⣤⡉⠀⠀⠸⢿⠂⠀⣶⡦⠀⠘⠇⠀⠀⠰⠆⠀⣠⣤⡀⠀⠉⠀⠀⠙⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⡟⠁⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠉⢁⣤⡀⠀⣀⠀⠀⢀⣠⡀⠀⠀⢰⣶⠀⠀⠀⠈⠉⠀⠀⠀⠼⠏⠀⠈⠻⣦⠀⠀⠀⠀
⠀⠀⢀⣿⠏⡀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠀⠀⣀⡈⠉⠀⠀⠋⠁⠀⠈⠉⠁⠀⠀⠀⠁⠀⠰⠟⠀⠀⠀⠰⠆⠀⠀⠀⠄⠀⠘⢧⠀⠀⠀
⠀⠀⣾⡟⢠⠇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠘⠛⠃⠀⠀⠀⢰⡆⠀⠀⠀⠀⠀⠀⠠⣤⠄⠀⢀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀
⠀⠀⣿⣇⠈⣧⡟⣆⢘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀
⠀⠀⠘⣿⣦⣌⣁⠈⠚⠷⢽⣮⣦⣄⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠀
⠀⢀⣤⠾⢋⠈⠉⠛⠳⠦⣤⣀⡉⠉⠉⠒⠛⠷⢶⡤⠤⠤⠤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠤⠴⠶⢾⣿⣅⠀⠀
⣴⣿⠿⢿⣿⠃⡀⠀⠀⠀⣀⠈⠉⠛⠒⠲⣦⣤⡤⠤⠤⠤⠤⠤⠤⠤⠤⠴⠶⠖⠲⠶⣶⣒⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⢀⣀⣈⣻⣿⣦
⠀⠀⠀⠚⠛⣻⡇⠀⣴⣏⣙⣷⠦⠶⠶⣟⠉⠀⠀⠀⠀⢠⡤⠤⣤⣀⠀⠀⠀⣤⢶⣄⣠⡭⠿⢶⣄⠀⢀⣤⠶⠶⢦⡤⠼⣿⡏⠉⠙⠻
⠀⠀⠀⢠⣴⣿⣷⣶⣿⣤⣉⡙⠛⠒⠒⠛⠛⣿⡄⢀⣤⠾⠤⠤⠖⠛⢷⣤⣼⣿⠶⣭⣄⣀⣀⢀⣸⣾⣋⣀⣀⣤⡤⣶⣿⣿⣅⠀⠀⠀
⠀⠀⠀⢿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⢀⣠⠴⢚⣽⣿⣿⣿⣿⣿⣿⡿⠻⠙⠋⠉⠘⣿⡄⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⣿⣟⣿⣿⣿⡟⢻⣏⣹⢻⣿⢻⣻⣿⣿⣦⠀⣀⣀⡴⠞⣋⣤⣶⡿⣿⠋⠳⣞⢁⡠⠁⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀
⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣖⢻⣿⣿⣿⣿⣿⣻⣿⣿⣿⡿⣧⣭⣵⠖⠋⢩⣽⢁⣀⠻⠀⢤⣤⠿⠤⠖⣦⣷⣂⣠⣴⣾⣟⠃⠀⠀
⠀⠀⠀⣾⡟⢿⣄⣈⣽⡿⠿⠟⠛⠿⣿⣿⣿⣿⣿⣿⣹⣯⣿⣤⣾⣚⣿⣲⣿⣚⣧⣤⣿⣾⣷⣾⣿⣾⣟⣋⡉⠉⠉⣿⠀⠙⣿⡄⠀⠀
⠀⠀⠀⣿⡆⣆⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢷⡄⠀⠉⠉⣉⡽⠛⠋⠙⠛⠿⣤⣤⠴⠟⠋⠁⠀⠀⠀⠀⠀⠈⠉⠛⠒⠛⠀⠀⢹⡇⠀⠀
⠀⠀⠀⢿⣷⢻⣿⣆⢠⡀⠀⡀⠀⠀⠀⠀⠀⠙⠳⠶⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀
⠀⠀⠀⠘⢿⣦⣍⡛⠦⣷⣀⠳⣀⠈⠳⣄⠀⠀⣀⢀⣀⣀⣀⣀⣀⣀⣀⠀⠀⢀⣀⣀⣀⣀⡠⠤⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠙⠛⠻⠷⣶⣶⣾⣽⣷⣦⣤⣀⣈⣉⣉⣁⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⡶⠶⠶⠶⠒⠚⠋⠉⠁⠀⠀⠀⠀⠀"""
        print(pizza)
        time.sleep(0.3)
        print(pizza_dilimi)
        time.sleep(0.3)
        print(burger)




def linkten_cookie_al():
    global cookies
    response = requests.get(link)
    time.sleep(1)
    tree = lxml.html.fromstring(response.text)
    link_icerigi = tree.xpath('//*[@id="txt-doc"]/text()')[0]
    cookies = json.loads(link_icerigi)
    kuki_str = str(cookies)
    if "migros" in kuki_str:
        print("Hesap bulundu")


def token_import():
    user_agent_string = "user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument(f'--user-agent = {user_agent_string}')
    driver = webdriver.Chrome(options=options)
    #ayarlar falanlar
    driver.get("https://www.migros.com.tr")
    print("driver.get çalıştı")
    time.sleep(2)
    for i in cookies:
        i.pop("sameSite")
        driver.add_cookie(i)
    print("cookie eklendi")
    time.sleep(1)
    driver.refresh()
    time.sleep(3600)

token_gir()
linkten_cookie_al()
token_import()