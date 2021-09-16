'''
문4) 다음 texts 객체를 대상으로 단계별로 텍스트를 전처리하시오. 


 <텍스트 전처리 후 결과> 
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


from re import sub

print('전처리 전 : ', texts)

# 1. 소문자 변경 
text_re=[]
text_re=[st.lower() for st in texts]
print(text_re)

# 2. 숫자 제거 
import re
texts_re2=[re.sub('[0-9]','',st) for st in text_re]
print(texts_re2)

# 3. 문장부호 제거 
punc_str='[,.?!:;]'
texts_re3=[re.sub(punc_str, '',st) for st in texts_re2]
print(texts_re3)
# 4. 영문자 제거 
texts_re4=[re.sub('[a-z|A-z]', '',st) for st in texts_re3]
print(texts_re4)
# 5. 특수문자 제거 
spec_str='[@#$%^&*()]'
texts_re5=[re.sub(spec_str, '',st) for st in texts_re4]
print(texts_re5)
# 6. 공백 제거(2칸 이상 공백 -> 1칸 공백)
texts_re6 = [ ' '.join(st.split()) for st in texts_re5]
print(texts_re6)







