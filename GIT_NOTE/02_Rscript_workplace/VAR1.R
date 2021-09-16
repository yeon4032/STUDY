
install.packages("forecast")

library(urca)
library(vars)
library(mFilter)
library(tseries)
library(torecast)
library(tidyverse)
library(forecast)
#Load the Dataset
install.packages("readxl")
library(readxl)
data_gdp<-read_excel("V.xlsx")
data_gdp
data_gdp=as.data.frame(read_excel("V.xlsx",col_names=c("year","GDP","GDP_growth",
                                                          "retail_index","employment"
                                                          ,"production_index")))
data_gdp

data_gdp<-data_gdp[-1,]
data_gdp
str(data_gdp)
data_gdp$retail_index<-as.numeric(data_gdp$retail_index)
data_gdp$GDP<-as.numeric(data_gdp$GDP)
data_gdp$GDP_growth<-as.numeric(data_gdp$GDP_growth)
data_gdp$employment<-as.numeric(data_gdp$employment)
data_gdp$production_index<-as.numeric(data_gdp$production_index)
str(data_gdp)

#A simple graph
ggplot(data=data_gdp)+geom_point(mapping-aes(x=data_gdp$`소매판매액 지수`,y=data_gdp$비농림취업지수))

#Declare our Time Series Variables
gdp<-ts(data_gdp$GDP,start=c(2000,1),frequency = 1)
retail_index<-ts(data_gdp$retail_index,start=c(2000,1),frequency = 1)
empl<-ts(data_gdp$employment,start=c(2000,1),frequency = 1)
pro_index<-ts(data_gdp$production_index,start=c(2000,1),frequency = 1)

#plot the series
outoplot(cbind(gdp,retail_index,empl,pro_index))

#OLS 
ols1<-lm(gdp ~ retail_index,data=data_gdp)
summary(ols1)

#Determine the persistence of the model 

acf(gdp,main= "ACF for REal GDP")
pacf(gdp, main= "PACF for real GDP")

acf(retail,main= "ACF for retail")
pacf(retail, main= "PACF for retail")

acf(empl,main= "ACF for employment")
pacf(empl, main= "PACF for employment")

acf(pro_index,main= "ACF for production")
pacf(pro_index, main= "PACF for production")

#Finding the Optimal Lags

op.bv<-cbind(gdp,retail_index,empl,pro_index)
colnames(op.bv)<-cbind("GDP","retail_index","employment"
                       ,"production_index")

lagselect<-VARselect(op.bv,lag.max =10,type="const")
lagselect$selection
# AIC(n)  HQ(n)  SC(n) FPE(n) 
# 3      3      3      2 

#craete model VAR

model1<-VAR(op.bv,p=3, type = "const",season=NULL, exog=NULL)
summary(model1)

#Diagnosing the VAR

#serial Correlation

serial1<- serial.test(model1,lags.pt = 12, type="PT.asymptotic")
serial1

#Heteroscedasticity
Arch1<-arch.test(model1,lags.multi = 3,multivariate.only = TRUE)
Arch1

#Normal Distribution of the residuals

Norm1<- normality.test(model1,multivariate.only = TRUE)
Norm1


#Testing for Structural Breaks in the Residuals

stability1<- stability(model1,type="OLS-CUSUM")
plot(stability1)
#any line from four graphs are exceed the red line. 
#Hence, the system is stable. 

#Granger causality

GranGDP<- causality(model1,cause= "GDP")
GranGDP
$Granger

# Granger causality H0: GDP do not Granger-cause
# retail_index employment production_index
# 
# data:  VAR object model1
# F-Test = 2.1896, df1 = 9, df2 = 20, p-value = 0.06932
# 
# 
# $Instant
# 
# H0: No instantaneous causality between: GDP and
# retail_index employment production_index
# 
# data:  VAR object model1
# Chi-squared = 8.3935, df = 3, p-value = 0.03854

Granemployment<- causality(model1,cause= "GDP")

#Impulse Response Function

GDPirf<- irf(model1,impulse = "employment",response = "GDP",n.ahead = 20, boot=TRUE)
plot(GDPirf,ylab="GDP", Mian= "shock from Unemployment")



#variance Decomposition

FEVD1<- fevd(model1,n.ahead=10)
plot(FEVD1)


#VAR Forecasting
forecast<-predict(model1,n.ahead=4,ci=0.95)
fanchart(forecast)
fanchart(forecast,names="GDP")

