import json

from appwrite.client import Client
from appwrite.services.databases import Databases

client = Client()
API_key = "f3a924b20d5eede6bfb91218f25e890dd24ee13e0a50dbf9b36f25708b7ce87210c239b910e4c4f486ca1d72065fcfe6ed0d4b3486bd38b0f167f70f27aeb9eb36b9df83bd6b65099edb653725d3540543fcc9394980bdf318cbef8ebb45d276d8b05a223f46f6009d297c65fdfba76af9bac41636e4010739250de7040f312d"
(client
  .set_endpoint('https://ourbike.fiszu.site/v1') # Your API Endpoint
  .set_project('63eb9a9713c140ba650b') # Your project ID
  .set_key(API_key) # Your secret API key
)

databases = Databases(client)
db_id = "63ee51ced274841bf79d"
col_id = "63ee51e38924df7b46bd"
doc_id = "63f7801bf3d8c4e5f61f"
result = databases.delete_document(db_id, col_id, doc_id)
print(result)
