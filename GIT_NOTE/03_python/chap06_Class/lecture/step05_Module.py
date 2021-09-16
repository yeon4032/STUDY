# -*- coding: utf-8 -*-
"""
step05_Module.py

패키지(package)= 폴더 유사함
 - 유사한모듈(module)을 꾸러미로 묶어놓은 단위
 - __init__.py : 패키지 초기화 모듈 포함
 

모듈(module)=파일 유사함
- 함수와 클래스를 포함한 파이썬 파일(*.py)

형식1)
import 패키지.모듈

형식2)
from 패키지.모듈 import 함수,클래스
"""
import os # os 관련 함수 제공: 작업경로 확인, 변경
os.getcwdb()#작업경로 확인
#'C:\\ITWILL\\3_python\\workplace\\myPackage'

os.chdir('C:\\ITWILL\\3_python\\workplace') #import할 패키지의 상위경로로 변경 할 필요가 있음
os.getcwdb()#작업경로 확인

#형식1)
import myPackage.module01

re=myPackage.module01.Adder(5,10)
print('덧셈=',re)

import myPackage.module01 as md #별칭 md 지칭
re= md.Adder(5,10)
print('덧셈=',re)


#형식2)
# from 패키지.모듈 import 함수,클래스
from myPackage.module01 import Adder, Mul

# 함수 호출
re= Adder(10,20)
print('덧셈=',re)

#클래스 객체 생성
m = Mul(10,5) #객체생성
print('곱셈=',m.mul())
































