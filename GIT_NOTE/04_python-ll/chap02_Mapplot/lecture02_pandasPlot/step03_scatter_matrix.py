# -*- coding: utf-8 -*-
"""
 - 산점도 행렬과 3차원 산점도 
"""

import pandas as pd # object
import matplotlib.pyplot as plt # chart
import os

os.chdir('C:/ITWILL/4_python-ll/data')


# 1. 산점도 행렬 
from pandas.plotting import scatter_matrix

# 3) iris.csv
iris = pd.read_csv('iris.csv')
cols = list(iris.columns)

x = iris[cols[:4]]
print(x.head())

# 산점도 matrix 
scatter_matrix(x)
plt.show()


# 2. 3차원 산점도 
from mpl_toolkits.mplot3d import Axes3D # 3d 그래프 사용시 필요 라이브러리

col_x = iris[cols[0]]
col_y = iris[cols[1]]
col_z = iris[cols[2]]

cdata=[] # color data
for s in iris[cols[-1]]: #Species
    if s == 'setosa':
        cdata.append(1)
    elif s =='versicolor':
        cdata.append(2)
    else:
        cdata.append(3)


fig = plt.figure()
chart = fig.add_subplot(projection='3d') # projection='3d'-> 3d 형의 산점도 제공

chart.scatter(col_x, col_y, col_z,c=cdata)
chart.set_xlabel('Sepal.Length')
chart.set_ylabel('Sepal.Width')
chart.set_zlabel('Petal.Length')
plt.show()






 
