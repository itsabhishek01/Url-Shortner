import http.client
import json
import validators
import sys

conn = http.client.HTTPSConnection("url-shortener-service.p.rapidapi.com")
url=input("Enter The URL: ")
print("\nChecking if you Entered a VAlid URL or not\n")
payload = "url="+url
valid=validators.url(url)
if valid==True:
    print("Url is valid")
else:
    print("Invalid url")
    sys.exit()
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "774785d8a4msh96d8f12a50b622dp166edbjsn8fe0f31e8de6",
    'x-rapidapi-host': "url-shortener-service.p.rapidapi.com"
    }

conn.request("POST", "/shorten", payload, headers)

res = conn.getresponse()
data = res.read()

mydata=json.loads(data.decode("utf-8"))
print("\nYour Shortened URL is: ",mydata["result_url"])
print("\nThanks for Using Our Service")