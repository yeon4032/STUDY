'''
 문4) tot 함수를 인수로 받아서 dataset 각 원소의 합을 계산하는 함수를 완성하시오.

  <출력 결과>
  tot = [12.5, 7, 22.3]
'''

def tot(x):
    return sum(x)

def my_func(func, dataset):
    re=[]
    for x in dataset:
        re.append(func(x))
    return re


# dataset
dataset = [[2,4.5,6], [3,4], [5,8.3,9]]

result = my_func(tot,dataset)
print(result)



def tot(x):
    return sum(x)

def my_func(func, dataset):
    re1 = [func(x) for x in datas]
    return re1
    
    
    
    
# dataset
dataset = [[2,4.5,6], [3,4], [5,8.3,9]]

tot=my_func(tot, dataset)
print('tot=',tot)