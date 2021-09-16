﻿/*
 * 집합 함수(COUNT,MAX,MIN,SUM,AVG) 
 * 작업 대상 테이블 : EMP, STUDENT, PROFESSOR
 */

--Q1. PROFESSOR 테이블에서 POSITION의 수 출력하기
SELECT COUNT(DISTINCT POSITION) 직위수 FROM PROFESSOR;


--Q2. EMP 테이블에서 소속 부서별 최대 급여와 최소 급여 구하기
SELECT DEPTNO, MAX(SAL), MIN(SAL) FROM EMP 
GROUP BY DEPTNO;


--Q3. EMP 테이블에서 전체 사원의 급여에 대한 분산과 표준편차 구하기
select variance(sal), stddev(sal) from EMP; 

-- Q4. EMP 테이블에서 각 부서별 사원수와 수당을 받는 사원수를 카운트 하시오.
SELECT DEPTNO, COUNT(*), COUNT(comm)
FROM emp
GROUP BY deptno;

--<출력 결과>
/*
부서번호     전체사원수     수당사원수
30        6        4  
20        5        0
10        3        0 
*/

--Q5. PROFESSOR 테이블에서 학과별 급여(pay) 평균이 400 이상 레코드 출력하기
select deptno, avg(pay) from Professor
group by deptno
having avg(pay) >= 400;

--Q6. PROFESSOR 테이블에서 학과별,직위별 급여(pay) 평균 구하기
select deptno, position, avg(nvl(pay,0)) 
from Professor
group by deptno, position
order by deptno;

--Q7. STUDENT 테이블에서 grade별로 
-- weight, height의 평균값, 최대값, 최소값을 구한 
-- 결과에서 키의 평균이 170 이하인 경우 구하기
select grade, avg(height), 
max(weight), min(weight), max(height), min(height) 
from STUDENT group by grade
having avg(height) <= 170;







