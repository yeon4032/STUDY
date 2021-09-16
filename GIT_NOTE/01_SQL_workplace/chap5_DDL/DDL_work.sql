-- DDL_work.sql

/*
 DDL : 테이블 생성, 변경, 삭제 
  - 자동 커밋(auto commit)
*/

-- 1. 의사컬럼(Pseudo Column)
-- rownum : select 레코드 순번(레코드 입력 순서)

-- 최초 레코드 순번 검색 : 의사칼럼 - select, where절 사용 
SELECT ROWNUM, EMPNO, ENAME, ROWID
FROM EMP WHERE ROWNUM <= 5 ;

-- 레코드 순번 역순 검색 
SELECT ROWNUM, EMPNO, ENAME, ROWID
FROM EMP WHERE ROWNUM <= 5 
ORDER BY ROWNUM DESC;

-- 5번 ~ 10번째 입사자 : 범위 - 검색 안됨 
SELECT ROWNUM, EMPNO, ENAME, ROWID
FROM EMP WHERE ROWNUM >= 5 AND ROWNUM <= 10 ;

-- 특정 범위 지정 : subquery + 별칭 이용 
SELECT rnum, empno, ename, sal
FROM (SELECT emp.*, ROWNUM as rnum FROM emp)
WHERE rnum >= 5 AND rnum <= 10;

-- SUB Query 별칭 : main query의 SELECT, WHERE 이용 
-- 주의 : SELECT절에서는 사용되는 칼럼 : SUB query 칼럼만 사용 가능 

-- 응용1 : 최초 입사자 5명 테이블 생성 
CREATE TABLE emp_copy
as
SELECT * FROM emp WHERE ROWNUM <= 5;

-- 응용2 : 입사순서 5번 ~ 10번째 입사자 테이블 생성(emp_copy2)
CREATE TABLE emp_copy2
as
SELECT rnum, empno, ename
FROM (SELECT empno, ename, ROWNUM as rnum FROM emp)
WHERE rnum >= 5 AND rnum <= 10;

SELECT * FROM emp_copy2;


-- 2. 실수형 테이블 생성 
CREATE TABLE EMP01(
EMPNO NUMBER(4),
ENAME VARCHAR2(20),
SAL NUMBER(7, 2)); -- (전체, 소숫점)

INSERT INTO emp01 VALUES(1, 'hong', 1234.1);
INSERT INTO emp01 VALUES(2, 'lee', 1234.123);
INSERT INTO emp01 VALUES(3, 'kang', 123456.12345); -- error 

SELECT * FROM emp01;


-- 3. 서브쿼리 이용한 테이블 생성 
CREATE TABLE EMP02
AS
SELECT * FROM EMP;

SELECT * FROM EMP02; -- 구조+전체 내용 복제 

-- 실습 : 특정 칼럼 대상 테이블 생성 
CREATE TABLE EMP03
AS
SELECT EMPNO, ENAME FROM EMP;

SELECT * FROM EMP03; -- 구조+일부 칼럼 복제

-- 과제1> EMP 테이블을 복사하되 사원번호, 사원이름, 급여 컬럼으로 구성된 테이블을 생성하시오.(단 테이블의 이름은 EMP04) 
CREATE TABLE EMP04
AS
SELECT empno, ename, sal FROM emp;

SELECT * FROM EMP04;

-- 특정 행 대상 테이블 생성 
CREATE TABLE EMP05
AS
SELECT * FROM EMP
WHERE DEPTNO=10; -- 10번 부서만 대상 


-- 구조(스키마)만 복제
CREATE TABLE EMP06
AS
SELECT * FROM EMP WHERE 1=0;

SELECT * FROM EMP06;

-- 과제2> DEPT 테이블과 동일한 구조의 빈 테이블을 생성하시오.(테이블의 이름은 DEPT02) 
CREATE TABLE DEPT02
AS
SELECT * FROM DEPT WHERE 10=5;

SELECT * FROM DEPT02;

INSERT INTO DEPT02 VALUES(10, '기획실', '서울시');





