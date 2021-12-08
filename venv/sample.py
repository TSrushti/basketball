import pandas.io.json
import requests
import pandas as pd
import json
import csv

result = requests.get(url="https://collectionapi.metmuseum.org/public/collection/v1/objects")
#var = result.json()
#print(result.text)
result_in_json = result.json()
#print(result_in_json)
df = pandas.json_normalize(result_in_json['data'])
#print(df)
df.to_csv("./museumapi1.csv", index = False)
