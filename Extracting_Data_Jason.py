#Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://python-data.dr-chuck.net/comments_353540.json (Sum ends with 71)

import json
import urllib

count = 0
sum = 0
url = raw_input("Enter Url - ")

data = urllib.urlopen(url).read()

print data

info = json.loads(str(data))

for i in info['comments']:
    count = count+1
    sum = sum + i['count']
print "Sum : ",sum   
print "count : ",count
