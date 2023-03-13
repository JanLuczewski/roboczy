import requests
import json
import random
from BLProductModel import BLProductModel
from MGR_model import MGRProductModel


items = ["but","skarpety","spodnie","pasek","koszulka","bluza","kurtka","szalik","czapka"]
def generate_bls():
    """ randomly generates BLProducts , sends POST request to BL API, returns list of new IDs"""
    objects = []
    for i in items:
        objects.append(BLProductModel("empty",
                                      i,
                                      random.randint(1,10000000),
                                      random.randint(1,10000000),
                                      23,
                                      f"to jest opis produktu {i}",
                                      random.randint(1,100),
                                      random.randint(1,1000),
                                      ))
    return objects
def post_bl(objects):
    url = "https://api.baselinker.com/connector.php"
    new_ids = []
    for object in objects:
        pars = json.dumps({
            "storage_id": "bl_1",
            "ean": object.ean,
            "sku": object.sku,
            "name": object.name,
            "quantity": object.quantity,
            "price_brutto": object.price_brutto,
            "tax_rate": object.tax_rate,
            "description": object.description,
        })
        payload = {'method': 'addProduct',
                   'parameters': pars}
        files = []
        headers = {
            'X-BLToken': '3012841-3039270-DDUCR3T8WLBL7WPWB49QGMN2PHABRHNZC1NOD5SAJIBQZI6R3UQR3I8M7AHL0WR8'
        }
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        response_data = json.loads(response.text)
        new_id = response_data['product_id']
        new_ids.append(new_id)
    return new_ids
def summary():
    objects = generate_bls()
    new_ids = post_bl(objects)
    for i in objects:
        n = objects.index(i)
        i.product_id = new_ids[n]
    return objects
def transform_to_MGR():
    """ transform BLProductModel list into MGRProductModel list """
    MGR_list = []
    for i in summary():
        MGR_list.append(MGRProductModel("empty",
                                        i.name,
                                        i.ean,
                                        i.sku,
                                        i.tax_rate,
                                        i.description,
                                        i.quantity,
                                        i.price_brutto,
                                        ))
    for o in MGR_list:
        print(o.__dict__)
    return MGR_list

def post_MGR():
    """ make a POST request to the MGR API to create the product in the MGR system,
            in return we get the ID of the created product"""
    url_id = "https://api.mygadgetrepairs.com/v1//products"
    headers_id = {
        'Authorization': 'r5r|H4!C.%m3D|BzG*Nm1IOII^62ccLFi|&ve=228nxt',
        'Content-Type': 'application/json',
        'Cookie': 'SERVERID=s4'
    }
    collect_id = []
    for instance in transform_to_MGR():
        payload_id = json.dumps({
            "type": "product",
            "name": instance.name,
            "condition": "New",
            "code": instance.code,
            "imei": instance.imei,
            "category": "",
            "model": "0.1",
            "additionalModels": "",
            "status": "Active",
            "oneTimeUse": True,
            "inventoryControl": True,
            "TaxIncludedInCost": True,
            "cost": 100,
            "TaxIncludedInPrice": True,
            "price": 80,
            "enableOfferPrice": True,
            "offerStart": "",
            "offerEnd": "",
            "TaxIncludedInOfferPrice": True,
            "offerPrice": instance.offerPrice,
            "tax": instance.tax,
            "alertQuantity": "",
            "discountable": True,
            "supplier": "",
            "reorderQuantity": 0,
            "supplierItemCode": "",
            "emailToSupplier": True,
            "physicalLocation": "",
            "warranty": "",
            "serialisedStock": True,
            "maintenancePlan": True,
            "planDuration": 0,
            "serviceSchedule": 0,
            "description": instance.description,
            "stockQuantity": instance.stockQuantity,
            "stock_cog_per_item": 0
        })
        response_id = requests.request("POST", url_id, headers=headers_id, data=payload_id)
        print(response_id.text)
        id_data = json.loads(response_id.text)
        collect_id.append(id_data['id'])
        print("sukces")
        print(collect_id)
        return collect_id




if __name__ == "__main__":
    post_MGR()


    
# TODO: pociągnąć je dalej do deploymentu na MGR
#  1) wyłapać ID nadane przy POSTowaniu, wrzucić w liste
#  2) obiekty z list generate_bls.objects
#  3) przerobić BL na MGR
#  4) zaPOSTować na MGR
#  5) wyłapać ID nadane przy POSTowaniu, wrzucić w liste
#  6) uzupełnić obiekt MGR o nowonadany ID