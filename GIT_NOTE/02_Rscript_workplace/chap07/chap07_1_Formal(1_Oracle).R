# chap07_1_Formal(1_Oracle)

########################################
## Chapter07-1. 정형데이터 처리 
########################################


# 1. JDK & JRE 설치 : RJDBC 패키지를 사용하기 위해서는 java 설치
######################################
## JDK & JRE 설치 
######################################
#http://naver.em/5mYw2sRZ
# DB 자료 활용: SQL+R 패키지 +시각화 도구 


# 2. 패키지 설치
#
install.packages("rJava") # 기존 설치된 패키지 
install.packages("DBI") #DB interface
install.packages("RJDBC")# R+DB연동 (rjava 의존성)


# 3. 패키지 로딩
library(DBI) #dbGetQuery ()
Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jdk1.8.0_151')
library(rJava)
library(RJDBC) # rJava에 의존적


# 4. Oracle 연동   
######################## Oracle 11g ####################################
# 단계1: driver 객체 
drv<-JDBC(driverClass="oracle.jdbc.driver.OracleDriver", 
          classPath="C:\\oraclexe\\app\\oracle\\product\\11.2.0\\server\\jdbc\\lib\\ojdbc6.jar")

# 단계2:  db연동(driver, url, user, password) 
conn <- dbConnect(drv=drv, 
                  url="jdbc:oracle:thin:@//127.0.0.1:1521/xe",
                  user="scott", 
                  password="tiger")

# url="jdbc:oracle:thin:@//127.0.0.1:1521/xe", #orcale 이 설치된 url의미
# 127.0.0.1 기본 url, 1521(포트번호), xe(db 이름) 등이 조합되어 만들어집니다.

######################################################################


#1.전체 테이블 조회

query<-"select*from tab"
dbGetQuery(conn,query) # conn 은
#dbGetQuery(db연동, 명령문)
#DB연동 객체, 명령문


#2. Table 생성
query<- "create table db_test(sid int, pwd char(4),
          name varchar(25),age int)"
#table 명이 DB_test

dbSendUpdate(conn,query) #table 생성

dbGetQuery(conn,"select*from tab") #table 조회



dbGetQuery(conn,"select*from DB_TEST") # SID  PWD  NAME AGE (table 컬럼과 내용 조회) 


#3. db내용 수정: dbsendupdate(conn,query문)

#1) insert 문
query<-"insert into DB_TEST values(1001,'1234','홍길동',35)"

dbSendUpdate(conn,query)

#2)update문
query<- "update DB_TEST set name = '김길동' where sid =1001"
dbSendUpdate(conn,query)

dbGetQuery(conn,"select*from DB_TEST") #table 조회


#3)delete 문
dbSendUpdate(conn,"delete from DB_TEST where sid=1001")

dbGetQuery(conn,"select*from DB_TEST") #table 조회

# ID  PWD  NAME AGE 
# <0 행> <또는 row.names의 길이가 0입니다

#4. table삭제
dbSendUpdate(conn,"drop table DB_TEST purge")

dbGetQuery(conn,"select*from tab") #목록에서 DB_TEST 사라짐




#5. table 불러오기
query<-"select*from emp"
emp<-dbGetQuery(conn,query) #DB(table)-> object of R

str(emp)
# 'data.frame':	14 obs. of  8 variables:

#통계함수
mean(emp$SAL) # 2073.214
mean(emp$COMM) #결측지 때문에 NA 나옴
mean(emp$COMM, na.rm= T) #550

summary(emp) #전채 컬럼에 대한 요약 통계

#조건식
query<-"select *from emp where sal>=2500 and job ='MANAGER'"
manager_2500<-dbGetQuery(conn,query)

manager_2500
#   EMPNO ENAME   JOB    MGR     HIREDATE         SAL COMM DEPTNO
# 1  7566 JONES MANAGER 7839 1981-04-02 00:00:00 2975   NA     20
# 2  7698 BLAKE MANAGER 7839 1981-05-01 00:00:00 2850   NA     30

#subquery
#부서='SALES' 인 저체 사원의 이름, 급여 직책 조회
#sub:DEPT, Main: EMP
dbGetQuery(conn,"select *from DEPT")

query<-"select ename,sal,job from EMP where  DEPTNO = (select DEPTNO from DEPT where DNAME='SALES')"

sales<-dbGetQuery(conn,query)
sales


#join
query<- "select e.ename,e.job,d.dname,d.*
          from EMP e,DEPT d
          where e.deptno=d.deptno and e.ename like '%M%'"
join_df<- dbGetQuery(conn,query)
join_df


# 저체 사원의 급연 정보 -> 막대차트로 시각화
length(emp$SAL)
barplot(emp$SAL,col=rainbow(length(emp$SAL)),
        main='전체 사원의 급여 정보',
        names.arg=emp$ENAME)

#names.arg :X축 눈금 지정


#집계함수 이용:각 부서별 급여 평균, 합계 

query<-"select deptno, avg(sal), avg_sal, sum(sal) sum_sal
        from emp
        group by DEPTNO
        order by deptno"

result<-dbGetQuery(conn,query)
result


# db연결 종료
dbDisconnect(conn) #TRUE means db 가 종료됨