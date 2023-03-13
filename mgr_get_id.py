from BLProductModel import BLProductModel
from MGR_model import MGRProductModel
import requests
import json

def get_mgrID():
    url = "https://api.mygadgetrepairs.com/v1//products"
    payload = json.dumps({
      "type": "product",
      "name": "test_jan_3",
      "condition": "New",
      "code": "121314567829",
      "model": "655954",
      "status": "Active",
      "cost": 100,
      "price": 80,
      "tax": 34513
    })
    headers = {
      'Authorization': 'r5r|H4!C.%m3D|BzG*Nm1IOII^62ccLFi|&ve=228nxt',
      'Content-Type': 'application/json',
      'Cookie': 'SERVERID=s2'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    ID_response = json.loads(response.text)
    print(ID_response['id'])
    collect_id = []
    collect_id.append(ID_response['id'])
    print(f"collect_id: {collect_id}")
    ID = ID_response['id']
    def delete_ID():
        url = "https://api.mygadgetrepairs.com/v1//products/{product_Id}"
        payload = json.dumps({
            "productId": ID
        })
        headers = {
            'Authorization': 'r5r|H4!C.%m3D|BzG*Nm1IOII^62ccLFi|&ve=228nxt',
            'Content-Type': 'application/json',
            'Cookie': 'SERVERID=s2'
        }

        response_1 = requests.request("DELETE", url, headers=headers, data=payload)
        print(response_1.text)
        print(response_1.status_code)
    return delete_ID()
if __name__ == '__main__':
    get_mgrID()