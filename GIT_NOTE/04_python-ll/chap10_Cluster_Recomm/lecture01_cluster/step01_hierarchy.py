'''
계층적 군집분석(Hierarchical Clustering) 
'''

from sklearn.datasets import load_iris # dataset
import pandas as pd # DataFrame
from scipy.cluster.hierarchy import linkage, dendrogram # 군집분석 도구
import matplotlib.pyplot as plt # 산점도 시각화 

# 1. dataset loading
iris = load_iris() # Load the data

X = iris.data # x변수 
y = iris.target # y변수(target) - 숫자형 : 거리계산 

# numpy -> DataFrame 
iris_df = pd.DataFrame(X, columns=iris.feature_names)
iris_df['species'] = y # target 추가 
iris_df.head()
iris_df.info() 


# 2. 계층적 군집분석 
clusters = linkage(iris_df, method='complete')
'''
method = 'complete' : default - 완전연결 
method = 'simple' : 단순연결
method = 'average' : 평균연결
'''
print(clusters)
clusters.shape # (149, 4)

# 3. 텐드로그램 시각화 : 군집수는 사용자가 결정 
plt.figure(figsize = (25, 10))
dendrogram(clusters)
plt.show()

# 4. 클러스터 자르기: 3개 클러스터링
from scipy.cluster.hierarchy import fcluster

re_clusters = fcluster(clusters, t=3, criterion='distance') 
# criterion='distance' ->거리기준으로 3개(t=3)의 군집을고 자른다 
print(re_clusters)
'''
[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 2 3 2 2 2 2 3 2 2 2 2
 3 2 3 3 2 2 2 2 3 2 3 2 3 2 2 3 3 2 2 2 2 2 3 3 2 2 2 3 2 2 2 3 2 2 2 3 2
 2 3]
'''

# 칼럼 추가
iris_df['clusters']=re_clusters
iris_df.columns

#산점도로 
plt.scatter(x=iris_df['sepal length (cm)'],
            y=iris_df['petal length (cm)'],
            c=iris_df['clusters'])
plt.show()

