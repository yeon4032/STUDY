'''
문제3) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : list -> set -> list
  
  <출력 예시>  
서울시 전체 동 개수 =  797
'''
import os
os.chdir('C:/ITWILL/3_python/workplace/step07_FileIO/data')

try :
    file = open("zipcode.txt", mode='r', encoding='utf-8')
    lines = file.readline() # 첫줄 읽기 
    dong = [] # 서울시 동 저장 list

#print(lines.split(sep='\t')) -> 를 사용해서 왜 tokens[3]를 사용 하는 지 이해하시요.
    while lines :       
        tokens = lines.split(sep='\t') # 토큰 생성 
      
        if tokens[1] == '서울' : # 서울시 주소지 확인 
            addr = tokens[3].split() # 주소 토큰(공백 분리)
            dong.append(addr[0]) # 동 추출 & 저장 
    
        lines = file.readline() # 2줄 ~ end줄 
    
    print('중복 포함 전체 동 개수 :', len(dong))
    
    # 중복 제거 : list -> set -> list
    re_dong = list(set(dong))
    print('서울시 전체 동 개수 = %d'%(len(re_dong)))  
    print(re_dong)     
    
except Exception as e :
    print('예외발생 :', e)
    
    
    
    