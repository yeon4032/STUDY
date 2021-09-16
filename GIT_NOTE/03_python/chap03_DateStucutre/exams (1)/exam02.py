'''
step02 문제

문1) message에서 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
      <조건> list + for 형식1) 적용   
      
  <출력결과>      
[1, 0, 1, 0, 1]   


문2) message에서 'spam' 원소만 추출하여 spam_list에 추가하시오.
      <조건> list + for + if 형식2) 적용   
      
  <출력결과>      
['spam', 'spam', 'spam']   

'''

message = ['spam', 'ham', 'spam', 'ham', 'spam']
dum=[1 if i == 'spam' else 0 for i in message]
print(dum)


dum2=['spam' for x in message if x=='spam']
print(dum2)


#문제1
message = ['spam', 'ham', 'spam', 'ham', 'spam']
dummy=[0 if i=='ham'else 1 for i in message]
print(dummy)


#문제2
message = ['spam', 'ham', 'spam', 'ham', 'spam']
spam_list= [ words for words in message if words=='spam']
print(spam_list)
            
