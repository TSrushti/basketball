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


# Converting to CSV file


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


def csv_to_html():
    """
    covert csv file to html
    :return:
    """
    try:
        a = pd.read_csv("crypto1.csv")
        a.to_html("crypto88.html", escape = False, index = False)
        index = 0
        for item in a['image']:
            a['image'].at[index] = '<img src = "' + item + '" width = 50>'
            index = index+1
        a.to_html("crypto88.html", escape = False, index = False)

    except requests.ConnectionError:
        logging.error("Server Down")
    except ImportError as ie:
        logging.error(ie)