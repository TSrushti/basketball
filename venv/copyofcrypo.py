import pandas.io.json
import requests
import csv
import pandas as pd
import pdfkit
from lxml import html, etree
import matplotlib.pyplot as plt
import logging

logging.basicConfig(filename='logging_statements.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

result = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"
    "&sparkline=false&price_change_percentage=1h%2C24h",
    headers=headers)

""" got the json format file and status code of the requesting url"""

def json_to_csv():
    """
    Convert the json to csv formate
    :return:none
    """
    try:
        result_in_json = result.json()

        df = pandas.json_normalize(result_in_json)
        csv_file = df.to_csv(index=False)
        with open("./crypto1.csv", "w")as file:
            file.write(csv_file)
            file.close()
        logging.info('Data Retrieved')

    except requests.ConnectionError:
        logging.error("Server Down")
    except ImportError as ie:
        logging.error(ie)

# Converting to Html

def csv_to_html():
 try:
   a = pd.read_csv("crypto3.csv")
   a.to_html("crypto7.htm", escape = False, index = False)
index = 0
 except
for item in a['image']:
    a['image'].at[index] = '<img src = "'+ item + '" width = 50>'
    index = index+1
a.to_html("crypto7.html", escape = False, index = False)
html_file = a.to_html()

except



# converting to xml
def coverting_to_lxml():
 if __name__ != '__main__':
     pass
 else:
     file = "crypto7.html"
 with open(file, 'r', encoding = 'utf-8') as inp : htmldoc= html.fromstring(inp.read())

 with open("crypto22.xml", 'wb') as out : out.write(etree.tostring(htmldoc))

# converting to PDF
# options = {
#       'page-size': 'B0',
#      'dpi': 400
# }
# config = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
# pdfkit.from_string('crypo7.html', 'crypo11PDF.pdf')
# pdfkit.from_file('crypto7.html', 'crypo11PDF.pdf', configuration = config, options = options)
