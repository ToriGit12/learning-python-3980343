# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#

import urllib.request

# Open a URL and get the HTTP result code
# 200 if working, 404 if there is an error
web_url = urllib.request.urlopen("http://www.example.com")
print("Result code:", web_url.getcode())

# Read the entire contents of the provided URL
# Comes out in HTML
data = web_url.read()
print(data)