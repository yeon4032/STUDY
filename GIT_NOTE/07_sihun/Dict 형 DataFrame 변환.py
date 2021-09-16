# -*- coding: utf-8 -*-
"""
사전을 Pandas DataFame로 변환하는 방법
"""

# python 3.x
import pandas as pd

fruit_dict = {
    3: 'apple',
    2: 'banana',
    6:'mango',
    4:'apricot',
    1:'kiwi',
    8:'orange'}

print(pd.DataFrame(list(fruit_dict.items()),
                   columns=['Quantity', 'FruitName']))
'''
   Quantity FruitName
0         3     apple
1         2    banana
2         6     mango
3         4   apricot
4         1      kiwi
5         8    orange
'''


print(pd.DataFrame([fruit_dict]))
'''
       3       2      6        4     1       8
0  apple  banana  mango  apricot  kiwi  orange
'''


data = {
    '1':{
        'apple':11, 
        'banana':18}, 
    '2':{
        'apple':16, 
        'banana':12}
}
df = pd.concat({k: pd.Series(v) for k, v in data.items()}).reset_index()
df.columns = ['dict_index', 'name','quantity']
print(df)
'''
  dict_index    name  quantity
0          1   apple        11
1          1  banana        18
2          2   apple        16
3          2  banana        12
'''





















