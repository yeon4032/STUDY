'''
회귀분석용 sklearn dataset 정리 
'''
from sklearn import datasets # dataset 제공 library
import numpy as np

#y변수가 연속형
######################################
# 선형회귀분석에 적합한 데이터셋
######################################

# 1. iris
'''
붓꽃(iris) 데이터
붓꽃 데이터는 통계학자 피셔(R.A Fisher)의 붓꽃의 분류 연구에 기반한 데이터
•타겟 변수 : y변수
◦setosa, versicolor, virginica의 세가지 붓꽃 종(species)
•특징 변수(4) : x변수
◦꽃받침 길이(Sepal Length)
◦꽃받침 폭(Sepal Width)
◦꽃잎 길이(Petal Length)
◦꽃잎 폭(Petal Width)
'''
iris = datasets.load_iris() # Load the data
print(iris) 
print(iris.DESCR) # dataset 설명제공 : 변수특징, 요약통계 

print(iris.data) # x변수 
print(iris.data.shape) #(150, 4)

print(iris.target) # y변수(target)
print(iris.target.shape) #(150,)

# numpy -> DataFrame 
import pandas as pd
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
tg = pd.Series(iris.target, dtype="category") # 집단변수  
tg = tg.cat.rename_categories(iris.target_names) # 카테고리 이름 변경 

iris_df['species'] = tg # target 추가 
iris_df.head()
iris_df.info() 


# 차트 분석 : 각 특징별 타겟변수의 분포현황  
import seaborn as sn
import matplotlib.pyplot as plt

# 변수 간 산점도 : hue = 집단변수 : 집단별 색상 제공 
sn.pairplot(iris_df, hue="species")
plt.show() 

# 타겟변수(집단)별 특징 분포현황   
sn.distplot(iris_df[iris_df.species == "setosa"]["petal length (cm)"], label="setosa")
sn.distplot(iris_df[iris_df.species != "setosa"]["petal length (cm)"], label="others")
plt.legend() # 범례
plt.show()


# 2. 당료병 데이터셋
'''
442명의 당뇨병 환자를 대상으로한 검사 결과를 나타내는 데이터

•타겟 변수:y
1년 뒤 측정한 당료병 진행상태 정량적화 자료(연속형)

•특징 변수(10: 모두 정규화된 값):x
age : 나이 (세)
sex : 성별 
bmi : 비만도지수
bp : 평균혈압(Average blood pressure)
S1 ~ S6: 기타 당료병에 영향을 미치는 요인들 
'''
diabetes = datasets.load_diabetes() 
print(diabetes.DESCR) # 컬럼 설명, url
'''
:Target: Column 11 -> 1년기준으로 질병 진행상태를 정량적(연속형)으로 측정 
:Attribute Information: Age ~ S6
'''    
print(diabetes.target_names) # None : target 연속형 
print(diabetes.feature_names)
X, y = datasets.load_diabetes(return_X_y=True)

print(np.shape(X)) # (442, 10) : matrix
print(np.shape(y)) # (442,) : vector



# 3. boston 주택가격 
'''
보스턴 주택 가격 데이터(회귀 분석용 예제 데이터)

•타겟 변수
1978 보스턴 주택 가격: 506개 타운의 주택 가격 중앙값(단위 1,000 달러)
•특징 변수(13)
CRIM: 범죄율
INDUS: 비소매상업지역 면적 비율
NOX: 일산화질소 농도
RM: 주택당 방 수
LSTAT: 인구 중 하위 계층 비율
B: 인구 중 흑인 비율
PTRATIO: 학생/교사 비율
ZN: 25,000 평방피트를 초과 거주지역 비율
CHAS: 찰스강의 경계에 위치한 경우는 1, 아니면 0
AGE: 1940년 이전에 건축된 주택의 비율
RAD: 방사형 고속도로까지의 거리
DIS: 직업센터의 거리
TAX: 재산세율
'''
boston = datasets.load_boston()
print(boston)
print(boston.DESCR)
print(boston.target_names) # None : target 연속형 

boston_x = boston.data # 4개 columns
boston_y = boston.target

print(np.shape(boston_x)) # (506, 13) : matrix
print(np.shape(boston_y)) # (506,) : vector


# 4. california 주택가격 
'''
캘리포니아 주택 가격 데이터(회귀 분석용 예제 데이터)

•타겟 변수
1990년 캘리포니아의 각 행정 구역 내 주택 가격의 중앙값

•특징 변수(8) 
MedInc : 행정 구역 내 소득의 중앙값
HouseAge : 행정 구역 내 주택 연식의 중앙값
AveRooms : 평균 방 갯수
AveBedrms : 평균 침실 갯수
Population : 행정 구역 내 인구 수
AveOccup : 평균 자가 비율
Latitude : 해당 행정 구역의 위도
Longitude : 해당 행정 구역의 경도
'''
from sklearn.datasets import fetch_california_housing
california = fetch_california_housing()
print(california.DESCR)

cal_df = pd.DataFrame(california.data, columns=california.feature_names)
cal_df["MEDV"] = california.target
cal_df.tail()
cal_df.info() 

