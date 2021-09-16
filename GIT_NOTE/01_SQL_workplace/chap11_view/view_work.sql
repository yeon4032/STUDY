--view_work.sql

--1.기본 테이블 생성

CREATE TABLE DEPT_COPY
AS
SELECT * FROM DEPT;

CREATE TABLE EMP_COPY
AS
SELECT * FROM EMP;


--2.뷰 생성: 서브쿼리 이용

CREATE VIEW EMP_VIEW30
AS 
SELECT EMPNO, ENAME, DEPTNO
FROM EMP_COPY
WHERE DEPTNO=30;

/*
SCOTT사용자 view 권한 
SQL> conn system/1234
SQL>grant create view to scott;
*/

select *from emp_view30; --기본 테이블의 부분 내용 조회


--3.뷰의 데이터사전 뷰

select *from user_views; -- 사용자가 만든 view 의 목록 볼수있다.

-- USER_VIEWS에서 테이블 이름과 텍스트만 출력해 보자.
select view_name, text from user_views;


--4. 뷰 삭제
drop view emp_view30;


--5. 뷰에 사용 목적
/*
1. 복잡한 SQL문 사용시 
2. 보안 목적 (접근권안을 이용해 특정 인물이 정보를 열람 가능 하고 안하고 정해짐)
*/

--1. 복잡한 SQL문 사용시 

create or replace view join_view
as 
(SELECT S.NAME 학생명, S.STUDNO 학과,P.NAME 교수명,P.PROFNO 교수번호
FROM PROFESSOR P,STUDENT S
WHERE S.PROFNO= P.PROFNO)
with read only; -- 읽기 전용의 view(INSERT, UPDATE,DELETE 차단)

select *from join_view;

--2.보안 목적
--예를 들어 사원 테이블에 개인 정보인 급여와 커미션은 부서에 따라
--접근을 제한한다. 인사과는 급여나 커미션 모두 조회할 수 없도록
--하고, 경리과에서는 이 모두가 조회될 수 있도록 한다. 또한
--영업부서에서는 경쟁심을 유발하기 위해서 다른 사원의 커미션을
--조회할 수 있도록 해야한다.


--1)영업사원 제공 뷰
create or replace view sales_view
as 
(select empno,ename, comm from emp 
where job='SALESMAN')
WITH READ ONLY;

SELECT *FROM SALES_VIEW WHERE COMM > 0;

DELETE FROM SLAES_VIEW WHER EMPNO=7499; -- 가능하나 VIEW 에서 WITH READ ONLY 라는 명령어 땜 안됨

--2) 일반사원 제공 뷰 :서브쿼리 카럼 상속 대신 별칭 사용 가능 

create or replace view CLERK_view (사번,이름,입사일,부서번호)
as 
(select empno,ename, HIREDATE, DEPTNO from emp 
where job='CLERK')
WITH READ ONLY;

SELECT *FROM CLERK_VIEW;


-- 뷰의 옵션

--1) WITH CHECK OPTINO

CREATE OR REPLACE VIEW VIEW_CHK30
AS 
(SELECT EMPNO, ENAME, SAL, COMM, DEPTNO 
FROM EMP_COPY
WHERE DEPTNO=30) WITH CHECK OPTION;

UPDATE VIEW_CHK30 SET DEPTNO=20
WHERE SAL>= 1200; --ERROR 
--VIEW_CHK30 뷰를 생성할 때 부서번호에 WITH CHECK OPTION을 지정하였기에 
--이 뷰를 통해서는 부서번호를 변경할 수 없다.
























