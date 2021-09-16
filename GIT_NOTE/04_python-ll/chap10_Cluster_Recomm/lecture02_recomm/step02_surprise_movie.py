# -*- coding: utf-8 -*-
"""
step02_surprise_movie.py
"""

import pandas as pd # csv file
from surprise import SVD # SVD model 
from surprise import Reader, Dataset # SVD dataset

# 1. dataset loading
ratings = pd.read_csv('C:\\ITWILL\\4_python-ll\\data/movie_rating.csv')
print(ratings) #  평가자[critic]   영화[title]  평점[rating]


# 2. pivot table 작성 : row(영화제목), column(평가자), cell(평점)
print('movie_ratings')
movie_ratings = pd.pivot_table(ratings,
               index = 'title',
               columns = 'critic',
               values = 'rating').reset_index()

print(movie_ratings) # default index 추가 
'''
critic      title  Claudia  Gene  Jack  Lisa  Mick  Toby -> 추천 대상자
0         Just My      3.0   1.5   NaN   3.0   2.0   NaN
1            Lady      NaN   3.0   3.0   2.5   3.0   NaN
2          Snakes      3.5   3.5   4.0   3.5   4.0   4.5
3        Superman      4.0   5.0   5.0   3.5   3.0   4.0
4       The Night      4.5   3.0   3.0   3.0   3.0   NaN
5          You Me      2.5   3.5   3.5   2.5   2.0   1.0
'''

# 3. SVD dataset 생성
reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(ratings, reader=reader)

# 4. train/test set 생성
dir(data)
trainset = data.build_full_trainset() # 훈련셋
testset = trainset.build_testset() # 검정셋


# 5. SVD model 생성
obj = SVD()
model = obj.fit(trainset)


# 6.평점 예측치: 전체 사용자
all_pred=model.test(testset)
print(all_pred)


#7. Toby 사용자 미관람 영화 추천 예측
#model.predict(target 사용자의id, 아이템id, 실제 평점)
user_id = 'Toby' # 추천 대상자
items = ['Just My', 'Lady', 'The Night'] # 추천 아이템
actual_rating = 0  


for item_id in items:
    svd_pred = model.predict(user_id, item_id, actual_rating)
    print(svd_pred)

'''
user: Toby       item: Just My    r_ui = 0.00   est = 2.87   {'was_impossible': False}
user: Toby       item: Lady       r_ui = 0.00   est = 3.04   {'was_impossible': False}
user: Toby       item: The Night  r_ui = 0.00   est = 3.41   {'was_impossible': False}  <- 가장 높은 평점(est)
'''













