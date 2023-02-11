import json
import numpy as np
import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
from datetime import  datetime, date,timedelta
import yfinance as yf
from code_cr import *
from pykrx import stock
import math
import sqlite3
from stock_price import get_stock_price, get_etf_price, get_kospi_price
from option_crawling import option_crawl



# ====================================================
#                      데이터
# ====================================================
com_df=pd.read_csv('com_df.csv',
                   dtype={'stock_code': 'str', '표준코드': 'str', '단축코드': 'str', 'stock_code_ori':'str'},
                   parse_dates=['listed_date', '상장일'])


from pykrx import stock
import math
import sqlite3
from stock_price import get_stock_price, get_etf_price, get_kospi_price

import port_data

# ====================================================
#                      라우터
# ====================================================
app = Flask(__name__, template_folder="template", static_folder="static")



# ====================================================
#                    메인 페이지 by 최상현
# ====================================================


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/buy_option')
def index():
    return render_template("buy_option.html")

@app.route('/dashboard')
def dashboard():
    return render_template("index.html")

@app.route('/strategy')
def strategy():
    return render_template("strategySelect.html")

@app.route('/strategySelectUp')
def strategyUp():
    return render_template("strategySelectUp.html")

@app.route('/strategySelectDown')
def strategyDown():
    return render_template("strategySelectDown.html")

@app.route('/get_premium', methods=['post'])
def get_premium():

    strike_price = request.form.get('strike_price')
    mat_month = request.form.get('maturity_month')

    print(strike_price, mat_month)

    option_price = option_crawl (mat_month= mat_month, strike_price= strike_price)[1]
    #종가


    return json.dumps(str(option_price))

@app.route('/get_port_graph_data')
def get_port_graph_data():
    return port_data.get_port_graph_data()

@app.route('/get_kospi_graph_data')
def get_kospi_graph_data():
    return port_data.get_kospi_graph_data()

@app.route('/get_port_profit')
def get_port_profit():
    return json.loads(port_data.get_port_profit())
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080, threaded=True)