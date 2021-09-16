-- [1] SUBQUERY 테이블 생성 
-- DEPT 테이블의 부서위치(LOC)가 'BOSTON'을 제외한 나머지 내용으로 DEPT_TEST 테이블을 생성하시오. 
create table dept_test
as
select *from dept where loc!= 'boston';

-- [2] SUBQUERY 레코드 수정 
-- DEPT 테이블의 부서 번호 40번의 지역명을 이용하여 DEPT_TEST 테이블의 부서번호 30번 부서의 지역명을 변경하시오.
update dept_test set loc=
(select loc from dept where deptno=40)
where deptno=30;

-- [3] SUBQUERY 테이블 생성 
-- EMP 테이블에서 사번, 이름, 급여, 수당, 부서번호 칼럼의 내용으로 EMP_TEST 테이블을 생성하시오. 
create table EMP_TEST
AS
SELECT EMPNO,ENAME,SAL,COMM,DEPTNO FROM EMP;
SELECT * FROM EMP;



-- [4] SUBQUERY 레코드 삭제 
-- 'RESEARCH'부서에서 근무하는 모든 사원을 삭제하시오. 
-- 서브쿼리 : DEPT_TEST 테이블
-- 메인쿼리 : EMP_TEST 테이블 

DELETE FROM EMP_TEST
WHERE DEPTNO=(SELECT DEPTNO
FROM DEPT_TEST WHERE DNAME ='RESEARCH');


-- [5] SUBQUERY 레코드 삭제 
-- 이름(ENAME)이 'M'로 시작하는 레코드를 모두 삭제하시오. 
-- 서브쿼리 : EMP 테이블
-- 메인쿼리 : EMP_TEST 테이블 


DELETE FROM EMP_TEST 
WHERE ENAME IN( SELECT ENAME FROM EMP WHERE ENAME LIKE 'M%');

DELETE FROM EMP_TEST WHERE ENAME IN ('MARTIN', 'MILLER');

SELECT *FROM EMP_TEST;

