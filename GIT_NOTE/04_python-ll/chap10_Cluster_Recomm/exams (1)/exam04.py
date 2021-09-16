# -*- coding: utf-8 -*-
"""
문3) 한국영화 후기(review_data.csv) 파일을 대상으로 아래와 같은 조건으로
키워드를 입력하여 관련 영화 후기를 검색하는 함수를 정의하시오.   

 <조건1> 사용할 칼럼 : review2 
 <조건2> 사용할 문서 개수 : 1번째 ~ 5000번째   
 <조건3> 코사인 유사도 적용 - 영화 후기 검색 함수
         -> 검색 키워드와 가장 유사도가 높은 상위 3개 review 검색  
 <조건4> 검색 키워드 : 액션영화, 시나리오, 중국영화 
        -> 위 검색 키워드를 하나씩 입력하여 관련 후기 검색   
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. dataset load 
data = pd.read_csv("C:\\ITWILL\\4_python-ll\\data/review_data.csv")
data.info() 
'''
 0   id       34525 non-null  int64 
 1   review   34525 non-null  object
 2   label    34525 non-null  int64 
 3   review2  34525 non-null  object -> 사용할 칼럼 
'''
print(data.head())


# 사용할 문서 5,000개 제한  
review = data.review2[:5000] # 1번째 ~ 5000번째 문서 


# 2. sparse matrix 생성 : overview 칼럼 대상 
obj=TfidfVectorizer(stop_words='english') # 단어생성기
#희소행렬
sp_mat = obj.fit_transform(review)
sp_mat.shape #(5000, 19361)

# scipy -> numpy array
sp_mat_arr = sp_mat.toarray()
sp_mat_arr.shape # (5000, 19361)

# 3. cosine 유사도 : 영화 후기 검색 함수  
def review_search(query) : 
    query_data = [query] # 문장 -> list 변경
    
    # 2)query DTM
    query_sm = obj.transform(query_data)
    query_sm_arr = query_sm.toarray()
    
    # 3)유사도 계산
    sim = cosine_similarity(query_sm_arr,sp_mat_arr) # (query, raw doc)
    print(sim.shape)
    sim=sim.squeeze # 2d->1d  : 차원수가 1인 차원 제거 or sim.reshape(5000)
    #2d(1,19361)-> 1d(19361,)
    
    # 4) 내림차순 정렬: index 정렬
    sim_idx = sim.argsort()[::-1]
    print(sim_idx) #[1281 1304  373 ...  906  907    0]
    
    # 5) TopN=5 영화추천하기
    for idx in sim_idx[:3]:
        print(f'sim:{sim[idx]}, review:{review[idx]}')

# 4. 검색 키워드 : 액션영화, 시나리오, 중국영화   
review_search(input('검색할 키워드 입력 : '))

'''
검색할 키워드 입력 : 액션영화
(1, 5000)
[4709 4559 1763 ... 3334 3335    0]
sim:0.5846263639334625, review:스웨덴식 액션영화 강추
sim:0.43431544406444184, review:나 범죄영화나 스릴러영화나 액션영화 디게 좋아하는데
sim:0.24862959769106963, review:년대 만들었을 법한 액션영화 감독이 돈이 많은가 보네요어찌 이런 영화를 의도하에 만든건지 심심해서 만든건지비디오영화도 이 정도는 아닌데 감독대단



검색할 키워드 입력 : 시나리오
(1, 5000)
[  71 1945  534 ... 3334 3335    0]
sim:0.6444909451577203, review:최고의영화죠 시나리오 굿
sim:0.5014644310272237, review:시나리오 쓰신 분 정말 존경스럽네요 
sim:0.39110728021204, review:참신하고 독특한 영화 울나라는 이런 시나리오 못 쓰나요



검색할 키워드 입력 : 중국영화
(1, 5000)
[1509    2 4999 ... 3335 3336    0]
sim:0.27677966931755404, review:요란법석만떨며 시끄럽기만 한 중국영화 스티븐시걸주연의 급 비디오용 영화보는듯 하다 개연성설득력리얼리티는 제로 시나리오는 저 멀리 년대 홍콩액션영화
sim:0.2723791172588158, review:갈수록 개판되가는 중국영화 유치하고 내용없음 폼잡다 끝남 말도안되는 무기에 유치한남무 아 그립다 동사서독같은 영화가 이건 류아류작이다
sim:0.0, review:주인공이 더 악당인영화재미있을 려고 영화봤는데더 스트레스받는 영화
'''





