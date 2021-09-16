'''
Best Cluster 찾는 방법 
'''

from sklearn.cluster import KMeans # model 
from sklearn.datasets import load_iris # dataset 
import matplotlib.pyplot as plt # 시각화 

# 1. dataset load 
X, y = load_iris(return_X_y=True)
print(X.shape) # (150, 4)
print(X)

# 2. kMeans model 
obj = KMeans(n_clusters=3) # k=3
model = obj.fit(X)

# model 예측치 
pred = model.predict(X)
pred

# 3. Best Cluster 
size = range(1, 11) # k값 범위(1~10)
inertia = [] # 군집의 응집도 

for k in size :
    obj = KMeans(n_clusters = k) # 1 ~ 10
    model = obj.fit(X)
    inertia.append(model.inertia_) 

print(inertia)
'''
군집의 응집도를 나타내는 수치: 작을 수록 응집도 좋다.
- 중심점과 각 포인트 간의 거리 제곱의 합
'''

# best cluster 수 확인 
plt.plot(size, inertia, '-o')
plt.xticks(size)
plt.show()