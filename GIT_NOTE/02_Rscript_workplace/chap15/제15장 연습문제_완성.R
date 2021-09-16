#################################
## <제15장 연습문제>
################################# 

# 01. 다음은 15명의 면접자를 대상으로 가치관, 전문지식, 자격증 유무 등을 토대로 
#  종합점수에 근거하여 합격여부를 결정한 자료이다. 다음과 같은 단계로 계층적 
#  군집분석을 수행하여 군집수(cluster)를 탐색하고, 각 군집별로 서브셋을 작성하여 
#  각 군집의 특성을 분석하시오.

# 단계1 : dataset 가져오기 
interview <- read.csv("c:/Rwork/data/interview.csv")
names(interview)
head(interview)

# 단계2 : 유클리디안 거리 계산  
inter_df <- interview[c(2:8)] # 응시번호와 합격여부 제외
idist <- dist(inter_df) # 유클리디안 거리 생성 
head(idist)


# 단계3 : 계층적 군집분석 & 덴드로그램 시각화 
hc <- hclust(idist)
hc

plot(hc, hang=-1) # 음수값 제외


# 단계4 : 군집별 서브셋 만들기 : cutree()함수 이용 
ghc <- cutree(hc, k=3)
inter_df$ghc <- ghc
inter_df
g1 <- subset(inter_df, ghc==1)
g2 <- subset(inter_df, ghc==2)
g3 <- subset(inter_df, ghc==3)


# 단계5 : 각 군집별 특성 분석 : summary()함수 이용 
summary(g1) # 자격증 : 1,       Mean   :19   Mean   :14.4   Mean   :15.6   Mean   :14.8  Mean   :11.8  Mean   :75.6
summary(g2) # 자격증 : 0 or 1,  Mean   :11   Mean   :15.2   Mean   :19.4   Mean   :11,   Mean   :6.2   Mean   :62.8
summary(g3) # 자격증 : 0,       Mean   :14.4 Mean   :18.8   Mean   :10.8   Mean   : 9.4, Mean   :18.2  Mean   :71.6





# 02. 다음과 같은 조건을 이용하여 각 단계별로 비계층적 군집분석을 수행하시오.

# 조건1) 대상 파일 : c:/Rwork/Part-IV/product_sales.csv
# 조건2) 변수 설명 : tot_price : 총구매액, buy_count : 구매횟수, 
#                    visit_count : 매장방문횟수, avg_price : 평균구매액

sales <- read.csv("c:/Rwork/Part-IV/product_sales.csv", header=TRUE)
head(sales) 


# 단계1: 비계층적 군집분석 : 3개 군집으로 군집화
model <- kmeans(sales,3) # kmeans(data, k) : k개수: 군집수
model # 원형데이터를 대상으로 3개 군집으로 군집화

# 각 케이스에 대한 소속 군집수(1,2,3) 확인
model$cluster # 각 케이스에 대한 소속 군집수(1,2,3)

# 단계2: 원형데이터에 군집수 추가
sales$group <- model$cluster
head(sales)# group 추가

# 단계3 : tot_price 변수와 가장 상관계수가 높은 변수와 군집분석 시각화
# (1) 상관관계 분석 
cor(sales[,-5], method="pearson")
# <해설> tot_price에 가장 큰 영향을 미치는 변수는 avg_price

# (2) 비계층적 군집분석 시각화 : 그룹으로 색상 표시 
plot(sales[c("tot_price", "avg_price")], col=sales$group)

# 단계4. 군집의 중심점 표시
points(result2$centers[,c("tot_price", "avg_price")], col=1:3, pch=8, cex=2)
