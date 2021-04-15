import urllib.request
import json
from pprint import pprint
import datetime
import csv

#variables 


# apiKey = "5601dff4-135d-48bb-884e-c8e1c0b15e1f
apiKey = "79f83d1f-f210-4c8f-81e7-2421f5ea63ed"

date = datetime.datetime(2006, 9, 26,)

print(date)


for i in range(5000):

    date += datetime.timedelta(days=1)
    dateBuilt = str(str(date.year) + "-" + str(date.month) + "-" + str(date.day))
    url = str("http://content.guardianapis.com/search?from-date=" + dateBuilt + "&to-date=" + dateBuilt + "&page-size=25&api-key=" + apiKey)
    print(url)
    if (dateBuilt == "8-8-2008"):
        break
# url = "http://content.guardianapis.com/search?from-date=2000-01-01&to-date=2000-01-01&page-size=25&api-key=5601dff4-135d-48bb-884e-c8e1c0b15e1f"

    dateBuiltSlash = str(str(date.year) + "/" + str(date.month) + "/" + str(date.day))
    output = str(dateBuiltSlash)
    try:
        # Convert from bytes to text
        resp_text = urllib.request.urlopen(url).read().decode('UTF-8')
    # Use loads to decode from text
        json_obj = json.loads(resp_text)


        index = 0
        while (index < 25):
            try:
                output = output + "\t" + (json_obj["response"]["results"][index]["webTitle"])
                index = index +1
            except:
                print("ERROR")
                index = index + 1
        output = output + "\n"
        print(output)

        with open("output.txt", "a") as myfile:
            myfile.write(output)


    except:

        with open("output.txt", "a") as myfile:
            myfile.write(dateBuilt)


# # date_ = datetime.datetime(2001,8,1,12,4,5)
#
# #Get Http request
# k = urllib.request.urlopen(url).read()
# #print(k)
# i
# json.dump(k)
#
# data = json.load(k)
#
# print(data)

# currentRequest = 0 
# requestLimit = 5000

# while(currentRequest < requestLimit):
# # incremeting date time for the file 






#