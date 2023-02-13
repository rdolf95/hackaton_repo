import json
from datetime import  datetime,timedelta
from pykrx import stock
import sqlite3
from stock_price import get_stock_price, get_etf_price, get_kospi_price




def get_port_graph_data(param):

    con = sqlite3.connect("hedgeNOhedgeDB.db")
    cur = con.cursor()
    #data 조회
    row_list = []
    if param == '0':
        cur.execute(" SELECT * FROM 'Stock' ")
    elif param == '1':
        cur.execute(" SELECT * FROM 'Stock2' ")

    row_list = cur.fetchall()

    today = datetime.now()
    today = today.strftime('%Y%m%d')
    prev_month = datetime.now() - timedelta(days=30)
    prev_month = prev_month.strftime('%Y%m%d')
    difflist = [0 for _ in range(30)]

    datelist = [0 for _ in range(30)]

    #내가 보유한 주식정보(포트폴리오) DB에서 가져옴
    diff = []
    for i in row_list:  # i: 종목별
        tick = i[1]
        num = i[2]
        buy = i[3]
        diff = get_stock_price(fromdate=prev_month, todate=today, ticker= tick)

        for j in range(len(diff)):  # j : 날짜별
            difflist[j] += (diff.loc[j][1] - buy) * num

    for j in range(len(diff)):  # j : 날짜별
        datelist[j] = diff.loc[j][0]

    result = []

    for j in range(len(datelist)):
        if datelist[j] != 0:
            result.append((datelist[j].strftime("%Y/%m/%d"), str(difflist[j])))

    #print(result)
    # difflist : 최근 30일간의 내 portfolio 수익률을 list로 저장 (영업일이 아닌 날은 마지막에 0으로 들어감)

    return json.dumps(result) #리스트 형태로 데이터 전송


def get_etf_graph_data():

    today = datetime.now()
    today = today.strftime('%Y%m%d')
    prev_month = datetime.now() - timedelta(days=30)
    prev_month = prev_month.strftime('%Y%m%d')

    etfDiff = get_etf_price(fromdate=prev_month, todate=today, ticker= '289480')
    etfDiffList = [0 for _ in range(30)]

    for i in range(len(etfDiff)):
        etfDiffList[i] = str(etfDiff.loc[i][1])

    #print(etfDiffList)
    # etfDiffList : 최근 30일간의 ETF 수익률을 list로 저장 (영업일이 아닌 날은 마지막에 0으로 들어감)

    return json.dumps(etfDiffList) #리스트 형태로 데이터 전송


def get_kospi_graph_data(param):

    today = datetime.now()
    today = today.strftime('%Y%m%d')
    prev_month = datetime.now() - timedelta(days=30)
    prev_month = prev_month.strftime('%Y%m%d')

    kospi_diff = get_kospi_price(fromdate= prev_month, todate= today, ticker= "1028")
    kospiDiffList = [0 for _ in range(30)]

    print(kospi_diff)
    

    for i in range(len(kospi_diff)):
        kospiDiffList[i] = (str(kospi_diff.loc[i][0].strftime("%Y/%m/%d")), str(kospi_diff.loc[i][1]))

    #print(kospiDiffList)
    # kospiDiffList : 최근 30일간의 kospi 데이터를 list로 저장 (영업일이 아닌 날은 마지막에 0으로 들어감)

    return json.dumps(kospiDiffList) #리스트 형태로 데이터 전송

def get_port_profit(param):

    json_res = {}

    con = sqlite3.connect("hedgeNOhedgeDB.db")
    cur = con.cursor()
    #data 조회
    if param == '0':
        cur.execute(" SELECT * FROM 'Stock' ")
    elif param == '1':
        cur.execute(" SELECT * FROM 'Stock2' ")
    row_list = cur.fetchall()

    today = datetime.now()
    today = today.strftime('%Y%m%d')


    #내가 보유한 주식정보(포트폴리오) DB에서 가져옴
    for i in row_list:

        ticker = i[1]
        company_name = stock.get_market_ticker_name(ticker)
        stock_num = i[2]
        buy_price = i[3]
        
        #cur_price = get_stock_price(fromdate=today, todate=today, ticker= ticker).loc[0][1]

        cur_price = get_stock_price(fromdate='20230210', todate='20230210', ticker= ticker).loc[0][1]
        profit = (cur_price - buy_price) / buy_price * 100
        total = cur_price * stock_num

        stock_dict = {}
        stock_dict['ticker'] = str(ticker)
        stock_dict['num'] = str(stock_num)
        stock_dict['buy_price'] = str(buy_price)
        stock_dict['cur_price'] = str(cur_price)
        stock_dict['profit'] = str(profit)
        stock_dict['total_price'] = str(total)

        json_res[company_name] = stock_dict

    #print(json_res) #딕셔너리 형태로 포트폴리오 데이터 전송

    return json.dumps(json_res, ensure_ascii=False) 

def get_cur_kospi():

    today = datetime.now()
    today = today.strftime('%Y%m%d')
    prev_month = datetime.now() - timedelta(days=30)
    prev_month = prev_month.strftime('%Y%m%d')

    kospi_diff = get_kospi_price(fromdate= prev_month, todate= today, ticker= "1028")
    kospiDiffList = [0 for _ in range(30)]

    print(kospi_diff)
    

    for i in range(len(kospi_diff)):
        kospiDiffList[i] = (str(kospi_diff.loc[i][0].strftime("%Y/%m/%d")), str(kospi_diff.loc[i][1]))

    #print(kospiDiffList)
    # kospiDiffList : 최근 30일간의 kospi 데이터를 list로 저장 (영업일이 아닌 날은 마지막에 0으로 들어감)

    return json.dumps(kospiDiffList) #리스트 형태로 데이터 전송
