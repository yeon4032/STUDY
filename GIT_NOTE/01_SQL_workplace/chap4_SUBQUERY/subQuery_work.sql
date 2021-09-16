-- subQuery.sql

/*
 형식1)
 main query -> 2차 실행 
 as
 sub query; -> 1차 실행 

형식2)
main query 비교연산자 (sub query); 
*/

-- 형식1) 테이블 생성(내용 + 구조) 
create table dept01 -- main
as
select * from dept;  -- sub

select * from dept01; -- 내용 + 구조 

-- 형식2) main : dept, sub : emp -> join(dept - deptno - emp)
SELECT * FROM dept 
WHERE deptno = 
(SELECT deptno FROM emp WHERE ename='SCOTT'); -- 20


-- 1. 단일행 서브쿼리
-- 형식) main query 비교 연산자 (sub query);

-- 1. SCOTT과 같은 부서에서 근무하는 사원의 이름과 부서 번호를 출력하는 SQL 문을 작성해 보시오. (EMP)
-- main : emp, sub : emp
SELECT ename, deptno FROM emp
WHERE deptno = 
(SELECT deptno FROM emp WHERE ename='SCOTT'); -- 10


-- 2. SCOTT와 동일한 직속상관(MGR)을 가진 사원을 출력하는 SQL 문을작성해 보시오. (EMP)
SELECT * FROM emp
WHERE mgr = 
(SELECT mgr FROM emp WHERE ename='SCOTT'); -- 7566

-- 3. SCOTT의 급여와 동일하거나 더 많이 받는 사원 명과 급여를 출력하시오.(EMP)
SELECT ename, sal FROM emp
WHERE sal >= 
(SELECT sal FROM emp WHERE ename='SCOTT'); --3000

-- 4. DALLAS에서 근무하는 사원의 이름, 부서 번호를 출력하시오.(서브쿼리 : DEPT01, 메인쿼리 : EMP)
SELECT ename, deptno FROM emp
WHERE deptno =
(SELECT deptno FROM dept01 WHERE loc = 'DALLAS'); -- 20


-- 5. SALES(영업부) 부서에서 근무하는 모든 사원의 이름과 급여를출력하시오.(서브쿼리 : DEPT01, 메인쿼리 : EMP)
SELECT ENAME, SAL from emp
where deptno = 
(select DEPTNO from DEPT01 where dname='SALES'); -- 30

-- 단일행 서브 쿼리에서 그룹 함수 : 평균 급여 이상 수령자 
SELECT ENAME, SAL
FROM EMP
WHERE SAL > (SELECT AVG(SAL) FROM EMP); -- 2073.214


-- 2. 다중 행 서브쿼리 
-- 형식) main query  IN/ANY/ALL (sub query);

-- 1) IN (List)
SELECT ENAME, SAL, DEPTNO
FROM EMP
WHERE DEPTNO IN (SELECT DISTINCT DEPTNO
FROM EMP
WHERE SAL>=3000); -- 10, 20


-- 단일 쿼리 
SELECT ENAME, SAL, DEPTNO
FROM EMP
WHERE DEPTNO IN (10, 20);

-- 7. 직급(JOB)이 MANAGER인 사람이 속한 부서의 부서 번호와 부서명과 지역을 출력하시오.(DEPT01과 EMP 테이블 이용)
SELECT * FROM dept01
WHERE deptno IN
(SELECT deptno FROM emp WHERE job = 'MANAGER')
ORDER BY deptno; -- 10,20,30

-- 단일 쿼리
SELECT * FROM dept01
WHERE deptno IN (10,20,30);


-- 2) ALL(AND)
SELECT ENAME, SAL
FROM EMP
WHERE SAL > ALL (SELECT SAL FROM EMP WHERE DEPTNO =30); -- 2850

-- 8. 영업 사원들 보다 급여를 많이 받는 사원들의 이름과 급여와 직급(담당 업무)를 출력하되 영업 사원은 출력하지 않습니다. 
SELECT ENAME, SAL, JOB
FROM EMP
WHERE SAL >= ALL (SELECT SAL FROM EMP WHERE job = 'SALESMAN') AND job != 'SALESMAN';

SELECT * FROM emp;


-- 3) ANY(OR)
SELECT ENAME, SAL
FROM EMP
WHERE SAL > ANY ( SELECT SAL FROM EMP WHERE DEPTNO = 30 ); -- 950

-- 9. 영업 사원들의 최소 급여 이상 수령하는 사원들의 이름과
-- 급여와 직급(담당 업무)를 출력하되 영업 사원은 출력하지 않습니다. 
SELECT ename, sal, job
FROM emp 
WHERE sal >= ANY 
(SELECT sal FROM emp WHERE  job =  'SALESMAN')
AND job != 'SALESMAN'; -- 1250



