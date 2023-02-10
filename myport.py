import sqlite3
from pykrx import bond
from stock_price import get_stock_price, get_etf_price
from pykrx import stock
import time
from datetime import timedelta
import datetime

con = sqlite3.connect("hedgeNOhedgeDB.db")
cur = con.cursor()
#data 조회
cur.execute(" SELECT * FROM 'Stock' ")
row_list = cur.fetchall()

#오늘날짜,(과거 일주일과 비교해서 수익 보여주자!)
today = datetime.datetime.now()
today = today.strftime('%Y%m%d')
jubunju = datetime.datetime.now() - datetime.timedelta(days=30)
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

print(difflist)

# TIGER 200 커버드콜 ATM 수익률
etfDiff = get_etf_price(fromdate=jubunju, todate=today, ticker= '289480')
etfDiffList = [0 for _ in range(30)]

for i in range(len(etfDiff)):
    etfDiffList[i] = etfDiff.loc[i][1]

print(etfDiffList)


#difflist에 일주일치 내 포트폴리오 수익(각일자별) list



