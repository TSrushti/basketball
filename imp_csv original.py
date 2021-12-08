import pandas
import pandas as pd
import requests
import json
import numpy as np

result = requests.get("https://www.balldontlie.io/api/v1/players")
#print(result.text)
#df = pd.read_json("result.json")
#bn=pd.DataFrame(df.features.values.tolist())['id']
#pd.DataFrame.from_records(bn)
result_in_json = result.json()
#print(result_in_json)
df = pandas.json_normalize(result_in_json['data'])

#print(df)
df.to_csv("./sujant.csv",index = False)

pd.read_csv("sujant.csv")
a.to_html("crime.htm", index= False)
a.to_html("crime.html", index= False)
html_file = a.to_html()