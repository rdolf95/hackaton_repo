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




# ====================================================
#                      라우터
# ====================================================
app = Flask(__name__, template_folder="template", static_folder="static")



@app.route('/', methods=['get'])
def index():
    return render_template("buy_option.html")

@app.route('/get_premium', methods=['post'])
def get_premium():

    print("get premium!")

    str = request.form.get('strike_price')
    print(str)

    return json.dumps(  'hello'  ) #리스트 형태로 데이터 전송



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080, threaded=True)