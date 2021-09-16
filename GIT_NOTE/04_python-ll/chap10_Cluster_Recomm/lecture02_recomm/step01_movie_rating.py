'''
영화 추천 시스템 알고리즘
 - 추천 대상자 : Toby   
 - 유사도 평점 = 미관람 영화평점 * Toby와의 유사도
 - 추천 영화 예측 = 유사도 평점 / Toby와의 유사도
'''

import pandas as pd

# 1. 데이터 가져오기 
ratings = pd.read_csv('C:\\ITWILL\\4_python-ll\\data/movie_rating.csv')
print(ratings) #  평가자[critic]   영화[title]  평점[rating]


# 2. pivot table 작성 : row(영화제목), column(평가자), cell(평점)
print('movie_ratings')
movie_ratings = pd.pivot_table(ratings,
               index = 'title',
               columns = 'critic',
               values = 'rating').reset_index()

print(movie_ratings) # default index 추가 



# 3. 사용자 유사도 계산(상관계수 R) : 번호 행 추가 효과 
sim_users = movie_ratings.corr().reset_index() # corr(method='pearson')
print(sim_users) # default index 추가 
'''
critic   critic   Claudia      Gene      Jack      Lisa      Mick      Toby
0       Claudia  1.000000  0.314970  0.028571  0.566947  0.566947  0.893405
1          Gene  0.314970  1.000000  0.963796  0.396059  0.411765  0.381246
2          Jack  0.028571  0.963796  1.000000  0.747018  0.211289  0.662849
3          Lisa  0.566947  0.396059  0.747018  1.000000  0.594089  0.991241
4          Mick  0.566947  0.411765  0.211289  0.594089  1.000000  0.924473
5          Toby  0.893405  0.381246  0.662849  0.991241  0.924473  1.000000
'''
sim_users['Toby']

# 4. Toby 미관람 영화 추출  
# 1) movie_ratings table에서 title, Toby 칼럼으로 subset 작성 
toby_rating = movie_ratings[['title', 'Toby']] # index 칼럼 추가 
print(toby_rating)
print(toby_rating.columns) # Index(['title', 'Toby']
# 칼럼명 교체 
toby_rating.columns=['title', 'rating']
print(toby_rating)
'''
critic title  rating
0    Just My     NaN
1       Lady     NaN
2     Snakes     4.5
3   Superman     4.0
4  The Night     NaN
5     You Me     1.0
'''

# 2) Toby 미관람 영화제목 추출 : rating null 조건으로 title 추출 
# 형식) DF.추출칼럼[DF.조건칼럼.isnull()]
toby_not_see = toby_rating.title[toby_rating.rating.isnull()] 
print(toby_not_see)
'''
0      Just My
1         Lady
4    The Night
'''

# Series -> list
toby_not_see = list(toby_not_see) 
toby_not_see # ['Just My', 'Lady', 'The Night']


# 3) raw data에서 Toby 미관람 영화 subset 생성 
rating_t = ratings[ratings.title.isin(toby_not_see)]
print(rating_t)
'''
     critic      title  rating
0      Jack       Lady     3.0
4      Jack  The Night     3.0
5      Mick       Lady     3.0
:
30     Gene  The Night     3.0
'''

# 5. Toby 미관람 영화 + Toby 유사도 join
# 1) Toby 유사도 추출 
toby_sim = sim_users[['critic','Toby']] # critic vs Toby 유사도 


# 2) 평가자 기준 병합  
rating_t = pd.merge(rating_t, toby_sim, on='critic')
print(rating_t)
'''
     critic      title  rating      Toby
0      Jack       Lady     3.0  0.662849
1      Jack  The Night     3.0  0.662849
2      Mick       Lady     3.0  0.924473
'''


# 6. 영화 추천 예측
# 1) 유사도 평점 계산 = Toby미관람 영화 평점 * Tody 유사도 
rating_t['sim_rating'] = rating_t.rating * rating_t.Toby
print(rating_t)
'''
     critic      title  rating      Toby  sim_rating
0      Jack       Lady     3.0    0.662849    1.988547
1      Jack  The Night     3.0    0.662849    1.988547
2      Mick       Lady     3.0    0.924473    2.773420
[해설] 평점과 유사도가 클 수록 유사도 평점은 커진다.
'''
# 2) 영화제목별 합계
gsum = rating_t.groupby(['title']).sum() # 영화 제목별 합계
 
# 3) 영화제목별 합계  Toby 영화추천 예측 = 유사도 평점 / Tody 유사도
print('\n*** 영화 추천 결과 ***')
gsum['predict'] = gsum.sim_rating / gsum.Toby
print(gsum)
'''
           rating  similarity  sim_rating   predict
title                                              
Just My       9.5    3.190366    8.074754  2.530981
Lady         11.5    2.959810    8.383808  2.832550
The Night    16.5    3.853215   12.899752  3.347790
'''
