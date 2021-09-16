#################################
## <제11장 연습문제>
################################# 

# 01. 다음 mtcars 데이터셋을 대상으로 연비효율(mpg), 실린더수(cyl), 엔진크기(disp), 마력(hp), 무게(wt) 변수를 
# 대상으로 서브셋을 작성하시오.
library(datasets)
data(mtcars)
str(mtcars)

df <- subset(mtcars, select = c(1:4,6)) # 5개 변수 선택 
head(df)


# 02. 작성된 서브셋을 대상으로 상관분석을 수행하여 연비효율(mpg)과 가장 상관계수가 
# 높은 변수를 확인하시오. 
Cor <- cor(df)
Cor # 상관계수 행렬 
Cor['mpg', ] # mpg 기준 -> wt : -0.8676594


# 03. 연비효율과 가장 상관계수가 높은 변수와 산점도로 시각화하시오.
plot(df$mpg, df$wt)

# 04. iris 데이터셋에서 5번째 칼럼을 제외한 4개의 칼럼으로 상관계수를 확인하시오.
# <단계1> 4개 칼럼 간의 상관계수 행렬 확인 
Cor <- cor(iris[-5])
Cor # 상관계수 행렬

# <단계2> 첫번째 칼럼(Sepal.Length) 기준으로 상관계수 확인 
Cor['Sepal.Length', ]

# <단계3> 양의 상관계수가 가장 큰 두 변수 산점도 시각화  
plot(iris$Petal.Length, iris$Petal.Width)

# <단계4> 음의 상관계수가 가장 낮은 두 변수 산점도 시각화 
plot(iris$Sepal.Length, iris$Sepal.Width)








