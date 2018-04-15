import requests,time
trn_no = input("Enter train no :")
api_key="4w8qgwoihj" #fromrailway api dot com
x= str(input("Enter date of journey"))
a=time.localtime()
date = x +"-" + str(a[1]) + "-" + str(a[0])
print(date)
def live_status():
    url= "https://api.railwayapi.com/v2/live/train/" + trn_no + "/date/" +date + "/apikey/" +api_key +"/"
    get_status = requests.get(url).json()
    curr_loc=get_status["position"]
    name = get_status["train"]
    print("You queried for Train: ", name["name"], " Train No: ", name["number"])
    print(curr_loc)
   # print(get_status.text)



    #print(get_status)12
live_status()
