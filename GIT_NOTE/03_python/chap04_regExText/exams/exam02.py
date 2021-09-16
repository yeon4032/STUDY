'''
문2) 다음과 같은 여러 줄의 문자열을 대상으로 정규표현식을
       적용하여 email 양식이 올바른 것만 출력되도록 하시오. 
       
  <email 양식 조건> 
        아이디 : 첫자는 영문소문자, 단어길이 4자 이상
        호스트이름 : 영문소문자 시작, 단어길이 3자 이상 
        최상위 도메인 : 영문소문자 3자리 이하
        
  << 출력 결과 >>
  you2@naver.com
  kimjs@gmail.com
'''

from re import match # match 함수 이용 
# 정규표현식 기본 패턴 : '메타문자@메타문자.메타문자'

email = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""


for e in email.split(sep='\n'):
    re=match('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]{3}',e)
    if re :
        print(re)



