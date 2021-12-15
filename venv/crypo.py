import pandas.io.json
import requests
import csv
import pandas as pd
import pdfkit
from lxml import html, etree
import matplotlib.pyplot as plt

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
result = requests.get(
                 "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h", headers=headers)

#print(result.text)
result_in_json = result.json()

#print(result_in_json)
df = pandas.json_normalize(result_in_json)
#print(df)
df.to_csv("./crypto1.csv", index = False)

# converting to HTML
a = pd.read_csv("crypto3.csv")
a.to_html("crypto7.htm", escape = False, index = False)
index=0
for item in a['image']:
    a['image'].at[index] = '<img src = "'+ item + '" width = 50>'
    index = index+1
#a.to_html("crypto7.html", escape = False, index = False)
html_file= a.to_html()

#converting to xml
#if __name__ == '__main__': file = "crypto7.html"
#with open(file, 'r', encoding = 'utf-8') as inp : htmldoc = html.fromstring(inp.read())

#with open("crypto22.xml", 'wb') as out : out.write(etree.tostring(htmldoc))

#converting to PDF
#options = {
 #       'page-size': 'B0',
  #      'dpi': 400
#}
#config = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
#pdfkit.from_string('crypo7.html', 'crypo11PDF.pdf')
#pdfkit.from_file('crypto7.html', 'crypo11PDF.pdf', configuration = config, options = options)

# To create bar chart
#df_sort = df.sort_values('current_price')
#df_sort[:20].plot(x='id', y='current_price',kind = 'bar')
#plt.title('Prices ')
#plt.xticks(rotation = 70)
#plt.ylabel('Price in USD')
#plt.legend(loc ='best')
#for i in range(len(df_sort[:20])):
 #  price = '{:.3f}'.format(df_sort[:20]['current_price'].values[i])
#plt.text(i, float(price), float(price), ha = 'center')
#plt.show()

#line chart
#df_sort = df.sort_values('current_price')
#df_sort[:20].plot(x='id', y='current_price',kind = 'bar')
#line1 = df_sort[:10].plot.line(x = 'id', y = 'current_price', label = "Crypto curency")
#plt.title("line chart of Cryptocurrency")
#plt.ylabel('Current Price')
#plt.show()

#pichart
#df_sort[:5].plot(x = 'id', y = 'current_price', kind = 'pie', labels = [x for x in df_sort[:7]['id']], autopct='%1.0f%%')
#plt.title('Crypto Prices')
#plt.legend(loc = 'upper left')
#plt.show()