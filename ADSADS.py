# burda biseyler karalıyorum
import base64
import pyperclip
link = str(input("linki giriniz:"))


token = base64.standard_b64encode(bytes(f'{link}', 'utf-8'))
utftoken = str(token, 'utf-8')
print(utftoken)
pyperclip.copy(utftoken)


