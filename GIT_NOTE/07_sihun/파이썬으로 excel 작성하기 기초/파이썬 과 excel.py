# -*- coding: utf-8 -*-
"""
파이썬 엑셀 자동화 도구 종류
1. xlwings
- 엑셀 자동화 스크립팅,엑셀의 VBA를 python으로 대체
- window,OSX지원 설피된 엑셀 필요
- import openpyxl
- wb=openpyxl.load_workbook('@@@.xlsx')


2. openpyxl
- 2010(.xlsx) 포멧 일고 쓰기 지원
- 설피된 엑셀 필요 없음

3.xlrd&xlwt
-엘셀 파일 읽기/쓰기 
-설치된 엑셀 필요 없음

4. xlsewriter
- 2010(.xlsx) 포멧 쓰기, 차트 기능
- 설치된 엑셀 필요 없음

5.PyWin32
- 윈도우의 COM 기술(정확히는 OLE Automation) 사용
- 엑셀 뿐만 아니라 다양한 오피스 제품과 상호작용이 가능
- windows 지원, 설치된 엑셀 필요.
"""

