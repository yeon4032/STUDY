# chap03_DataIO

# 1. 데이터 불러오기

# 1) 키보드 입력 : 소량의 자료 
num <- scan() # 숫자 입력 
num
sum(num)

names <- scan(what = character())
names

name_doc = paste(names, collapse = ",") # str_c() 유사함 
name_doc


# 2) 파일 데이터 가져오기 
# - 칼럼 단위 구분 : csv, excel 

# (1) read.table() : 칼럼 구분(공백, 특수문자)
getwd() # "C:/ITWILL/2_Rwork/data"
setwd("C:/ITWILL/2_Rwork/data")
# 칼럼명 없는 경우 
st1 <- read.table('student.txt') # 제목 없음 
st1 # V1   V2  V3 V4 -> 기본 칼럼명 제공 

# 칼럼명 있는 경우 
st2 <- read.table('student1.txt', header = TRUE)
st2

# 구분자 : 특수문자 
st3 <- read.table('student2.txt', header = TRUE, sep = ";")
st3

# (2) read.csv() : 칼럼 구분(콤마)
# na.strings : 특수문자 -> NA
st4 <- read.csv('student4.txt', na.strings = c("&","-"))#, header = TRUE, sep = ",")
st4

str(st4)
mean(st4$'키', na.rm=TRUE) # 177.6667
mean(st4$'키')

# 탐색기 제공 
test <- read.csv(file = file.choose())


# (3) read.excel() : 패키지 설치 
install.packages('readxl') # 패키지 설치
library(readxl) # in memory
st_excel <- read_excel('studentexcel.xlsx') # excel 파일 열기 
st_excel


# 3) 인터넷 파일 불러오기 
# 데이터 셋 제공 사이트 
# http://www.public.iastate.edu/~hofmann/data_in_r_sortable.html - Datasets in R packages
# https://vincentarelbundock.github.io/Rdatasets/datasets.html
# https://r-dir.com/reference/datasets.html - Dataset site
# http://www.rdatamining.com/resources/data

titanic <- read.csv('https://vincentarelbundock.github.io/Rdatasets/csv/COUNT/titanic.csv')
str(titanic)
# 'data.frame':	1316 obs. of  5 variables:
# $ X       : int  1 2 3 4 5 6 7 8 9 10 ...
# 범주형 
# $ class   : chr  "1st class" "1st class" "1st class" "1st class" ...
# $ age     : chr  "adults" "adults" "adults" "adults" ...
# $ sex     : chr  "man" "man" "man" "man" ...
# $ survived: chr  "yes" "yes" "yes" "yes" ...

# 범주형 변수의 빈도수 
table(titanic$sex) # 성별 
#man women 
#869   447
titanic
table(titanic$survived) # 생존유무 
# no yes 
#817 499

# 교차분할표 
table(titanic$sex, titanic$survived) # (행, 열)
#       no yes
#man   694 175
#women 123 324

175 / (694 + 175) # 0.2013809
324 / (123 + 324) # 0.7248322


# 2. 데이터 저장(출력)하기

# 1) 화면 출력 

# 문자열 + 수식 or 변수 
cat("남성의 생존비율 =", 175 / (694 + 175))
# 남성의 생존비율 = 0.2013809

x <- 100
y <- 200
z = x + y
cat('z=', z)

# 변수 or 수식 
print(z)
print('z=', z) # error 
print(175 / (694 + 175))


# 2) 파일 데이터 저장 
# read.table() <-> write.table()
# read.csv() <-> write.csv()
# read_excel() <-> write_xlsx()

# (1) write.csv()
str(titanic)
titanic_df <- subset(titanic, select = c(class, sex, survived) )

write.csv(titanic_df, 'titanic.csv', row.names = FALSE,
          quote = FALSE)

# (2) write_xlsx()
install.packages('writexl')
library(writexl)
write_xlsx(st_excel, path = 'student_ex.xlsx')




