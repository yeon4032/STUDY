# -*- coding: utf-8 -*-
"""
 선형대수(linear algebre) 관련 함수 : ppt.57 참고
  - 수학의 한 분야 
 - 벡터 또는 행렬을 대상으로 한 연산
 - 응용분야: 차원 축소, 행렬 분해, 코사인 유사도,연립방정식 해
"""

import numpy as np 

# 1. 선형대수 관련 함수

# 1) 단위행렬 : 대각원소가 1이고, 나머지는 모두 0인 n차 정방행렬
eye_mat = np.eye(3)  # n=3
print(eye_mat) # 3차원의 정방 행렬 (행열 길이 같은거 를 정방 행렬이라한다.)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''

# 2) 대각행렬 : 대각성분 이외의 모든 성분이 모두 '0'인 n차 정방행렬
x = np.arange(1,10).reshape(3,3)
print(x)

diag_vec = np.diag(x)
print(diag_vec) #대각성분 [1 5 9]

# 대각행렬 = 단위행렬 * 대각성분 
diag_mat = eye_mat * diag_vec
print(diag_mat)
'''
[[1. 0. 0.]
 [0. 5. 0.]
 [0. 0. 9.]]
'''

# 3) 대각합 : 정방행렬의 대각에 위치한 원소들의 합 
trace_scala = np.trace(diag_mat) # 2차원 
print(trace_scala) # [1 5 9] = 15.0


# 4) 행렬식 : 대각원소의 곱과 차 연산으로 scala 반환 
x = np.array([[3,4], [1,2]])
print(x)
'''
[[3 4]
 [1 2]]
'''
det_scala = np.linalg.det(x)
print(det_scala) #2.0000000000000004 

############
det=((3*2)-(1*4))
print(det)
#########

# 5) 역행렬 : 행렬식의 역수를 정방행렬 대응 곱셈 
inv_mat = np.linalg.inv(x)
print(inv_mat)
'''
[[ 1.  -2. ]
 [-0.5  1.5]]
'''
#위의 값은 아래와 같다

'''
1/det* X^-1 

 
X^-1 => [[2 -4]
        [-1 3]]

'''

#6) 행렬식과 역행렬 관계
'''
-행렬식으로 역행렬 존제 유무 판단
-det==0 -> 역행렬 존재 않는다.
-det!=0 -> 역핼렬 존재 한다.
'''

#ex) 역행렬 존제 하지 않음
x2=np.array([[3,0],[1,0]])
x2
'''
array([[3, 0],
       [1, 0]])
'''

det = np.linalg.det(x2)
print('행렬식=',det) #행렬식= 0.0

inv_mat2 = np.linalg.inv(x2)
#LinAlgError: Singular matrix 오류 등장 그럼으로 역행렬 존제 하지 않음










