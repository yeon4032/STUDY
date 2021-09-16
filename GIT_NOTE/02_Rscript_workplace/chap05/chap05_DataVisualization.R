# chap05_DataVisualization 

# 1. 이산형 변수 시각화 
# - 정수 단위로 나누어지는 변수(자녀수, 판매수)

# 차트 데이터 생성
chart_data <- c(305,450, 320, 460, 330, 480, 380, 520) 
names(chart_data) <- c("2016 1분기","2017 1분기","2016 2분기","2017 2분기","2016 3분기","2017 3분기","2016 4분기","2017 4분기")
str(chart_data)
chart_data
max(chart_data) # 520
length(chart_data) # 8

# 1) 막대차트 

# (1) 세로막대차트 
help("barplot")

barplot(chart_data, ylim = c(0, 600),
        col = rainbow(8), 
        ylab = '매출액(단위:천원)', 
        xlab = "년도별 분기현황",
        main ="2016년 vs 2017년 분기별 매출현황")


# (2) 가로막대차트 : horiz = TRUE
barplot(chart_data, xlim = c(0, 600),
        horiz = TRUE, 
        col = rainbow(8), 
        ylab = '년도별 분기현황', 
        xlab = "매출액(단위:천원)",
        main ="2016년 vs 2017년 분기별 매출현황")

# [범례] 추가 
barplot(chart_data, ylim = c(0, 600),
        col = rainbow(8), 
        ylab = '매출액(단위:천원)', 
        xlab = "년도별 분기현황",
        main ="2016년 vs 2017년 분기별 매출현황",
        legend.text = names(chart_data),
        args.legend = list(x = 'topleft'))

# [text] 추가 
bp <- barplot(chart_data, ylim = c(0, 600),
        col = rainbow(8), 
        ylab = '매출액(단위:천원)', 
        xlab = "년도별 분기현황",
        main ="2016년 vs 2017년 분기별 매출현황")
# text 반영 
text(x = bp, y = chart_data + 20,
     labels = chart_data, col = "black", cex = 0.7)

# 1행 2열 차트 그리기
par(mfrow=c(1,2)) # 1행 2열 그래프 보기

VADeaths # 시골 vs 도시 출신 사망비율 
str(VADeaths) # num [1:5, 1:4]

# 왼쪽 : 개별막대 
barplot(VADeaths, beside=T,col=rainbow(5),
        main="미국 버지니아주 하위계층 사망비율")
legend(19, 71, c("50-54","55-59","60-64","65-69","70-74"), cex=0.8,
       fill=rainbow(5))

# 오른쪽 : 누적형 막대 
barplot(VADeaths, beside=F,col=rainbow(5),
        main="미국 버지니아주 하위계층 사망비율")

# 2) 점 차트 
help("dotchart")
par(mfrow=c(1,1))
dotchart(chart_data, color=c("green","red"), lcolor="black",
         pch=1:2, labels=names(chart_data), xlab="매출액",
         main="분기별 판매현황 점 차트 시각화", cex=1.2)

# 3) 파이 차트 : 비율(점유율) 시각화에 유용 
pie(chart_data, labels = names(chart_data), 
    border = 'blue', col = rainbow(8), cex=1.2)

title("분기별 판매현황", cex.main = 2)

# 파이 차트 주의사항 : 중복응답 반영 안됨(비율 제공)
genre <- c(45, 25, 15, 30) # 100명 
sum(genre) # 115
names(genre) <- c("액션", "스릴러", "공포", "드라마")

genre

pie(genre, labels = names(genre), col = rainbow(4))


rate = round(genre / sum(genre) * 100, 2)
rate

labels = names(genre)
labels = paste(labels,'\n', rate) # 레이블, 줄바꿈, 비율 
# 문자열 결합 : paste()함수 

# 비율 적용 
pie(genre, labels = labels, col = rainbow(4))


# 2. 연속형 변수 시각화 
# - 연속된 값(실수값)을 갖는 변수(시간, 길이, 몸무게 등)

# 1) 상자그래프 
# - 요약통계 정보 -> 시각화 도구 
# - 요약통계(분석기사) : 사분위수(중위수), 최솟값, 최댓값, 이상치 

VADeaths
summary(VADeaths) # Min, 사위분위수, Mean, Max
boxplot(VADeaths)

# 사분위수 
VADeaths[,1] # Rural Male
quantile(VADeaths[,1])
#0%=min  25%  50%  75% 100%=max 
#11.7 18.1 26.9 41.0 66.0

# 2) 히스토그램 : 각 계급의 빈도수 
iris
str(iris) # 붗꽃 
#'data.frame':	150 obs. of  5 variables:
#$ Sepal.Length: 꽃받침 길이 num  5.1 4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 ...
#$ Sepal.Width : 꽃받침 넓이 num  3.5 3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 ...
#$ Petal.Length: 꽃잎 길이 num  1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 ...
#$ Petal.Width : 꽃잎 넓이 num  0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 ...
#$ Species     : Factor w/ 3 levels "setosa","versicolor"

