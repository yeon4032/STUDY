#chap07_2_infromal
#################################
## <제7장-1 연습문제>
################################# 

# 01. 다음과 같은 단계를 통해서 테이블을 호출하고, SQL문을 이용하여 레코드를 조회하시오.
# (DBMS : Oracle 사용)

# [단계 1] 사원테이블(EMP)을 검색하여 결과를 EMP_DF로 변수로 불러오기
EMP_DF<- dbGetQuery(conn,"select *from EMP")
EMP_DF

# [단계 2] EMP_DF 변수를 대상으로 부서별 급여의 합계를 막대차트로 시각화(col)
# 부서별 급여 합계
query<-"select deptno, sum(SAL),avg(sal) from emp 
        group by deptno"

sum_dep<- dbGetQuery(conn,query)
sum_dep

# 부서명 받아오기
dept<-dbGetQuery(conn,"select *from dept")
dname<-dept$DNAME


# [단계 3] 막대차트를 대상으로 X축의 축눈금을 부서명으로 표시하기

barplot(sum_dep$`SUM(SAL)`,col = rainbow(3),names.arg = dname[1:3],main = "부서별 급여 합계")
help(barplot)

#  02. 'WARD' 사원의 상사(MGR)와 같은 사원이름, 직책, 연봉을 출력하시오.
# <조건1> Oracle 서브쿼리 이용
# <조건2> 차트 결과 참고  

query<- "select ename,job,sal,mgr from emp 
        where MGR=(select MGR from emp where ename='WARD')"

emp_MGR_WARD<-dbGetQuery(conn,query)
emp_MGR_WARD

pie(emp_MGR_WARD$SAL,labels = emp_MGR_WARD$ENAME, col=rainbow(5),
    main="WARD 사원의 상사와 같은 사원들의 급여")

pie(result$SAL, 
    labels = result$ENAME, col = rainbow(5),
    main = "WARD 사원의 상사와 같은 사원들의 급여")


#chap07_2_infromal
#################################
## <제7장-1 연습문제>
################################# 

# 01. 다음과 같은 단계를 통해서 테이블을 호출하고, SQL문을 이용하여 레코드를 조회하시오.
# (DBMS : Oracle 사용)

# [단계 1] 사원테이블(EMP)을 검색하여 결과를 EMP_DF로 변수로 불러오기
EMP_DF <- dbGetQuery(conn, "select * from EMP")

# [단계 2] EMP_DF 변수를 대상으로 부서별 급여의 합계를 막대차트로 시각화(col)
query <- "select deptno, sum(sal) tot_sal  
          from emp
          group by deptno
          order by deptno"

# 부서별 급여 합계
emp_sal <- dbGetQuery(conn, query) 

# 부서명 받아오기
dept <- dbGetQuery(conn, "select * from dept")
dname <- dept$DNAME  


# [단계 3] 막대차트를 대상으로 X축의 축눈금을 부서명으로 표시하기
barplot(emp_sal$TOT_SAL, col = rainbow(3),
        names.arg = dname[1:3], main = "부서별 급여 합계")


#  02. 'WARD' 사원의 상사(MGR)와 같은 사원이름, 직책, 연봉을 출력하시오.
# <조건1> Oracle 서브쿼리 이용
# <조건2> 차트 결과 참고  

query <-"select ename, job, sal, mgr from EMP 
         where MGR = (select MGR from EMP where ename='WARD')"
result <- dbGetQuery(conn, query)


pie(result$SAL, 
    labels = result$ENAME, col = rainbow(5),
    main = "WARD 사원의 상사와 같은 사원들의 급여")


#내가 한거 
# 좀그 다름
#################################
## <제7장-1 연습문제>
################################# 

# 01. 다음과 같은 단계를 통해서 테이블을 호출하고, SQL문을 이용하여 레코드를 조회하시오.
# <조건1> Oracle 사용
# <조건2> 차트 결과 참고 

# [단계 1] 사원테이블(EMP)을 검색하여 결과를 EMP_DF 변수로 불러오기
emp<-"select*from emp"
EMP_DF<-dbGetQuery(conn,emp)
EMP_DF

emp
# [단계 2] EMP_DF 변수를 대상으로 부서별 (10,20,30) 급여의 합계를 막대차트로 시각화

query<- "select DEPTNO,sum(sal) from emp group by(DEPTNO)"


#부서별 그룹 생성
emp_sal<-dbGetQuery(conn, query)


df<- dbGetQuery(conn,query)
df

length(emp$SAL)
barplot(df$`SUM(SAL)`,col=rainbow(3),names.arg= df$DEPTNO,main='전체 사원의 급여 정보',)


barplot(emp$SAL,col=rainbow(length(emp$SAL)),
        main='전체 사원의 급여 정보',
        names.arg=emp$ENAME)

# [단계 3] 막대차트를 대상으로 X축의 축눈금을 부서명으로 표시하기

barplot(df$`SUM(SAL)`,col=rainbow(3),names.arg= df$DEPTNO,main='전체 사원의 급여 정보',xlab= "부서명")





#  02. 'WARD' 사원의 상사(MGR)와 동일한 사원이름, 직책, 연봉을 출력하시오.
# <조건1> Oracle 서브쿼리 이용
# <조건2> 차트 결과 참고 

query<-"select ename,job,sal from EMP
        where EMPNO in(select EMPNO from EMP where MGR=7698)"


MGR<-dbGetQuery(conn,query)
MGR

pie(MGR$SAL,df$ENAME,col=rainbow(5),
    main="WARD 사원의 상사와 같은 사원들의 급여")





