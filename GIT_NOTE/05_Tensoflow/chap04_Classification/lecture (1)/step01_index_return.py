'''
index 리턴 
  1. argmin/argmax
   - 최소/최대 값의 index 반환 
   tf.arg_min -> tf.arg_min
  2. unique
   - 중복제거 
'''

import tensorflow as tf # ver2.0


# 1. argmin/argmax
a = tf.constant([5,2,1,4,3], dtype=tf.int32)
b = tf.constant([4,5,1,3,2])
c = tf.constant([[5,4,2], [3,2,4]]) # 2차원 

# dimension : reduce 차원(vector = 0) 
min_index = tf.argmin(a, 0) # 1차원 대상 
max_index = tf.argmax(b, 0) # 1차원 대상 
max_index2 = tf.argmax(c, 1) # 2차원 대상
min_index2 = tf.argmin(c,1) # 2차원 대상

print(min_index.numpy())  #2 -> 3번째 칼럼
print(tf.argsort(a,0)) #[2 1 4 3 0] (색인값임) <- 값을 기준으로 오름 차순 정렬 
print(max_index.numpy()) #1 -> 2 번째 칼럼
print(max_index2.numpy()) #[0 2] -> [1행,2행]
print(min_index2.numpy()) #[2 1] -> [1행,2행]

# 2. unique
c = tf.constant(['a','b','a','c','b', 'c'])

cstr, cidx = tf.unique(c)
print(cstr.numpy()) # [b'a' b'b' b'c'] # [byte'값' byte'값' byte'값'] 즉 '' 안의 값이 아니면 의미없다.
print(cidx.numpy()) # [0 1 0 2 1 2]





