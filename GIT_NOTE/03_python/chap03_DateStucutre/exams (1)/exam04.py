'''
step05 문제

문2) price에는 과일 가게에 진열된 과일과 가격이 저장되어 있고,
    buy는 고객이 구매한 장바구니이다.

    조건>  [list + for] 형식을 적용하여 구매 상품 총 금액(tot_bill)을 계산하시오.

<출력 결과>
총 금액 : 18,500
'''

# 과일가게 진열 상품
price = {'사과':2000, '복숭아' : 3000, '딸기' : 2500}

# 구매 상품
buy = {'사과' : 3, '딸기' : 5}

# 구매 상품 총 금액

bill= [price[k]*buy[k] for k in buy]
print(bill)
print('총 금액 : {0:3,d}'.format(sum(bill)))
