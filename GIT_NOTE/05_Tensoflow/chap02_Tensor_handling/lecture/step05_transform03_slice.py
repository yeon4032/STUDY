'''
slice
 - tensor를 slice하여 새로운 tensor 생성 
'''

import tensorflow as tf

# 1차원 : [10] -> a = [1,2,3,4,5,6,8,9,10]
print('arr1d slice')
arr1d = tf.constant([1,2,3,4,5,6,7,8,9,10])
arr1d # shape=(10,)

help(tf.slice)
'''
slice(input_, begin, size, name=None)
input_: slice 대상 객체
`begin` is zero-based; `size` is one-based.
begin[i]: i 원소 시작 위치 :0 base
size[i] : i원소 시작 우치 : 1 base
'''
print(tf.slice(arr1d, [2], [4])) # 3번째 -> [3 4 5 6]

# 2차원 : [2,5] -> b = [[1,2,3,4,5],[6,7,8,9,10]]
arr2d = tf.constant([[1,2,3,4,5],[6,7,8,9,10]])

print('arr2d slice')
print(tf.slice(arr2d, [0,0], [2,5])) # [0,0]:1행1열-> [2,5] slice 
print(tf.slice(arr2d, [0,0], [-1,-1])) # -1: 시작으로 부터 전체 원소
print(tf.slice(arr2d, [0,2], [2,3])) # [0,2]:1행3열 -> 2행에서 3개씩 slice 

#slice error
print(tf.slice(arr2d, [0,2], [2,5])) # element over 
print(tf.slice(arr2d, [1,2], [2,3])) # dim over

# 문제) 시작: 1행 3열 -> 1차원 3개 slice
print(tf.slice(arr2d, [0,2],[1,3])) # [3 4 5]


# 3차원 : [3,2,3]
print('arr3d slice')
arr3d = tf.constant([[[1, 1, 1], [2, 2, 2]],
                     [[3, 3, 3], [4, 4, 4]],
                     [[5, 5, 5], [6, 6, 6]]])

print(tf.slice(arr3d, [0,0,0], [3,2,3])) # 3차원 전체 원소 슬라이스
print(tf.slice(arr3d, [0,0,0], [-1,-1,-1])) # 3차원 전체 원소 슬라이스
print(tf.slice(arr3d, [0,0,0], [1,1,1])) # [[[1]]] : 3차원 전체에서 첫번째 원소 
print(tf.slice(arr3d, [1,0,0], [1,1,2])) # [[[3 3]]] : 2면에서 2개 원소 
print(tf.slice(arr3d, [1,0,0], [1,1,3])) # [[[3 3 3]]] : 2면에서 3개 원소

#문제 3면에서 2행 전체 slice
print(tf.slice(arr3d, [2,1,0], [1,1,3]))#[[6,6,6]]


