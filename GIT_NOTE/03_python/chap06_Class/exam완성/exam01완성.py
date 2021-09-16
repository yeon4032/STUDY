'''
 문1) 다음 처리조건에 맞게 Rectangle 클래스를 정의하시오.
 <처리조건>
 1. 멤버 변수 : 가로(width), 세로(height)
 2. 생성자 : 가로(width), 세로(height) 멤버 변수 초기화
 3. 멤버 메서드(area_calc) : 사각형의 넓이를 구하는 메서드
          사각형 넓이 = 가로 * 세로 
 4. 멤버 메서드(circum_calc) : 사각형의 둘레를 구하는 메서드
          사각형 둘레 = (가로 + 세로) * 2
 5. 기타 출력 예시 참조
   
 
    
     << 출력 예시 >>       
 사각형의 넓이와 둘레를 계산합니다.
 사각형의 가로 입력 : 10
 사각형의 세로 입력 : 5
 ------------------------------------
 사각형의 넓이 : 50
 사각형의 둘레 : 30
 ------------------------------------
'''
# 1. 클래스 설계 
class Rectangle :
    # 멤버 변수(전역변수) : data 생성 
    width = 0
    height = 0
    
    # 생성자 : 객체 생성 + 멤버 변수 초기화 
    def __init__(self, w, h) :
        self.width = w
        self.height = h
    
    # 멤버 메서드 : data 처리 
    def area_calc(self) :
        re = self.width * self.height
        return re
    
    def circum_calc(self) :
        re = (self.width + self.height) * 2
        return re
        

# 키보드 입력 
print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input('사각형의 가로 입력 : '))
h = int(input('사각형의 세로 입력 : '))

# 2. 객체 생성 : 생성자 이용 
obj = Rectangle(w, h)

# object.method()
print('사각형의 넓이 :', obj.area_calc())
print('사각형의 둘레 :', obj.circum_calc())

















