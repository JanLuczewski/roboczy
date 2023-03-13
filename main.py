from BLProductModel import BLProductModel
from MGR_model import MGRProductModel
import requests
import json
import time

url = "https://api.baselinker.com/connector.php?=&"
payload={'method': 'getProductsList',
'parameters': '{"storage_id": "bl_1"}'}
files=[

]
headers = {
  'X-BLToken': '3012841-3039270-DDUCR3T8WLBL7WPWB49QGMN2PHABRHNZC1NOD5SAJIBQZI6R3UQR3I8M7AHL0WR8'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
data = json.loads(response.text)

product_list = []
for product in data['products']:
  product_list.append(product['product_id'])
# print(product_list)

"""second request that takes each id from product_list and returns datasheet for each product"""
pars = json.dumps({'storage_id': 'bl_1', 'products': product_list})
url_2 = "https://api.baselinker.com/connector.php"
payload_2 = {'method': 'getProductsData',
           "parameters": pars,
             }
files_2 = [

]
headers_2 = {
  'X-BLToken': '3012841-3039270-DDUCR3T8WLBL7WPWB49QGMN2PHABRHNZC1NOD5SAJIBQZI6R3UQR3I8M7AHL0WR8'
}

response_2 = requests.request("POST", url_2, headers=headers_2, data=payload_2, files=files_2)
data_2 = json.loads(response_2.text)
BLProductModel_list= []
# print(data_2['products'])
for pds, prod_data in data_2['products'].items():
  BLProductModel_list.append(BLProductModel(prod_data['product_id'],
                                       prod_data['name'],
                                       prod_data['ean'],
                                       prod_data['sku'],
                                       prod_data['tax_rate'],
                                       prod_data['description'],
                                       prod_data['quantity'],
                                       prod_data['price_brutto'],
                                       ))

# MGR_list = []
# for i in BLProductModel_list:
#     MGR_list.append(MGRProductModel("empty",
#                                     i.name,
#                                     i.ean,
#                                     i.sku,
#                                     i.tax_rate,
#                                     i.description,
#                                     i.quantity,
#                                     i.price_brutto))



def double(obiekt_bl):
    return MGRProductModel("empty",
                           obiekt_bl.name,
                           obiekt_bl.ean,
                           obiekt_bl.sku,
                           obiekt_bl.tax_rate,
                           obiekt_bl.description,
                           obiekt_bl.quantity,
                           obiekt_bl.price_brutto)


obiekty_bl = BLProductModel_list

mgr_list = list(map(double, obiekty_bl))
for mgr in mgr_list:
    url = "https://api.mygadgetrepairs.com/v1//products"
    payload = json.dumps({
        "type": "product",
        "name": mgr.name,
        "condition": "New",
        "code": mgr.code,
        "imei": mgr.imei,
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
        "offerPrice": mgr.offerPrice,
        "tax": mgr.tax,
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
        "description": mgr.description,
        "stockQuantity": mgr.stockQuantity,
        "stock_cog_per_item": 0
    })
    headers = {
        'Authorization': 'r5r|H4!C.%m3D|BzG*Nm1IOII^62ccLFi|&ve=228nxt',
        'Content-Type': 'application/json',
        'Cookie': 'SERVERID=s4'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
"""
Poniższy for loop działa i został wykomentowany tylko tymczasowo na potrzebe dalszej pracy
"""
# counter = 0
# for mgr in mgr_list:
#     result = counter % 30
#     print(f"wynik {result}")
#     if counter % 30 == 0 and counter != 0:
#         print(f"counter = {counter} więc czekam")
#         time.sleep(60)
#         url = "https://api.mygadgetrepairs.com/v1//products"
#         payload = json.dumps({
#             "type": "product",
#             "name": mgr.name,
#             "condition": "New",
#             "code": mgr.code,
#             "imei": mgr.imei,
#             "category": "",
#             "model": "0.1",
#             "additionalModels": "",
#             "status": "Active",
#             "oneTimeUse": True,
#             "inventoryControl": True,
#             "TaxIncludedInCost": True,
#             "cost": 100,
#             "TaxIncludedInPrice": True,
#             "price": 80,
#             "enableOfferPrice": True,
#             "offerStart": "",
#             "offerEnd": "",
#             "TaxIncludedInOfferPrice": True,
#             "offerPrice": mgr.offerPrice,
#             "tax": mgr.tax,
#             "alertQuantity": "",
#             "discountable": True,
#             "supplier": "",
#             "reorderQuantity": 0,
#             "supplierItemCode": "",
#             "emailToSupplier": True,
#             "physicalLocation": "",
#             "warranty": "",
#             "serialisedStock": True,
#             "maintenancePlan": True,
#             "planDuration": 0,
#             "serviceSchedule": 0,
#             "description": mgr.description,
#             "stockQuantity": mgr.stockQuantity,
#             "stock_cog_per_item": 0
#         })
#         headers = {
#             'Authorization': 'r5r|H4!C.%m3D|BzG*Nm1IOII^62ccLFi|&ve=228nxt',
#             'Content-Type': 'application/json',
#             'Cookie': 'SERVERID=s4'
#         }
#         response = requests.request("POST", url, headers=headers, data=payload)
#         counter += 1
#         print(response.text)
#         # print(f"lece dalej {counter}")
#     else:
#         url = "https://api.mygadgetrepairs.com/v1//products"
#         payload = json.dumps({
#             "type": "product",
#             "name": mgr.name,
#             "condition": "New",
#             "code": mgr.code,
#             "imei": mgr.imei,
#             "category": "",
#             "model": "0.1",
#             "additionalModels": "",
#             "status": "Active",
#             "oneTimeUse": True,
#             "inventoryControl": True,
#             "TaxIncludedInCost": True,
#             "cost": 100,
#             "TaxIncludedInPrice": True,
#             "price": 80,
#             "enableOfferPrice": True,
#             "offerStart": "",
#             "offerEnd": "",
#             "TaxIncludedInOfferPrice": True,
#             "offerPrice": mgr.offerPrice,
#             "tax": mgr.tax,
#             "alertQuantity": "",
#             "discountable": True,
#             "supplier": "",
#             "reorderQuantity": 0,
#             "supplierItemCode": "",
#             "emailToSupplier": True,
#             "physicalLocation": "",
#             "warranty": "",
#             "serialisedStock": True,
#             "maintenancePlan": True,
#             "planDuration": 0,
#             "serviceSchedule": 0,
#             "description": mgr.description,
#             "stockQuantity": mgr.stockQuantity,
#             "stock_cog_per_item": 0
#         })
#         headers = {
#             'Authorization': 'r5r|H4!C.%m3D|BzG*Nm1IOII^62ccLFi|&ve=228nxt',
#             'Content-Type': 'application/json',
#             'Cookie': 'SERVERID=s4'
#         }
#         response = requests.request("POST", url, headers=headers, data=payload)
#         counter += 1
#         print(response.text)
# print('finisz')

