# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import urllib.request 
import json

# Open the URL and read the data
web_url = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
print("Result code:", web_url.getcode())

# Read the JSON data from the source
data = web_url.read()
# print(data)

# Print the content of the 'text' field

# This line takes the string of JSON code
# and parses it into a native Python dictionary object
theJSON = json.loads(data) # "load s" means "load string"

# Now access the data within the object
print(theJSON["text"]) # access dictionary value with key