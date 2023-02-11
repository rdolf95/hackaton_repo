import sqlite3

print("sqlite3라이브러리 : " + sqlite3.version)
print("SQLite DB엔진 버전 : "+sqlite3.sqlite_version)

con = sqlite3.connect('./hedgeNOhedgeDB.db')
cur = con.cursor()

# #테이블 생성
# cur.execute("CREATE TABLE Member(ID TEXT, PW TEXT, Name TEXT, Deposit INTEGER);")
# cur.execute("CREATE TABLE Stock(ID TEXT, Ticker TEXT, Num INTEGER);")
# cur.execute("CREATE TABLE Option(ID TEXT, Ticker TEXT, Type TEXT, Num INTEGER, StrikePrice REAL, Premium REAL);")

# #데이터 삽입
# cur = con.cursor()
# cur.execute("INSERT INTO Member Values('Koscom', '1234','Koscom', 10000000000);")
# con.commit()#005930 삼성전자, 100주 보유
# cur.execute("INSERT INTO Stock Values('Koscom', '005930', 100);")
# con.commit()
# cur.execute("INSERT INTO Option Values('Koscom', '201s420','call', 10, 420, 1.04);")
# #옵션 티커?
# con.commit()


# cur.execute("INSERT INTO Stock Values('Koscom', '000660', 30),('Koscom', '068270', 30),('Koscom', '000660', 30),('Koscom', '005490', 10);")
# con.commit()

# cur.execute("UPDATE Stock set Num=50 WHERE Ticker = '005930';")
# con.commit()

cur.execute('SELECT * FROM Stock')
row = cur.fetchall()
for rows in row:
    print(rows)
con.close()
#g.