# chap06_2_Data_Sampling

# 1. sample(n, size)
sample(x=10:20, size=5, replace = FALSE) # 20 11 10 15 14

sample(c(10:20, 30:40), 10) # 35 16 13 12 34 20 31 19 30 38

# 2. up/down 샘플링  
# - 복원추출 방식 y변수의 비율을 맞추는 샘플링 방식 

install.packages('caret')
library(caret)

getwd()
weather <- read.csv('weather.csv')
dim(weather) # 366  15
str(weather) # $ RainTomorrow : chr -> Y
table(weather$RainTomorrow)
# No Yes 
# 300 66

300 / (300+66) # 0.8196721
300 / nrow(weather)

# y변수 요인형 변경 
weather$RainTomorrow <- as.factor(weather$RainTomorrow)
str(weather) # $ RainTomorrow : Factor


# y변수 제외 
weather_df <- subset(weather, select = -RainTomorrow)
dim(weather_df) # 366  14

# Up sample
up_weather <- upSample(weather_df, weather$RainTomorrow)
str(up_weather) # 600

table(up_weather$Class)
# No Yes 
# 300 300 

# 칼럼명 추출 
cols <- names(up_weather)
cols

# 칼러명 변경 
cols[15] <- 'RainTomorrow'
names(up_weather) <- cols
head(up_weather)


# Down sample
down_weather <- downSample(weather_df, weather$RainTomorrow)
str(down_weather) # 132 obs

table(down_weather$Class)
#No Yes 
#66  66









