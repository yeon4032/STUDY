# -*- coding: utf-8 -*-
'''
pykrx 모듈
'''
#pip install -U pykrx  # prompt 에서 pykrx 설치

from pykrx import stock

# 주식 가격정보 krx(한국거래소)에서 가지고 오기
df = stock.get_market_ohlcv_by_date("20190501", "20190531", "005930") # ("시작날짜", "종료날짜", "주식 코드")
#stock 모듈의 get_market_ohlcv_by_date( ) 함수를 호출하여 특정 거래일의 일봉 데이터를 데이터프레임 형태로 다운로드합니다.

'''
shift 함수
'''
from pykrx import stock

#shift
#데이터프레임에서 한 로우 또는 칼럼은 시리즈 객체인데 shift( )라는 메서드를 사용하면 원하는 수 만큼 시프트 시킬 수 있습니다.
df = stock.get_market_ohlcv_by_date("20180101", "20180531", "005930")
df["전날거래량"] = df["거래량"].shift(1)
cond = df["거래량"] > df["전날거래량"]
print(df[cond])


"""
이동평균
"""

#이동평균 등을 쉽게 계산하기 위한 rolling( ) 메서드를 제공합니다.

from pykrx import stock
 
df = stock.get_market_ohlcv_by_date("20180101", "20180531", "005930")
df['5일이동평균'] = df['종가'].rolling(window=5).mean()
print(df)
#rolling(windows=5) 메서드를 통해 위에서부터 5개의 데이터 묶음에 대해 mean( ) 메서드를 적용합니다.

#주어진 기간 동안 시가가 5일 이동평균선을 돌파한 횟수를 세어봅시다.
cond = df['5일이동평균'].shift(1) < df['시가']
print("상승일:", len(df[cond]))
print("영업일:", len(df)

