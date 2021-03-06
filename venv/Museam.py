import requests
import pandas as pd
import json
import csv

result = requests.get(url="https://collectionapi.metmuseum.org/public/collection/v1/objects")
var = result.json()

arr = []

for i in var['objectIDs'][:100]:
    detail = requests.get(url="https://collectionapi.metmuseum.org/public/collection/v1/objects/{}".format(i))
    objects = detail.json()
    arr.append(objects)
    # print(type(objects))

# print(len(arr))

df = pd.DataFrame(arr)
# df.head()

mod_df = df.loc[:, ['additionalImages', 'constituents', 'measurements', 'tags']]
for i in mod_df.columns:
    mod_df = mod_df.explode(i)
print(mod_df)

flat_dct = pd.json_normalize(json.loads(mod_df.to_json(orient="records")))
# print(flat_dct.head())

df1 = pd.concat([df, flat_dct], axis = 1)

df1 = df1.drop(['additionalImages', 'constituents', 'measurements', 'tags'], axis = 1)

df1.to_csv('museum.csv', index = False)