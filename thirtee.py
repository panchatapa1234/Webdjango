import json
import requests
pincode=input("Enter :")
code=requests.get("https://api.postalpincode.in/pincode/"+pincode)
info=json.loads(code.text)[0]['PostOffice']
print(info)