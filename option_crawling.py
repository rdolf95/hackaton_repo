import requests
import pandas as pd
from io import BytesIO
from datetime import datetime
import calendar

path = 'option/'

option_name_list = pd.read_excel(path + '옵션명정리.xlsx', dtype={'name':str})
isu_nm = option_name_list.iloc[42, 1]
isu_nm_cd = option_name_list.iloc[42, 0]

_alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def calc_check_digit(number):
    number = ''.join(str(_alphabet.index(n)) for n in number)
    number = ''.join(
        str((2, 1)[i % 2] * int(n)) for i, n in enumerate(reversed(number)))
    return str((10 - sum(int(n) for n in number)) % 10)

def make_date_code(exp_year, exp_month):
    if exp_year == '96':
        year_code = '6'
    elif exp_year == '97':
        year_code = '7'
    elif exp_year == '98':
        year_code = '8'
    elif exp_year == '99':
        year_code = '9'
    elif exp_year == '00':
        year_code = '0'
    elif exp_year == '01':
        year_code = '1'
    elif exp_year == '02':
        year_code = '2'
    elif exp_year == '03':
        year_code = '3'
    elif exp_year == '04':
        year_code = '4'
    elif exp_year == '05':
        year_code = '5'
    elif exp_year == '06':
        year_code = 'A'
    elif exp_year == '07':
        year_code = 'B'
    elif exp_year == '08':
        year_code = 'C'
    elif exp_year == '09':
        year_code = 'D'
    elif exp_year == '10':
        year_code = 'E'
    elif exp_year == '11':
        year_code = 'F'
    elif exp_year == '12':
        year_code = 'G'
    elif exp_year == '13':
        year_code = 'H'
    elif exp_year == '14':
        year_code = 'J'
    elif exp_year == '15':
        year_code = 'K'
    elif exp_year == '16':
        year_code = 'L'
    elif exp_year == '17':
        year_code = 'M'
    elif exp_year == '18':
        year_code = 'N'
    elif exp_year == '19':
        year_code = 'P'
    elif exp_year == '20':
        year_code = 'Q'
    elif exp_year == '21':
        year_code = 'R'
    elif exp_year == '22':
        year_code = 'S'
    elif exp_year == '23':
        year_code = 'T'
    elif exp_year == '24':
        year_code = 'V'
    elif exp_year == '25':
        year_code = 'W'
    elif exp_year == '26':
        year_code = '6'
    elif exp_year == '27':
        year_code = '7'
    elif exp_year == '28':
        year_code = '8'
    elif exp_year == '29':
        year_code = '9'
    elif exp_year == '30':
        year_code = '0'
    elif exp_year == '31':
        year_code = '1'
    elif exp_year == '32':
        year_code = '2'
    elif exp_year == '33':
        year_code = '3'
    elif exp_year == '34':
        year_code = '4'
    elif exp_year == '35':
        year_code = '5'
    elif exp_year == '36':
        year_code = '6'

    if exp_month == '01':
        month_code = '1'
    elif exp_month == '02':
        month_code = '2'
    elif exp_month == '03':
        month_code = '3'
    elif exp_month == '04':
        month_code = '4'
    elif exp_month == '05':
        month_code = '5'
    elif exp_month == '06':
        month_code = '6'
    elif exp_month == '07':
        month_code = '7'
    elif exp_month == '08':
        month_code = '8'
    elif exp_month == '09':
        month_code = '9'
    elif exp_month == '10':
        month_code = 'A'
    elif exp_month == '11':
        month_code = 'B'
    elif exp_month == '12':
        month_code = 'C'
    
    return year_code, month_code


