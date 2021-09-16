# -*- coding: utf-8 -*-
"""
문) review_data.csv 파일의 'review2' 칼럼을 대상으로 다음과 같이 
    단계별로 단어의 빈도수를 구하고, 단어 구름으로 시각화하시오.
"""
import pandas as pd
from konlpy.tag import Okt
from wordcloud import WordCloud # class

# 1. file load 
review_data = pd.read_csv('C:/ITWILL/4_python-ll/data/review_data.csv', encoding='utf-8')

review_data.info()
'''
RangeIndex: 34525 entries, 0 to 34524
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   id       34525 non-null  int64 
 1   review   34525 non-null  object
 2   label    34525 non-null  int64 
 3   review2  34525 non-null  object
''' 

# review2 칼럼 선택 
review = review_data['review2']
len(review) #34525

okt = Okt()
dir(okt)

# 2. 문장 추출 :  Okt 클래스 이용
sents = [okt.normalize(sent) for sent in review]
len(sents) #11200
print(sents)

# 3. 명사 추출 : Okt 클래스 이용
'''
방법 1
ex_nouns = [noun for sent in sents for noun in okt.nouns(sent) ]
print(ex_nouns)
'''
#방법2
nouns=[]
for noun in sents:
    for L_noun in okt.nouns(noun):
        nouns.append(L_noun)

print(nouns)
# 4. 전처리 : 2음절~5음절 단어 선정  
from re import match # 숫자 제외
nouns_count={} # 단어 카운터

for noun in nouns:
    if len(noun) > 1 and len(noun) <6:
        nouns_count[noun] = nouns_count.get(noun,0) + 1

print(nouns_count)
len(nouns_count)#11246


# 5. WordCloud : top100 word 
#1) Top5 word
from collections import Counter #class

word_count=Counter(nouns_count)
top100_word=word_count.most_common(100) #top5
print(top100_word)


# 2) word cloud 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')

wc_result = wc.generate_from_frequencies(dict(top100_word))

import matplotlib.pyplot as plt

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기
plt.show()


