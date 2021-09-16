# -*- coding: utf-8 -*-
"""
step02_konlp.py

konlpy:한글 형태소 분석을 제공하는 패키지 
pip install konlpy
"""
import konlpy

from konlpy.tag import Kkma #class
from konlpy.tag import Okt #class

'''
Kkma: 상세한 품사 정보 제공
OKt: 일반 품자 정보 제공(명사, 조사, 형용사)
'''

###############################################
### Kkma
###############################################3
kkma = Kkma() # 생성자

dir(kkma)
'''
'morphs', : 형태소 추출
'nouns',  : 문단->명사 추출
'pos',    : 품사 추출
'sentences',: 문단-> 문장 추출
'''

# 문단-> 문장
para = "나는 홍길동 입니다. age는 23세 입니다. 대한민국을 사람 만세 입니다."

ex_sent = kkma.sentences(para)
print(ex_sent)
#['나는 홍길동 입니다.', 'age는 23세 입니다.', '대한민국을 사람 만세 입니다.']
len(ex_sent) #3

#문단-> 명사(단어)
ex_nouns = kkma.nouns(para)
print(ex_nouns)
#['나', '홍길동', '23', '23세', '세', '대한', '대한민국', '민국', '사람', '만세']
len(ex_nouns) #10

#문단-> 품사(형태소)
ex_pos = kkma.pos(para)
print(ex_pos)
'''
[('형태소','품사')]
[('나', 'NP'), ('는', 'JX'), ('홍길동', 'NNG'), ('이', 'VCP'), ('ㅂ니다', 'EFN'), ('.', 'SF'), 
 ('age', 'OL'), ('는', 'JX'), ('23', 'NR'), ('세', 'NNM'), ('이', 'VCP'), ('ㅂ니다', 'EFN'), 
 ('.', 'SF'), ('대한민국', 'NNG'), ('을', 'JKO'), ('사람', 'NNG'), ('만세', 'NNG'), ('이', 'VCP'), 
 ('ㅂ니다', 'EFN'), ('.', 'SF')]
'''

len(ex_pos)#20
#NNG 일반 명사 NNP 고유 명사 NP 대명사

nouns=[] # 명사 저장
for word,wclass  in ex_pos: # ('형태소','품사')
    if wclass == 'NNG' or wclass == 'NNP' or wclass == 'NP':
        nouns.append(word)

print(nouns)
#['나', '홍길동', '대한민국', '사람', '만세']

#형태소
kkma.morphs(para)



######################################
#### Okt
######################################
okt=Okt()
dir(okt)
'''
'morphs', :형태소 추출
'normalize' : 문단 -> 문장
'nouns', 문장-> 단어
'pos', 형태소 + 품사
'''

okt.morphs(para)
'''
['나','는','홍길동','입니다',.','age','는','23','세','입니다','.'
 ,'대한민국','을','사람','만세','입니다','.']
'''

okt.normalize(para) # string type 으로 추출됨
'''
'나는 홍길동 입니다. age는 23세 입니다. 대한민국을 사람 만세 입니다.'
'''

okt.nouns(para)
#['나', '홍길동', '세', '대한민국', '사람', '만세']

okt.pos(para) # 품사 부착 
'''
[('나', 'Noun'),('는', 'Josa'),('홍길동', 'Noun'),('입니다', 'Adjective'),('.', 'Punctuation'),
 ('age', 'Alpha'),('는', 'Verb'),('23', 'Number'),('세', 'Noun'),('입니다', 'Adjective'),('.', 'Punctuation'),
 ('대한민국', 'Noun'),('을', 'Josa'),('사람', 'Noun'),('만세', 'Noun'),('입니다', 'Adjective'),('.', 'Punctuation')]
'''

ex_pos=okt.pos(para)

#단어 백터:필요한 품사 추출 
nouns=[] # 명사 저장

for word,wclass in ex_pos:
    if wclass == 'Noun' or wclass == 'Alpha':
        nouns.append(word)
       
print(nouns)
# ['나', '홍길동', 'age', '세', '대한민국', '사람', '만세']

