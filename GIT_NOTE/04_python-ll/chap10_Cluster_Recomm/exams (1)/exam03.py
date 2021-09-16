# -*- coding: utf-8 -*-
"""
문) food 데이터셋을 대상으로 작성된 피벗테이블(pivot table)을 보고 'g' 사용자가 아직
    섭취하지 않은 음식을 대상으로 추천하는 모델을 생성하고, 추천 결과를 확인하시오. 
"""

import pandas as pd
from surprise import SVD # SVD model 생성 
from surprise import Reader, Dataset # SVD data set 생성 


# 1. 데이터 가져오기 
food = pd.read_csv('C:\\ITWILL\\4_python-ll\\data/food.csv')
print(food.info()) #    id(user)  menu(item) count
food['count'].value_counts()

# 2. 피벗테이블 작성 
ptable = pd.pivot_table(food, 
                        values='count',
                        index='uid',
                        columns='menu', 
                        aggfunc= 'mean')

print(ptable)

# 3. rating 데이터셋 생성    
reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(food, reader=reader)

# 4. train/test set 생성 
trainset = data.build_full_trainset() # 훈련셋
testset = trainset.build_testset() # 검정셋

# 5. model 생성 : train set 이용 
obj = SVD()
model = obj.fit(trainset)

# 6. 'g' 사용자 대상 음식 추천 예측 
all_pred=model.test(testset)
print(all_pred)

user_id = 'g' # 추천 대상자
menus = ['식빵','우유','치킨'] # 추천 아이템
actual_rating = 0  


for menu_id in menus:
    svd_pred = model.predict(user_id,  menu_id, actual_rating)
    print(svd_pred)

'''
user: g          item: 식빵         r_ui = 0.00   est = 3.39   {'was_impossible': False}<- 추천
user: g          item: 우유         r_ui = 0.00   est = 3.05   {'was_impossible': False}
user: g          item: 치킨         r_ui = 0.00   est = 3.16   {'was_impossible': False}

'''
