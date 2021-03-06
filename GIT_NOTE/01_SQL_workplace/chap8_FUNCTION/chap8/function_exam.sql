/*
 * 주요 함수 
 * 작업 대상 테이블 : STUDENT, EMP, PROFESSOR 
 */

--Q1. STUDENT 테이블에서 JUMIN 칼럼을 사용하여 
-- 태어난 달이 8월인 사람의 이름과 생년월일 출력하기
-- 힌트 : substr() 함수 이용

SELECT *FROM STUDENT;
SELECT NAME,BIRTHDAY,SUBSTR(JUMIN,3,2) FROM STUDENT 
WHERE SUBSTR(JUMIN,3,2)=08;

SELECT NAME,BIRTHDAY,JUMIN FROM STUDENT 
WHERE SUBSTR(JUMIN,3,2)=08;


--Q2. EMP 테이블에서 사번이 홀수인 사람들을 검색하기
-- 힌트 : mod() 함수 이용

SELECT *FROM EMP WHERE MOD(EMPNO,2)= 1;


--Q3. Professor 테이블에서 교수명, 급여, 보너스, 연봉을 출력하기 
-- 조건) 연봉 = pay*12+bonus 으로 계산, bonus가 없으면 pay*12 처리
-- 힌트 : nvl2() 함수 이용

SELECT *FROM PROFESSOR;
SELECT NAME,PAY,BONUS,PAY*12+NVL2(BONUS,BONUS,0) FROM PROFESSOR ;



--Q4. Professor 테이블에서 교수명, 학과명을 출력하되 
--  deptno가 101번이면 ‘컴퓨터 공학과’, 102번이면 
-- ‘멀티미디어 공학과’, 103번이면 ‘소프트웨어 공학과’, 
-- 나머지는 ‘기타학과’로 출력하기
-- decode()함수 이용

SELECT NAME,DEPTNO, DECODE
(DEPTNO,101,'컴퓨터공학과',102,'멀티미디어 공학과',103,'소프트웨어 공학과','기타학과')
FROM PROFESSOR;
