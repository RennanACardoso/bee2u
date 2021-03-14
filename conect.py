from pymongo import MongoClient
import pymongo
import requests


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["beer2u_leitos"]
leitos = mydb["leitos"]


### carregando bd
#r = requests.get("https://elastic-leitos.saude.gov.br/leito_ocupacao/_search", auth=('user-api-leitos', 'aQbLL3ZStaTr38tj'))
# # x = mycol.insert_many(r)
# #print(x.inserted_ids)
# for i in r.json().get("hits").get('hits'):
#      print(i.get('_source'))
#      x = mycol.insert_one(i.get('_source'))

# for i in leitos.find():
#     print(i['estado'])