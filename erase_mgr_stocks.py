import requests
import json

def get_ids():
    url = "https://api.mygadgetrepairs.com/v1/stockCount"
    payload={}
    headers = {
      'Authorization': 'r5r|H4!C.%m3D|BzG*Nm1IOII^62ccLFi|&ve=228nxt',
      'Cookie': 'SERVERID=s1'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    print(data)
    ids = []
    json_data = json.loads(data)
    for i in json_data:
        ids.append(i['id'])
    return ids

def delete_stock():
    

