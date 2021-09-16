/*
 * 주요 함수 
 * 작업 대상 테이블 : STUDENT, EMP, PROFESSOR 
 */

--Q1. STUDENT 테이블에서 JUMIN 칼럼을 사용하여 
-- 태어난 달이 8월인 사람의 이름과 생년월일 출력하기
-- substr() 함수 사용
select name, birthday, jumin, substr(jumin, 3, 2) 
from student where substr(jumin, 3, 2)='08';

--Q2. EMP 테이블에서 사번이 홀수인 사람들을 검색하기
-- mod() 함수 사용
select * from EMP where mod(empno,2) != 0;

--Q3. Professor 테이블에서 교수명, 급여, 보너스, 연봉을 출력하기 
-- 조건) bonus 있는 경우 : 연봉 = pay*12+bonus, 
--      bonus 없는 경우 : 연봉 = pay*12
-- 힌트 : nvl2(값1,값2,값3)
select name, pay, bonus, nvl2(bonus,pay*12+bonus, pay*12) 연봉 
from professor;

--Q4. Professor 테이블에서 교수명, 학과명을 출력하되 
--  deptno가 101번이면 ‘컴퓨터 공학과’, 102번이면 
-- ‘멀티미디어 공학과’, 103번이면 ‘소프트웨어 공학과’, 
-- 나머지는 ‘기타학과’로 출력하기
-- 힌트 : decode()함수 사용
select name, deptno, 
   decode(deptno,101,'컴퓨터공학과',
                 102,'멀티미디어 공학과',
                 103,'소프트웨어 공학과','기타학과') 
   from professor;