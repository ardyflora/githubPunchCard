from selenium import webdriver
import json
from collections import OrderedDict

driver = webdriver.Chrome()
driver.get("https://github.com/users/ardyflora/contributions")


Data_points = []

#for loop and assuming max 20 commits in a day
for i in range(1,20):
    listElem = driver.find_elements_by_xpath("//*[@data-count="+ str(i)+ "]")
    for elem in listElem:
        Data ={}
        print elem.get_attribute("data-date")
        print elem.get_attribute("data-count")
        Data['data-date'] = str(elem.get_attribute("data-date"))
        Data['data-count'] = str(elem.get_attribute("data-count"))
        Data_points.append(Data)

#DataStructure dataPoints:
# X axis = data-date
# Y axis = data-count
#
#print("Final data set:",Data_points)

from operator import itemgetter
newlist = sorted(Data_points, key=itemgetter('data-date'), reverse=False)
print(newlist)

#Parsing the data into json file to be used by .js script
with open("output.json", "w") as f:
    json.dump(newlist, f)
json.dumps(newlist)


driver.close()
