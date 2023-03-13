from BLProductModel import BLProductModel
from MGR_model import MGRProductModel
import requests
import json
"""
The above code is used to get a list of products from the Baselinker API and transform them into the MGR Product Model. 
It begins with the get_BLlist() function which calls the Baselinker API and retrieves a list of products. 
This list is then passed to the get_product_sheet() function which retrieves the product data for each of the products 
in the list and stores them in a BLProductModel list. Finally, the transform_to_MGR() function is used to transform the 
BLProductModel list into an MGRProductModel list. Finally, the mgr_make_id() function makes a POST request to the
MGR API to create the product in the MGR system.
"""
def get_BLlist():
    """ request for list of products IDs from Baselinker API """
    url = "https://api.baselinker.com/connector.php?=&"
    payload = {'method': 'getProductsList',
               'parameters': '{"storage_id": "bl_1"}'}
    files = []
    headers = {
        'X-BLToken': '3012841-3039270-DDUCR3T8WLBL7WPWB49QGMN2PHABRHNZC1NOD5SAJIBQZI6R3UQR3I8M7AHL0WR8'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    data = json.loads(response.text)
    product_list = []
    for product in data['products']:
        product_list.append(product['product_id'])
    def get_product_sheet():
        """ request for product data for each ID  from Baselinker API """
        pars = json.dumps({'storage_id': 'bl_1', 'products': product_list})
        url_connector = "https://api.baselinker.com/connector.php"
        payload_connector = {'method': 'getProductsData',
                                "parameters": pars,
                                }
        files_connector = []
        headers_connector = {
            'X-BLToken': '3012841-3039270-DDUCR3T8WLBL7WPWB49QGMN2PHABRHNZC1NOD5SAJIBQZI6R3UQR3I8M7AHL0WR8'
        }
        response_connector = requests.request("POST", url_connector, headers=headers_connector, data=payload_connector)
        data_connector = json.loads(response_connector.text)
        BLProductModel_list = []
        for pds, prod_data in data_connector['products'].items():
            BLProductModel_list.append(BLProductModel(prod_data['product_id'],
                                                      prod_data['name'],
                                                      prod_data['ean'],
                                                      prod_data['sku'],
                                                      prod_data['tax_rate'],
                                                      prod_data['description'],
                                                      prod_data['quantity'],
                                                      prod_data['price_brutto'],
                                                      ))
        return BLProductModel_list
    def transform_to_MGR():
        """ transform BLProductModel list into MGRProductModel list """
        MGR_list = []
        for i in get_product_sheet():
            MGR_list.append(MGRProductModel("empty",
                                            i.name,
                                            i.ean,
                                            i.sku,
                                            i.tax_rate,
                                            i.description,
                                            i.quantity,
                                            i.price_brutto,
                                            ))
        return MGR_list
    def mgr_make_id():
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
            return collect_id

    return mgr_make_id()





if __name__ == '__main__':
    print(get_BLlist())



# TODO: lista produktów mgr wzbogacona o ID (które wczesniej miało wartość "empty")
#   1) aby to zrobić musze stworzyć nowe produkty w Baselinker
# TODO: stworzyć nową kolekcje w database appwrite
# TODO: POSTowanie list do appwrite