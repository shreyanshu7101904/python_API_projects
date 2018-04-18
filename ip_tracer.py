import requests
import json


print("*"*30)
print("IP LOCATION TRACKER")
print("*"*30)


def tracker(ip_input):
    url = "http://ip-api.com/json/" + ip_input
    content = requests.get(url).json()
    print("Query for IP",content["query"])
    print(json.dumps(content,sort_keys=True,indent=4))


x = str(input("Enter IP adress/Domain name :"))
while x != "c":
    tracker(x)
    x = input("Enter IP Address/Domain name :")