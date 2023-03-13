class BLProductModel:
    def __init__(self,product_id ,name ,ean ,sku ,tax_rate ,description ,quantity ,price_brutto):
        self.product_id = product_id
        self.name = name
        self.ean = ean
        self.sku = sku
        self.tax_rate = tax_rate
        self.description = description
        self.quantity = quantity
        self.price_brutto = price_brutto
