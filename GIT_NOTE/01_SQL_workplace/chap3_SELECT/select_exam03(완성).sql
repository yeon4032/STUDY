-- <연습문제3>
--1. EMP 테이블에서 hiredate가 1981년 2월 20과 1981년 5월 1일 사이에 입사한 사원의 
-- ename, job, hiredate을 출력하는 SELECT 문장을 작성(단 hiredate 순으로 정렬) 

-- 관계 & 논리식 
SELECT ename, job, hiredate
FROM emp
where hiredate >= to_date('1981/02/20', 'yyyy/mm/dd') and
hiredate <= to_date('1981/05/01', 'yyyy/mm/dd')
order by hiredate;

-- SQL 연산자 
SELECT empno,ename,job,sal,hiredate,deptno FROM emp
where hiredate BETWEEN to_date('1981/02/20', 'yyyy/mm/dd') 
AND to_date('1981/05/01', 'yyyy/mm/dd');

-- 리터널 이용 
SELECT empno,ename,job,sal,hiredate,deptno FROM emp
where hiredate between '81/02/20' and '81/05/01'
order by hiredate; 

-- 2. EMP 테이블에서 deptno가 10,20인 사원의 모든 정보를 출력하는 SELECT 문장을작성
-- (단 ename순으로 정렬)
SELECT * FROM emp
where deptno in (10, 20)
order by ename;





