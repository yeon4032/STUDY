'''
문3) 정규표현식을 적용하여 person을 대상으로 주민번호 양식이 올바른 
     사람을 대상으로 다음과 같은 출력 예시와 같이 주민등록번호를 출력하시오.
    
   <출력 예시> 
유관순 750905-******* 
홍길동 850905-******* 
강감찬 770210-*******  
'''

import re # 정규표현식 패키지 임포트

person = """유관순 750905-2049118
홍길동 850905-1059119
강호동 790101-5142142
강감찬 770210-1542001"""

for line in person.split("\n"):
    name=line[:3]
    jumin=re.findall('[가-힣]{3} [0-9]{6}-[1234]\\d{6}', line)
    
    if jumin:
        str_jumin=jumin[0]
        result=str_jumin[:10]+'-*******'
        print(result)


for line in person.split("\n"): 
    name = line[:3]
    jumin = re.findall('[가-힣]{3} \\d{6}-[1234]\\d{6}', line) 
    #print(jumin)
           
    if jumin :
        str_jumin = jumin[0]
        result = str_jumin[:10] + '-*******'                       
        print(result)





























text1=re.sub('[0-9]{7}','*******',person)
print(text1)

result=[]
for line in person.split('\n'):
    name=line[:3]
    jumin=re.findall('[가-힝]{3}\\d{6}-[1234]\\{6}',line)

    if jumin:
        str_jumin=jumin[0]
        result=str_jumin[:10]+'*******'
        print(result)

print(result)
