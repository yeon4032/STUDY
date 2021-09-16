install.packages("forecast")
install.packages("torecast")
install.packages("mFilter")

library(urca)
library(vars)
library(mFilter)
library(tseries)
library(torecast) #안됨
library(tidyverse)
library(forecast)

#Load the Dataset

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

#Convert to Time Series Object

y<- ts(data_gdp$GDP, start=c(2000,1,1),frequency = 1)
x1<-ts(data_gdp$retail_index,start=c(2000,1,1),frequency = 1)
x2<-ts(data_gdp$employment,start=c(2000,1,1),frequency = 1)
x3<-ts(data_gdp$production_index,start=c(2000,1,1),frequency = 1)

#plot the Series
ts.plot(y)
ts.plot(x1)
ts.plot(x2)
ts.plot(x3)

#SVAR Retriction 

amat<- diag(4)
amat

amat[2,1]<-NA
amat[3,1]<-NA
amat[3,2]<-NA
amat[4,3]<-NA
amat
#elements in the lower triangular of the matrix
#are now an ace in essence
#I am allowing whatever the coefficents end up 
#being here to be free for them to be estimated in my system.
# so x1 can affect x2,x3 but x2 cannot affect x1 but can affet x3.

#build the Model
sv<-cbind(y,x1,x2,x3)
colnames(sv)<- cbind("OutputGap","retail","employment","production")

#Lag Order selection
lagselect<- VARselect(sv,lag.max=20,type="both")
lagselect$selection
# AIC(n)  HQ(n)  SC(n) FPE(n) 
# 3      3      3      2 

#Estimating the model
Model2<-VAR(sv,p = 3,season = NULL,exog=NULL, type="const")
SVARMod1<-SVAR(Model2,Amat=amat,Bmat=NULL,hessian=TRUE,estmethod = c("scoring","direct"))
SVARMod1

# VAR Estimation Results:
#   ======================== 
#   
#   
#   Estimated A matrix:
#             OutputGap retail employment production
# OutputGap    1.00000  0.000        0.0          0
# retail       0.05194  1.000        0.0          0
# employment  -0.62495  5.996        1.0          0
# production   0.00000  0.000        0.1          1


#impulse Response Functions
SVARog<- irf(SVARMod1,impulse = "OutputGap",response = "OutputGap" )
SVARog
plot(SVARog)

SVARretail<- irf(SVARMod1,impulse = "OutputGap",response = "retail" )
SVARretail
plot(SVARretail)





































