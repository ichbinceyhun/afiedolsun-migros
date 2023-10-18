# burda biseyler karalıyorum
import base64
token = input("token giriniz:")


decoded = str(base64.standard_b64decode(token).decode("utf-8"))
print(decoded)
