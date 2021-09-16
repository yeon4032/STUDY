'''
numpy vs tensorflow
 1. 상수 생성 함수 
 2. 차원축소  수학 연산
'''

import tensorflow as tf # ver2.x


'''
1. 상수 생성 함수
 tf.constant(value, dtype, shape) : 지정한 값(value)으로 상수 텐서 생성   
 tf.zeros(shape, dtype) : 모양과 타입으로 모든 원소가 0으로 초기화된 텐서 생성 
 tf.ones(shape, dtype) : 모양과 타입으로 모든 원소가 1로 초기화된 텐서 생성
 tf.identity(input) : 내용과 모양이 동일한 텐서 생성   
 tf.fill(shape, value) : 주어진 scalar값으로 초기화된 텐서 생성 
 tf.linspace(start, stop, num) : start~stop 범위에서 num수 만큼 텐서 생성  
 tf.range(start, limit, delta) : 시작, 종료, 증감 으로 텐서 생성 
'''
a = tf.constant(10, tf.int32, (2, 3))
print(a)

b = tf.zeros( (2, 3) )# dtype=float32 기본타입 적용
print(b) # sess.run()

c = tf.ones( (2, 3) )# dtype=float32 기본타입 적용
print(c)

d = tf.identity(c)
print(d)

e = tf.fill((2, 3), 5) # (shape, value)
print(e) # sess.run(c)

f = tf.linspace(15.2, 22.3, 5)
print(f) 
#tf.Tensor([15.2   16.975 18.75  20.525 22.3  ]

g = tf.range(10, 1.5, -2.5) #(start, stop ,step) -> 
print(g) #tf.Tensor([10.   7.5  5.   2.5]

print('\n차원축소 관련 함수')
'''
2. 차원축소 수학 연산
 tf.reduce_sum(input_tensor, reduction_indices) : 지정한 차원을 대상으로 원소들 덧셈
 tf.reduce_mean(input_tensor, reduction_indices) : 지정한 차원을 대상으로 원소들 평균
 tf.reduce_prod(input_tensor, reduction_indices) : 지정한 차원을 대상으로 원소들 곱셈
 tf.reduce_min(input_tensor, reduction_indices) : 지정한 차원을 대상으로 최솟값 계산
 tf.reduce_max(input_tensor, reduction_indices) : 지정한 차원을 대상으로 최댓값 계산
 tf.reduce_all(input_tensor) : tensor 원소가 전부 True -> True 반환
 tf.reduce_any(input_tensro) : tensor 원소가 하나라도 True -> True 반환  
'''
data = [[1.5, 1.5], [2.5, 2.5], [3.5, 3.5]]
print(tf.reduce_sum(data, axis=0)) # 행축 합계:열 단위 합계 
print(tf.reduce_sum(data, axis=1)) # 열축 합계:행 단위 합계  

#전체 dat 연산
print(tf.reduce_mean(data)) # 2.5 # 전체 데이터 평균 (axis 생략시)
print(tf.reduce_max(data)) # 3.5 
print(tf.reduce_min(data)) # 1.5

bool_data = [[True, True], [False, False]] 
print(tf.reduce_all(bool_data)) # False
print(tf.reduce_any(bool_data)) # True