table(iris$Species)

range(iris$Sepal.Length) # 4.3 7.9

# (1) 일반 히스토그램 
hist(iris$Sepal.Length, xlab = '꽃받침 길이', 
     main = '붗꽃 꽃받침 길이')

# (2) 계급수 조정 
hist(iris$Sepal.Length, xlab = '꽃받침 길이',
     breaks = 30,
     main = '붗꽃 꽃받침 길이')

# (3) 확률밀도함수(pdf) : 확률변수 X의 크기를 계산하는 함수(추정)
# step1 : 밀도 단위 변경 
hist(iris$Sepal.Width, xlab = '꽃받침 넓이',
     breaks = 30, freq = FALSE,
     main = '붗꽃 꽃받침 넓이')

# setp2 : 확률밀도함수(pdf) -> 확률밀도 추정 -> 곡선 
lines(density(iris$Sepal.Width), col='red')

# (4) 정규분포 곡선 : dnorm -> 정규분포 추정 -> 곡선
range(iris$Sepal.Width) # 2.0 4.4

x <- seq(2.0, 4.4, 0.1)
x
curve(dnorm(x, mean = mean(iris$Sepal.Width), 
            sd = sd(iris$Sepal.Width)), col='blue', add = T)

# 3) 산점도 
plot(x=iris$Sepal.Length, y=iris$Petal.Length) # (x, y)
plot(iris$Petal.Length ~ iris$Sepal.Length) # (y ~ x)

price <- runif(100, min = 1, max = 100) # 1~100 난수 100개개
price

plot(price) # x : index, y : price값 

par(mfrow=c(2,2)) # 2행 2열 차트 그리기
# plot() 함수 속성 : pch : 연결점 문자타입-> plotting characher-번호(1~30)
plot(price, type="o", pch=5) # 빈 사각형
plot(price, type="o", pch=15)# 채워진 마름모
plot(price, type="o", pch=20, col="blue") #color 지정
plot(price, type="o", pch=20, col="orange", cex=1.5) #character expension(확대)

# 만능차트 
methods(plot)

# 1) 시계열 data -> 추세선 
WWWusage

plot(WWWusage)

# 2) 회귀모델 -> 관련 차트 
plot(iris$Petal.Length ~ iris$Sepal.Length) # (y ~ x) 
model <- lm(iris$Petal.Length ~ iris$Sepal.Length) # 종속변수(y) ~ 독립변수(x)
abline(model, col='red')

plot(model) # 회귀모델 관련 차트


# plot 2개 겹치기 
plot(iris$Sepal.Length, type = 'o', ann = FALSE, col='blue')
# ann = FALSE : 축이름 제외 
par(new = T) # 그래프 겹치기 
plot(iris$Petal.Length, type = 'o', axes = FALSE, ann = FALSE,
     col='red')
# axes = FALSE : 축 눈금 제외 

# 범례추가 
legend(x=0, y=7, legend = c("꽃받침 길이", "꽃잎의 길이"),
       col = c('blue', 'red'), lty = 1)


# 4) 산점도 행렬(scatter matrix) : 변수 비교 
pairs(iris[,1:4])

table(iris$Species)
#setosa versicolor  virginica 
# 50         50         50 

# 꽃의 종별 산점도 
pairs(iris[iris$Species=="setosa",1:4]) # [row,col]
pairs(iris[iris$Species=="versicolor",1:4])
pairs(iris[iris$Species=="virginica",1:4])


# 5) 차트 파일 저장 
getwd()
setwd("C:/ITWILL/2_Rwork/output")

jpeg("iris.jpg", width = 720, height = 480) # open
pairs(iris[,1:4]) # 차트 
dev.off() # close

plot(iris$Sepal.Length, iris$Petal.Length, col=iris$Species)


#########################
### 3차원 산점도 
#########################
install.packages('scatterplot3d')
library(scatterplot3d)

# 꽃의 종류별 분류 
iris_setosa = iris[iris$Species == 'setosa',]
iris_versicolor = iris[iris$Species == 'versicolor',]
iris_virginica = iris[iris$Species == 'virginica',]

# scatterplot3d(밑변, 오른쪽변, 왼쪽변, type='n') # type='n' : 기본 산점도 제외 
d3 <- scatterplot3d(iris$Petal.Length, iris$Sepal.Length, iris$Sepal.Width, type='n')

d3$points3d(iris_setosa$Petal.Length, iris_setosa$Sepal.Length,
            iris_setosa$Sepal.Width, bg='orange', pch=21)

d3$points3d(iris_versicolor$Petal.Length, iris_versicolor$Sepal.Length,
            iris_versicolor$Sepal.Width, bg='blue', pch=23)

d3$points3d(iris_virginica$Petal.Length, iris_virginica$Sepal.Length,
            iris_virginica$Sepal.Width, bg='green', pch=25)







