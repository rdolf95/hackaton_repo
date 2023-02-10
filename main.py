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
from stock_price import get_stock_price, get_etf_price




# ====================================================
#                      라우터
# ====================================================
app = Flask(__name__, template_folder="template", static_folder="static")



@app.route('/aaaa')
def index():

    return render_template("index.html")


@app.route('/', methods=['get'])
def home():

    con = sqlite3.connect("hedgeNOhedgeDB.db")
    cur = con.cursor()
    #data 조회
    cur.execute(" SELECT * FROM 'Stock' ")
    row_list = cur.fetchall()

    today = datetime.now()
    today = today.strftime('%Y%m%d')
    jubunju = datetime.now() - timedelta(days=30)
    jubunju = jubunju.strftime('%Y%m%d')
    # print(today)
    # print(jubunju)
    # yyyymmdd형식으로 날짜 출력부
    difflist = [0 for _ in range(30)]

    #내가 보유한 주식정보(포트폴리오) DB에서 가져옴
    for i in row_list:
        tick = i[1]
        company = stock.get_market_ticker_name(tick)
        buy = i[3]
        diff = get_stock_price(fromdate=jubunju, todate=today, ticker= tick)
        # print(diff)
        # print("\n"+company)
        # print("구입=",buy)
        # print("종가:",diff.loc[len(diff)-1][1])

        for i in range(len(diff)):
            difflist[i] += diff.loc[i][1] - buy
    #주식매수가격 - 종가 ==> diff.loc[0][1]

    for i in range(len(difflist)):
        difflist[i] = str(difflist[i])

    print(difflist)

    return render_template("res.html", ifrs = ifrs, res_obj=chart_res,
                        hidden_corp_name=hidden_corp_name,
                        f_info=f_info,
                        RD_LABEL_LIST=radar_label,RD_DATA_DICT=radar_dict,
                        BAR_LABEL_LIST=bar_label,
                        BAR_DATA_LIST_MCH=bar_mch_list,
                        BAR_DATA_LIST_DG=bar_dg_list,MY_NEWS=json_obj, MY_CODE=code,
                        MY_HIGH=high_stock, MY_LOW=low_stock, MY_CLOSE=close_stock,
                        MY_MAE=mae_mean,
                        # -------220222(날씨!!!!!!!!!!)
                        WEATHER_DATA_LIST=weather_list,  # PER PBR ROE EPS BPS
                        ICONS=icons,
                        FOREIGN=foreign,  # 외인 매수
                        GIGUAN=giguan,  # 기관 매수
                        ICONS2=icons2  # 외인, 기관 매수
                        )


    return json.dumps(difflist) #리스트 형태로 데이터 전송




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080, threaded=True)