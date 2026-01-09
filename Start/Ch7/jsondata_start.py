# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import urllib.request 
import json


# Open the URL and read the data
web_url = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
response = web_url.getcode()
if response == 200:
  data = web_url.read()
  # print(f"Data is retrived: {data}")
  
# Read the JSON data from the source
  json_data = json.loads(data)

# Print the content of the 'text' field
  print(json_data['text'])