def crawling_krx_option(isu_nm, isu_cd, isu_srt_cd, isu_nm_cd, num_days):
    
    gen_req_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    
    query_str_parms = {
        'strtDd': datetime(int(isu_nm[9:13]), int(isu_nm[13:15].replace(' ', '')), num_days-1).replace(year=datetime(int(isu_nm[9:13]), int(isu_nm[13:15].replace(' ', '')), num_days-1).year-1).strftime('%Y%m%d'),
        'endDd': datetime(int(isu_nm[9:13]), int(isu_nm[13:15].replace(' ', '')), num_days).strftime('%Y%m%d'),
        'tboxisuCd_finder_drvprodisu0_1': isu_nm_cd +'/' + isu_nm,
        'isuCd': isu_cd,
        'isuCd2': 'KRDRVOPK2I',
        'codeNmisuCd_finder_drvprodisu0_1': isu_nm,
        'param1isuCd_finder_drvprodisu0_1': '',
        'strtDdBox1': datetime(int(isu_nm[9:13]), int(isu_nm[13:15].replace(' ', '')), num_days-1).replace(year=datetime(int(isu_nm[9:13]), int(isu_nm[13:15].replace(' ', '')), num_days-1).year-1).strftime('%Y%m%d'),
        'endDdBox1': datetime(int(isu_nm[9:13]), int(isu_nm[13:15].replace(' ', '')), num_days).strftime('%Y%m%d'),
        'strtDdBox2': datetime(int(isu_nm[9:13]), int(isu_nm[13:15].replace(' ', '')), num_days-1).replace(year=datetime(int(isu_nm[9:13]), int(isu_nm[13:15].replace(' ', '')), num_days-1).year-1).strftime('%Y%m%d'),
        'endDdBox2': datetime(int(isu_nm[9:13]), int(isu_nm[13:15].replace(' ', '')), num_days).strftime('%Y%m%d'),
        'juya': 'ALL',
        'rghtTpCd': 'T',
        'share': '1',
        'money': '3',
        'csvxls_isNo': 'false',
        'name': 'fileDown',
        'url': 'dbms/MDC/STAT/standard/MDCSTAT12602'
    }
    
    headers = {
        'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' #generate.cmd에서 찾아서 입력하세요

    }
    
    r = requests.get(gen_req_url, query_str_parms, headers=headers)
    
    gen_req_url = 'http://data.krx.co.kr/comm/fileDn/download_excel/download.cmd'
    
    form_data = {
        'code': r.content
    }
    
    r = requests.post(gen_req_url, form_data, headers=headers)
    
    df = pd.read_excel(BytesIO(r.content))
    
    #df['이름'] = isu_nm
    
    #df.to_excel(path + 'option/' + isu_nm +'.xlsx', index=False, index_label=None)
    
    #print('KRX option crawling completed :', isu_nm)
    
    return df


def option_crawl (option_type: str= '2', mat_yr: str= '2023', 
                  mat_month: str= '2', strike_price: str= '325.0')->pd.DataFrame:

    """
    Args:
        option_type: call option = 2, put option = 3
        mat_yr: 옵션 만기 년도
        mat_month: 옵션 만긴 월
        strike_price: 행사 가격

    Returns:
        해당 옵션의 일별 시세 데이터
        dataframe 형태 = [일자, 종가, 대비, 시가, 고가, 저가, 내제변동성, 익일기준가, 거래량, 거래대금, 미결제약정]

    Note:
        KOSPI 200 옵션. 변경하려면 index 변수를 바꿀것
    """


    #option_type = type      # call (put = 3)
    index = '01'            # KOSPI 200
    #mat_yr = year           # maturity year (T = 2023)
    #mat_yr_code = 'T'       # maturity year (T = 2023)
    #mat_month = month       # maturity month
    #strike_price = strike   # strike price

    mat_month_code = mat_month + ' '
    if int(mat_month) < 10:
        mat_month_code = '0' + mat_month + ' '

    if option_type == '2':
        option_type_code = 'C '
    elif option_type == '3':
        option_type_code = 'P '
    else:
        print('Invalid option type')
        return

    isu_nm = '코스피200 ' + option_type_code + mat_yr + mat_month_code + strike_price

    year_code, month_code = make_date_code(isu_nm[11:13], isu_nm[13:15])

    isu_nm_cd = option_type + index + year_code + mat_month + strike_price[:-2]


    isu_cd_last = isu_nm.split(".")[0][-3:].replace(' ', '0')
    isu_cd = 'KR4' + option_type + '01' + year_code + month_code + isu_cd_last
    isu_cd_check = calc_check_digit(isu_cd)
    isu_cd = isu_cd + isu_cd_check
    isu_srt_cd = isu_cd[0] + isu_cd[3:11]
    _, num_days = calendar.monthrange(int(isu_nm[9:13]), int(isu_nm[13:15].replace(' ', '')))

    

    return crawling_krx_option(isu_nm, isu_cd, isu_srt_cd, isu_nm_cd, num_days)


df = option_crawl()

print(df)
#print('전일 종가: ', df.loc[0]['종가'])