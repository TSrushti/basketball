import pandas
import pandas as pd
import requests
import json


result = requests.get("https://www.balldontlie.io/api/v1/players")
#print(result.text)
#df = pd.read_json("result.json")
#bn=pd.DataFrame(df.features.values.tolist())['id']
#pd.DataFrame.from_records(bn)
result_in_json = result.json()
#print(result_in_json)
df = pandas.json_normalize(result_in_json['data'])
index = False
#print(df)
df.to_csv("./sujant.csv")

df = pd.read_csv("jsonoutput.csv")

df.to_html("test2.htm", index= False)

html_file = df.to_html()