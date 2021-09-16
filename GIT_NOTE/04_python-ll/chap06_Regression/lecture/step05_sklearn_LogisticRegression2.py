# -*- coding: utf-8 -*-
"""
step05_sklearn_LogisticRegression2.py

- multi class classification
"""
from sklearn.datasets import load_digits # dataset
from sklearn.linear_model import LogisticRegression # model
from sklearn.model_selection import train_test_split #dataset split
from sklearn.metrics import confusion_matrix, accuracy_score # model 평가 도구

#1. dataset loading
digits = load_digits()
digits

image = digits.data# x변수
label = digits.target # y변수

image.shape # (1797, 64) -> (1797,8,8):이미지 pixel
label.shape # (1797,): 10진수 정답
label # array([0, 1, 2, ..., 8, 9, 8])

# train_test_split
img_train,img_test,lab_train,lab_test=train_test_split(image,label,
                                               test_size=0.3,
                                               random_state=123)

#3. model 생성
lr=LogisticRegression(random_state=123, 
                   solver='lbfgs',
                   max_iter=200, 
                   multi_class='multinomial')

model = lr.fit(X=img_train,y=lab_train)

#4. model 평가
y_pred=model.predict(img_test)

con_mat = confusion_matrix(lab_test,y_pred)
con_mat

score=accuracy_score(lab_test, y_pred)
score#0.9666666666666667

print(lab_test)
print(y_pred)

re=[]
for i in range(len(lab_test)): # 0-539
    if lab_test[i] != y_pred[i]:
        re.append(i)
print(re) 
# [25, 46, 49, 66, 79, 98, 167, 200, 269, 276, 277, 369, 424, 428, 431, 457, 475, 530] 
len(re) # 18

#시각화
import matplotlib.pyplot as plt
#첫번째 오차
image[25]
x=image[25].reshape(8,8)
plt.imshow(x)
plt.show()

label[25] #5

import seaborn as sn # heatmap
# confusion matrix heatmap 
plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_mat, annot=True, fmt=".3f", linewidths=.5, square = True);# , cmap = 'Blues_r' : map »ö»ó 
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = f'Accuracy Score: {score}'
plt.title(all_sample_title, size = 18)
plt.show()

















