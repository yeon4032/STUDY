# -*- coding: utf-8 -*-
"""
물가를 예측하는 인공지능

출처
#https://www.youtube.com/watch?v=C_MOtffSues
Microsoft Visual C++ 14.0 설치해야한다고 나오네요.
"""

#패키지
import numpy as np
import pandas as pd
from fbprophet import Prophet # 이거 어떻게 하죠?
import os

#dataset load
os.chdir('C:/ITWILL/4_python-ll/data')
df=pd.read_csv('avocado.csv') #찾아보자
df.head()

#type알아보기
df.groupby('type').mean()

#전처리
df=df.loc[(df.type=='conventional')&(df.region=='TotalUS')]
df['Date'] = pd.to_datetime(df['Date']) #날짜형식 포멧으로 변경
data = df[['Date','AveragePrice']].reset_index(drop=True)
data = data.rename(columns={'Date':'ds','AveragePrice':'y'})
data.head()

#데이터 시각화
data.plot(x='ds', y='y', figsize=(16,8))

#Prhphet 사용
model=Prophet()
model.daily_seasonality=True
model.weekly_seasonality=True
model.fit(data) #학습

#예측
future = model.make_future_dataframe(periods=365)
forecast=model.predict(future)
forecast.tail()

#예측 그래프로 만들기
fig1=model.plot(forecaset)


#영향을 주는 요소가 무었인지 분석해서 보여준다
fig2=model.plot_components(forecast)



'''
INFO:numexpr.utils:NumExpr defaulting to 4 threads.
INFO:fbprophet:Disabling weekly seasonality. Run prophet with weekly_seasonality=True to override this.
INFO:fbprophet:Disabling daily seasonality. Run prophet with daily_seasonality=True to override this.
KeyError: 'metric_file'
'''


'''
윈도우10에서 Anaconda를 설치해 파이썬을 사용하고 있었다.

 

데이터 관련 학습을 진행하면서 fbprophet 라이브러리를 설치해야 했다.

 + fbprophet 0.7.1을 기준으로 진행했다.

    추가 라이브러리는 pandas 1.1.0, matplotlib 3.3.1 버젼으로 진행했다.

 

Anaconda에서 아래와 같은 방법으로 fbprophet을 설치 할 수 있다.

conda install -c conda-forge fbprophet
 

그런데 설치 이후 소스 코드를 실행시켰을 때 다음과 같은 오류가 발생했다.

fbprophet:Disabling weekly seasonality. Run prophet with weekly_seasonality=True to override this. 
INFO:fbprophet:Disabling daily seasonality. Run prophet with daily_seasonality=True to override this. 

KeyError: 'metric_file' 
Exception ignored in: 'stanfit4anon_model_f5236004a3fd5b8429270d00efcc0cf9_7332008770348935536._set_stanargs_from_dict' 
KeyError: metric_file
 

우선 그 중 이 부분은 생략해도 문제가 없다.

fbprophet:Disabling weekly seasonality. Run prophet with weekly_seasonality=True to override this. 
INFO:fbprophet:Disabling daily seasonality. Run prophet with daily_seasonality=True to override this. 
fbprophet을 저장한 변수에 추가로 형광색으로 칠한 다음 내용을 추가로 아래 예시처럼 입력하면 된다.

m = Prophet()
m.daily_seasonality=True
m.weekly_seasonality=True
 

그리고 이 오류는 pystan 버젼 차이로 인해 발생했다는 것을 찾게 되었다.

KeyError: 'metric_file' 
Exception ignored in: 'stanfit4anon_model_f5236004a3fd5b8429270d00efcc0cf9_7332008770348935536._set_stanargs_from_dict' 
KeyError: metric_file
 

 

이전에 설치된 pystan의 버젼은 pystan 2.19.0.0이였다. 

해결 방법은 다음과 아래와 같이 pystan을 업그레이드 해 pystan 2.19.1.1로 바꾸면 해결 할 수 있었다.

pip install pystan --upgrade
실행 후 엄청난 기다림 이후 업데이트가 완료 되었고 잘 실행되었다.
'''