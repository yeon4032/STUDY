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
# [단계 2] EMP_DF 변수를 대상으로 부서별 급여의 합계를 막대차트로 시각화
barplot(EMP_DF, ylim=JOB, xlim = SAL, col= ...)

# [단계 3] 막대차트를 대상으로 X축의 축눈금을 부서명으로 표시하기


#  02. 'WARD' 사원의 상사(MGR)와 동일한 사원이름, 직책, 연봉을 출력하시오.
# <조건1> Oracle 서브쿼리 이용
# <조건2> 차트 결과 참고 










