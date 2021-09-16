'''
step02 관련 문제

문) 다음과 같이 아메리카노 3잔만 제공하는 커피 자판기를 구현하시오.
     (커피 한 잔은 2500원이라고 가정한다.)
     조건1> 2500원 미만, 금액이 부족합니다. 반복 수행
     조건2> 2500원 이상, 맛있게 드세요. 잔돈 표시, 커피 잔 빼기
     조건3> 2500원 이면, 맛있게 드세오. 커피 잔 빼기
     조건4> 커피 3잔을 모두 판매하면 프로그램 종료
'''

print("==" * 15)   
print('아메리카노 커피 자판기 동작')
print('가격은 2,500원')
print('커피는 3잔만 판매 가능')
print("==" * 15)

coffee = 3 # 커피 3잔

while True: # 무한 반복
    payment=int(input('투입금액:'))
    
    if payment>=2500:
        print('맛있게 드세요, 잔돈은 {}입니다.'.format(payment-2500))
        coffee-=1
        print('남은커피는 {}'.format(coffee))
    else :
        print('금액이 부족합니다.')
        continue

    if coffee == 0: # 종료 조건
        print('~~ 장사 끝 ~~')
        break





print("==" * 15)   
print('아메리카노 커피 자판기 동작')
print('가격은 2,500원')
print('커피는 3잔만 판매 가능')
print("==" * 15)

coffee = 3 # 커피 3잔

while True: # 무한 반복

    if coffee == 0: # 종료 조건
        print('~~ 장사 끝 ~~')
        break

com=2500
coffee = 3
while True:
    cnt=1
    coin=int(input('지불할금액:'))
    coffee=coffee-cnt
    if coffee == 0: # 종료 조건
        print('남은 커피는 {0:1,d}잔 입니다'.format(coffee))
        print('커피 맛있게 드세요. 잔돈 {0:4,d}원 받으세요.'.format(coin-com))
        print('~~ 장사 끝 ~~')
        break
    
    elif coin>com:
        print('커피 맛있게 드세요. 잔돈 {0:4,d}원 받으세요.'.format(coin-com))
        print('남은 커피는 {0:1,d}잔 입니다'.format(coffee))
    
    elif coin==com:
        print('커피 맛있게 드세요')
        print('남은 커피는 {0:1,d}잔 입니다'.format(coffee))
    else:
        coffee+=1
        print('돈을 더넣어 주세요')
        
'''
    문) 다음과 같이 아메리카노 3잔만 제공하는 커피 자판기를 구현하시오.
     (커피 한 잔은 2500원이라고 가정한다.)
     조건1> 2500원 미만, 금액이 부족합니다. 반복 수행
     조건2> 2500원 이상, 맛있게 드세요. 잔돈 표시, 커피 잔 빼기
     조건3> 2500원 이면, 맛있게 드세오. 커피 잔 빼기
     조건4> 커피 3잔을 모두 판매하면 프로그램 종료
'''  

print("==" * 15)   
print('아메리카노 커피 자판기 동작')
print('가격은 2,500원')
print('커피는 3잔만 판매 가능')
print("==" * 15)

coffee = 3 # 커피 3잔

while True: # 무한 반복
    price=int(input('지불할금액:'))
    if price>2500:
        print('맛읶게 드세요.')
        print('잔돈은 %d 입니다.'%(price-2500))
        coffee -=1
        print('커피는 %d잔 남았습니다.'%coffee)
    elif price<2500:
        print('금액이 부족합니다.')
    
    elif price ==2500:
        print('맛읶게 드세요.')
        coffee-=1
        print('커피는 %d잔 남았습니다.'%coffee)
    
    if coffee == 0: # 종료 조건
        print('~~ 장사 끝 ~~')
        break
    




























    
    
    
    