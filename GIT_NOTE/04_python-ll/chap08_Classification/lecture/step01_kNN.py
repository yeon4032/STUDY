# -*- coding: utf-8 -*-
"""
step01_kNN.py

-알려진 범주로 알려지지 않은 범주 분류
- 유클리드 거리 계산식 이용 
"""

from sklearn.neighbors import KNeighborsClassifier # class

# 1. dataset

# 알려진 그룹 
grape = [8, 5]   # 과일   -0 
fish = [2, 3]    # 단백질 -1
carrot = [7, 10] # 채소   -2
orange = [7, 3]  # 과일   -0
celery = [3, 8]  # 채소   -2
cheese = [1, 1]  # 단백질 -1


know_group= [grape, fish, carrot, orange, celery, cheese] # x변수
print(know_group)
# [[8, 5], [2, 3], [7, 10], [7, 3], [3, 8], [1, 1]]

label = [0,1,2,0,2,1] # y변수

class_category= ['과일','단백질', '채소'] # 그룹 이름

# 2. 분류기 
knn = KNeighborsClassifier(n_neighbors=3 ) # 최근접 이웃 수 =k

model = knn.fit(X=know_group, y=label)

#3. 분류기 평가
x= int(input('단맛(1~10):')) #단맛 (1~10)
y= int(input('아삭거림(1~10):')) #아삭거림 (1~10)

test_X=[[x,y]]

# class 예측
y_pred = model.predict(X = test_X)
print(y_pred)

print('분류결과:', class_category[y_pred[0]])
#분류결과: 단백질 (2,4)





























