# -*- coding: utf-8 -*-
"""
step02_module_function.py


묘듈(module) 함수
 - 파이썬 제공 함수
 - 라이브러리 함수(*.py)
 - 유형 : built-in 모듈, import 모듈
"""

# 1. built-in 모듈
dataset=list(range(1,6))
print(dataset) # [1, 2, 3, 4, 5]

# built-in 모듈 제공 함수
print('sum=',sum(dataset))
print('max=',max(dataset))
print('min=',min(dataset))
print('len=',len(dataset))

help(len) # 함수 출처
# Help on built-in function len in module builtins:

# 2. import 모듈 
import statistics # 수학/통계 함수 상용 (statistics.py 의 파일 가지고 온거임) - 방법1
'''
source 확인 : Ctrl + 클릭
'''
#from모듈import 함수1,함수2,....
from statistics import mean, median, stdev # - 방법2)권장

print('방법1-평균:',statistics.mean(dataset))
print('방법2-평균:', mean(dataset))

print('중위수:', median(dataset))
print('표준편차:', stdev(dataset))
