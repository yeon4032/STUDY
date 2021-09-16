-- GroupFunction_work.sql


/*
  그룹 함수 : 그룹별 통계(집계)를 구하는 함수 
    - 통계/집계 함수 : 복수행(vector) -> 상수값(scala) : 차원축소 
*/

-- 1. SUM 함수 
SELECT SUM(SAL) FROM EMP;

SELECT SUM(COMM) FROM EMP;

-- 2. AVG 함수 : 대푯값 
SELECT AVG(SAL) FROM EMP; -- 2073.21

-- <문제1> ‘SCOTT’사원이 소속된 부서의 급여 합계와 평균을 구하시오.(서브쿼리 이용)
SELECT SUM(sal), AVG(sal) FROM emp
WHERE deptno =
(SELECT deptno FROM emp WHERE ename = 'SCOTT');


-- 3. MIN/MAX 함수 
SELECT MAX(SAL), MIN(SAL) FROM EMP;

SELECT ename, SUM(sal) FROM emp; -- error : 단일 칼럼, 그룹함수(x)


-- <문제2> 가장 최근에 입사한 사원의 입사일과 입사한지 가장 오래된 사원의 입사일
--- 을 출력하는 쿼리문을 작성하시오. (MAX, MIN, to_char 함수 이용)
SELECT TO_CHAR(MAX(HIREDATE), 'YY/MM/DD') "입사일", TO_CHAR(MIN(HIREDATE), 'YY/MM/DD') "입사일" 
FROM emp;

-- 4. COUNT 함수
SELECT COUNT(COMM), COUNT(*) FROM EMP;  -- 4, 14

SELECT COUNT(JOB) 업무수 FROM EMP; --14
SELECT COUNT(DISTINCT JOB) 업무수 FROM EMP; -- 5

-- <문제3> 30번 부서 소속 사원중에서 커미션을 받는 사원의 수를 구하시오.
SELECT COUNT(*) "사원수" FROM emp WHERE deptno = 30  AND comm IS NOT NULL; -- 4
SELECT COUNT(*) "사원수" FROM emp WHERE deptno = 30  AND comm > 0; -- 3

SELECT comm, deptno FROM emp WHERE deptno = 30  AND comm> 0; -- 3


-- 5. 분산/표준편차 : 산포도
/*
   모분산 = SUM((X - mu)^2) / N : mu : 모평균 -> 모분산 
   표본분산 = SUM((X - 산술평균)^2) / n-1 : mu : 모평균 -> 표본분산
   
   표준편차 = 분산의 제곱근 
*/

SELECT VARIANCE(bonus) FROM PROFESSOR;
SELECT STDDEV(bonus) FROM PROFESSOR;
SELECT SQRT(VARIANCE(bonus)) FROM PROFESSOR; -- 분산의 제곱근


-- 6.  GROUP BY 절
/*
   GROUP BY 범주형(칼럼) 
*/

SELECT DEPTNO
FROM EMP 
GROUP BY DEPTNO;
-- 주의 : 그룹 칼럼은 SELECT절에서 사용 가능 

SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO;

SELECT DEPTNO, MAX(SAL), MIN(SAL)
FROM EMP 
GROUP BY DEPTNO;

-- <문제4>  부서별로 가장 급여를 많이 받는 사원의 정보(사원 번호, 사원이름, 
-- 급여, 부서번호)를 출력하시오.
SELECT empno, ename, sal, deptno
FROM emp
WHERE  sal IN
(SELECT MAX(SAL) FROM EMP GROUP BY DEPTNO);


-- 7. HAVING절 조건
/*
  일반 SQL문 : WHERE 조건식 
  GROUP BY문 : HAVING 조건식 
*/

SELECT DEPTNO, AVG(SAL) 
FROM EMP
GROUP BY DEPTNO
HAVING AVG(SAL) > 2000;



-- <문제5> <문제4>의 결과에서 'SCOTT' 사원을 제외하고, 급여(SAL)를
-- 내림차순으로 정렬하시오.
SELECT empno, ename, sal, deptno
FROM emp
WHERE ename != 'SCOTT' AND (deptno, sal) IN
(SELECT DEPTNO, MAX(SAL) FROM EMP GROUP BY DEPTNO)
ORDER BY sal DESC;


