import json
import numpy as np
import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
from datetime import  datetime, date,timedelta
import yfinance as yf
from pykrx import stock
import math
import sqlite3
from stock_price import get_stock_price, get_etf_price, get_kospi_price
from option_crawling import option_crawl




# ====================================================
#                      라우터
# ====================================================
app = Flask(__name__, template_folder="template", static_folder="static")



@app.route('/', methods=['get'])
def index():
    return render_template("buy_option.html", cur_kospi = 325.0)

@app.route('/get_premium', methods=['post'])
def get_premium():

    strike_price = request.form.get('strike_price')
    mat_month = request.form.get('maturity_month')

    print(strike_price, mat_month)

    option_price = option_crawl (mat_month= mat_month, strike_price= strike_price)[1]
    #종가


    return json.dumps(str(option_price))



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080, threaded=True)