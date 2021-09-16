# -*- coding: utf-8 -*-
"""
step02_news_WordCloud.py

1. pickle file 읽기: news(2월)
2. 명사 추출 : Kkma
3. 전처리: 단어길이 제한, 숫자 제외
4. Word Cloud
"""
from konlpy.tag import Kkma     # 형태소
from wordcloud import WordCloud # Class
import pickle # pickle file 읽기
kkma=Kkma()

#1. pickle file 읽기
path="C:\\ITWILL\\4_python-ll\\workspace\\chap07_TextMining\\data"

file = open(path+"/new_data.pkl",mode='rb')

news_data = pickle.load(file)
news_data
len(news_data) #11200

# docs-> sentence
ex_sents = [kkma.sentences(sent)[0] for sent in news_data]
len(ex_sents) #11200



#2. 명사 추출 : Kkma
nouns_word=[] # 명사 저장
for sent in ex_sents:
    for noun in kkma.nouns(sent):
        nouns_word.append(noun)

len(nouns_word) # 105382
nouns_word

#3. 전처리: 단어길이 제한, 숫자 제외
from re import match # 숫자 제외
nouns_count={} # 단어 카운터

for noun in nouns_word:
    if len(noun) > 1 and not(match('^[0-9]',noun)):
        nouns_count[noun] = nouns_count.get(noun,0) + 1

print(nouns_count)
len(nouns_count)#11246

#4. Word Cloud
#1) Top5 word
from collections import Counter #class

word_count=Counter(nouns_count)
top50_word=word_count.most_common(50) #top5
print(top50_word)


# 2) word cloud 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')

wc_result = wc.generate_from_frequencies(dict(top50_word))

import matplotlib.pyplot as plt

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기
plt.show()

