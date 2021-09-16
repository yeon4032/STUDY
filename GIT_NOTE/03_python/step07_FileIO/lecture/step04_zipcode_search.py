# -*- coding: utf-8 -*-
"""
step04_zipcode_search.py

우편번호 찾기
우편번호tab[도/시]tab[구]tab[주소] 
135-806	서울	강남구	개포1동 경남아파트		
[0]     [1]  [2]     [3]

135-807	서울	강남구	개포1동 우성3차아파트	(1∼6동)	
[0]     [1]  [2]     [3]               [4]
우편번호tab[도/시]tab[구]tab[주소] tab[세부주소]

"""

try:
    dong = input('검색핟 동 입력:')
    
    #우편번호 파일 읽기
    path='C:/ITWILL/3_python/workplace/step07_FileIO/data/'
    file = open(path+'zipcode.txt', mode='r', encoding='utf-8')
    line=file.readline() # 첫줄 읽기
    #print(line)
    
    cnt=0 #검색 주소 카운터
    while line: # line의 값이 null 이면 -> False -> 작동그만  # line!= Null -> True-> 계속 작동함
        line=line.split(sep='\t') # tab을 기준으로 나눈다.
        
        if line[3].startswith(dong): # 접두어 비교
            cnt+=1
            print('['+line[0]+']', line[1], line[2], line[3], line[4])
            
        line = file.readline()#두번째 ~마지막 줄(EoF)
        
    print('검색 주소 개수:', cnt)

except Exception as e:
    print('error:',e)
finally:
    file.close() # 객체 닫기









