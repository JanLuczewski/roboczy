"""
file for erasing all MGR products from MGR's database
"""
import json
import requests

def eraser():
    url = "https://api.mygadgetrepairs.com/v1//products/"
    payload={}
    headers = {
      'Authorization': 'r5r|H4!C.%m3D|BzG*Nm1IOII^62ccLFi|&ve=228nxt',
      'Cookie': 'SERVERID=s4'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    ids = []
    for x in data:
        ids.append(x['id'])
    print(ids)
    def delete_ids():
        url = "https://api.mygadgetrepairs.com/v1//products/{product_Id}"
        headers = {
            'Authorization': 'r5r|H4!C.%m3D|BzG*Nm1IOII^62ccLFi|&ve=228nxt',
            'Content-Type': 'application/json',
            'Cookie': 'SERVERID=s2'
        }
        for instance in ids:
            payload = json.dumps({
                "productId": instance
            })
            response = requests.request("DELETE",url, headers=headers, data=payload)
            if response.status_code == 200:
                print(f"Product {instance} deleted successfully")
            else:
                print(response.text)
                print(f"Product {instance} deletion failed")

    return delete_ids()
if __name__ == '__main__':
    eraser()

