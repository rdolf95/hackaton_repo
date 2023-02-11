from pykrx import stock
import pandas as pd


com_df_srch =pd.read_csv('com_df_rm.csv',
                dtype={'stock_code': 'str', '표준코드': 'str', '단축코드': 'str', 'stock_code_ori':'str'},
                parse_dates=['listed_date', '상장일'])


def get_stock_price(fromdate: str= "20220720", todate: str= "20220810", name: str= '삼성전자', ticker: str= "none")->pd.DataFrame:
    """
    Args:
        fromdate: 검색 시작일
        todate: 검색 마지막일
        name: 종목 이름 (일부 매칭 가능)

    Returns:
        해당 주식 종가 데이터
        dataframe 형태 = [날짜, 시가, 고가, 저가, 종가, 거래량, 거래대금, 등락률]

    Note:
        fromdate ~ todate 까지 종가
    """
    
    if ticker == "none":
        ticker_list = com_df_srch[(com_df_srch['한글 종목명'].str.contains(name))|(com_df_srch['한글 종목명'].str.contains(name.upper()))][['yh_code', '한글 종목명']].head()
        ticker= ticker_list.values[0][0][0:6]

    ent_df = stock.get_market_ohlcv_by_date(fromdate= fromdate, todate= todate, ticker= ticker)
    ent_df = ent_df.reset_index()

    ent_df = ent_df.drop(['시가', '고가', '저가', '거래량', '거래대금', '등락률'], axis=1)
    ent_df.columns = ['Date', 'Close']
    
    return ent_df

#df = stock.get_index_ohlcv("20190101", "20190228", "1028")
#print(df.head(10))

def get_etf_price(fromdate: str= "20230108", todate: str= "20230208", ticker: str= "289480")->pd.DataFrame:
    """
    Args:
        fromdate: 검색 시작일
        todate: 검색 마지막일
        name: 종목 이름 (일부 매칭 가능)

    Returns:
        해당 주식 종가 데이터
        dataframe 형태 = [날짜, 시가, 고가, 저가, 종가, 거래량, 거래대금, 등락률]

    Note:
        fromdate ~ todate 까지 종가
    """
    ent_df = stock.get_etf_ohlcv_by_date(fromdate= fromdate, todate= todate, ticker= ticker)
    ent_df = ent_df.reset_index()

    ent_df = ent_df.drop(['NAV', '시가', '고가', '저가', '거래량', '거래대금', '기초지수'], axis=1)
    ent_df.columns = ['Date', 'Close']
    
    return ent_df

def get_kospi_price(fromdate: str= "20230108", todate: str= "20230208", ticker: str= "1028")->pd.DataFrame:
    """
    Args:
        fromdate: 검색 시작일
        todate: 검색 마지막일
        ticker: 지수 ticker

    Returns:
        해당 지수 종가 데이터
        dataframe 형태 = [날짜, 시가, 고가, 저가, 종가, 거래량, 거래대금, 등락률]

    Note:
        fromdate ~ todate 까지 종가
    """
    index_df = stock.get_index_ohlcv(fromdate= fromdate, todate= todate, ticker= ticker)
    index_df = index_df.reset_index()

    index_df = index_df.drop(['시가', '고가', '저가', '거래량', '거래대금', '상장시가총액'], axis=1)
    index_df.columns = ['Date', 'Close']
    
    return index_df

#print(get_etf_price())

#df = stock.get_index_ohlcv("20190101", "20190228", "1028")
#print(df.head(10))