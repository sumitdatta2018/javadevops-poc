import requests
from requests.exceptions import HTTPError
try:
    import json
except ImportError:
    import simplejson as json
try:
    response = requests.get('http://sumit-pwc.eastus.cloudapp.azure.com:8081/api/test')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)
    print(jsonResponse['result'])

    servers  = jsonResponse['result']
    f = open("hostnew", "w")
    for server in servers:
      ip  = server['resourceId']
      print ip
      f.write(ip +'\n')
except HTTPError as http_err:
    print('HTTP error occurred: {http_err}')
except Exception as err:
    print('Other error occurred: {err}')
finally:
    f.close()
