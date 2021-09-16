--step02_join_work.sql

/*
카티전 조인(cartesian join)
-논리적(조건식)으로 테이블을 연결하는 방식
종류
  1.Cross Join 조건 없이 테이블 연결
  2.Seif Join 한 테이블 내에서 조인 (동일 테이블 조인)
  3.Inner Join 조인 조건에 만족하는 행만 조인 (조인 대상 테이블이 모두 존재)
  4.Outer Join 조인 조건에 만족하지 않는 행도 조인(조인 대상 테이블중에서 한개 태이블 존재)
  
*/


--1. CROSS JOIN
--카티전 조인 또는 Cross Join으로 특별한 키워드 없이 SELECT 문의 FROM 절에 테이블을 콤마로 연결
--Cross Join 결과는 컬럼의 수는 사원 테이블의 컬럼 수(8), 부서 테이블의 컬럼 수(3)를 더한 것이므로 11개
--행 수는 사원 한 명에 대해서 DEPT 테이블의 4개의 행과 결합되기에 56개(14*4)

SELECT * FROM EMP, DEPT; -- SHAPE=> 전체 리코드(행) =56 (14*4), 8개의 컬럼(열) (8+3)

SELECT*FROM EMP; 행=14, 열=8
SELECT*FROM DEPT; 행=4 열=3

--2. SELF JOIN :별칭 이용
--조인은 두 개 이상의 서로 다른 테이블을 서로 연결하는 것뿐만 아니라, 하나의 테이블 내에서 조인을 해야만 
--원하는 자료를 얻는 경우도 발생한다.

SELECT E1.*,E2.*
FROM EMP E1,EMP E2;--1차:SHAP(196,16)
WHERE E1.MGR=E2.EMPNO;

SELECT E1.*,E2.*
FROM EMP E1,EMP E2
WHERE E1.MGR=E2.EMPNO; -- 2차:SHAPE (13,16)

/*
E1:일반 사원 정보
E2: 직속상사 정보
*/

--실습


SELECT E1.ENAME 사원명,E2.ENAME 상사명
FROM EMP E1,EMP E2
WHERE E1.MGR=E2.EMPNO;


--문제 1
SELECT E1.ENAME,E1.JOB
FROM EMP E1,EMP E2
WHERE  E1.MGR=E2.EMPNO  AND E2.ENAME='KING';



--INNER JOIN
--조인 대상 테이블에 모두 자료가 잇는 경우 사용가능.
--조인 대상이 되는 두 테이블에서 공통적으로 존재하는 컬럼의 값이 일치되는 행을 연결하여 결과를 생성
--형식
--SELECT *FROM EMP, DEPT WHERE EMP.DEPTNO = DEPT.DEPTNO

SELECT *FROM DEPT;
SELECT *FROM EMP;

SELECT *
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO;

--일반 INNER JOIN: 특정 컬럼만 (별칭이용)
SELECT E.EMPNO,E.ENAME,D.DNAME,D.LOC
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO;


--이름이 SCOTT인 사람의 부서명을 출력해봅시다.
SELECT ENAME, DNAME
FROM EMP, DEPT
WHERE EMP.DEPTNO=DEPT.DEPTNO AND ENAME='SCOTT'; -- JOIN 조건

SELECT E.ENAME, D.DNAME
FROM EMP E, DEPT D
WHERE E.DEPTNO=D.DEPTNO AND E.ENAME='SCOTT';

--Inner Join(컬럼명의 모호성 해결)
--두 테이블에 동일한 이름의 칼럼을 사용하면 어느 테이블 소속인지 불분명하기에 오류 메시지 출력

SELECT ENAME, DNAME, DEPTNO
FROM EMP, DEPT 
WHERE EMP.DEPTNO = DEPT.DEPTNO
AND ENAME='SCOTT'; --ERROR 왜냐하면 DEPTNO 이 EMP 와 DEPT 에 둘다 있어서 출처가 분명하기 않아서.

--ANSI INNER JOIN: 표준 SQL
SELECT EMP.ENAME, DEPT.DNAME
FROM EMP INNER JOIN DEPT
ON EMP.DEPTNO=DEPT.DEPTNO --JOIN 조건
WHERE EMP.ENAME='SCOTT';-- 일반 조건

--문제:뉴욕에서 근무하는 사원의 이름과 급여를 출력하시오.(EMP, DEPT 이용)

SELECT * FROM DEPT;
SELECT *FROM EMP;

SELECT EMP.ENAME, EMP.SAL
FROM EMP INNER JOIN DEPT
ON EMP.DEPTNO=DEPT.DEPTNO
WHERE DEPT.LOC='NEW YORK';

SELECT EMP.ENAME, EMP.SAL
FROM EMP,DEPT
WHERE EMP.DEPTNO=DEPT.DEPTNO
AND DEPT.LOC='NEW YORK';

--문제3:ACCOUNTING 부서 소속 사원의 이름, 입사일, 근무지역을 출력하시오.

SELECT EMP.ENAME,EMP.HIREDATE,DEPT.LOC,DEPT.DNAME
FROM EMP,DEPT
WHERE EMP.DEPTNO=DEPT.DEPTNO
AND DEPT.DNAME='ACCOUNTING';

--문제4 직급이 MANAGER인 사원의 이름, 부서명을 출력하시오.

SELECT EMP.ENAME,DEPT.DNAME
FROM EMP,DEPT
WHERE  EMP.DEPTNO=DEPT.DEPTNO
AND EMP.JOB='MANAGER';


--문제5:교수번호(profno) 칼럼을 기준 조인하여 다음 그림과 같이 학생명,학번, 교수명, 교수번호 칼럼을 조회하시오
SELECT *FROM PROFESSOR;--20,PROFNO
SELECT *FROM STUDENT; --16,PROFNO

SELECT STUDENT.NAME 학생명, STUDENT.STUDNO 학과,PROFESSOR.NAME 교수명,PROFESSOR.PROFNO 교수번호
FROM PROFESSOR,STUDENT
WHERE STUDENT.PROFNO= PROFESSOR.PROFNO;

SELECT S.NAME 학생명, S.STUDNO 학과,P.NAME 교수명,P.PROFNO 교수번호
FROM PROFESSOR P,STUDENT S
WHERE S.PROFNO= P.PROFNO;

--문제6:<문제5>의 결과에서 101 학과만 검색되도록 하시오

SELECT STUDENT.NAME 학생명, STUDENT.STUDNO 학과,PROFESSOR.NAME 교수명,PROFESSOR.PROFNO 교수번호
FROM PROFESSOR,STUDENT
WHERE STUDENT.PROFNO= PROFESSOR.PROFNO
AND PROFESSOR.DEPTNO=101;

SELECT S.NAME 학생명, S.STUDNO 학과,P.NAME 교수명,P.PROFNO 교수번호
FROM PROFESSOR P,STUDENT S
WHERE S.PROFNO= P.PROFNO
AND P.DEPTNO=101;


--4. Outer Join
--외부 조인은 NULL 값이기에 배제된 행을 결과에 포함시킬 수있으며 정보가 부족한 칼럼 뒤에“(+)” 기호를 덧붙인다.
--정보가 부족한 컬럼에 (+)추가
-- 기준 테이블 :+ 없음


--1) left outer join: 왼쪽 테이블 기준
SELECT e1.ename 사원명, e2.ename 상사명
FROM emp e1, emp e2
WHERE e1.mgr = e2.empno(+); -- 직속상사 없는 경우 추가
/*
  e1:일반 사원
  e2:직속 상사
*/

--문재8

select e.ename, e.deptno, d.dname
from emp e,dept d
where d.deptno = e.deptno(+)
order by deptno;



--2)right outer join:오른쪽 테이블 기준
select e.ename, e.deptno, d.dname
from emp e,dept d
where e.deptno(+)=d.deptno
order by deptno;


--or

select s.name 학생명, p.name 교수명
from student s, professor p
where s.profno (+)= p.profno;


--3) ANSI RIGHT OUTER JOIN :지도쇼수 없는 학생

select s.name 학생명, p.name 교수명
from student s RIGHT OUTER JOIN professor p
ON s.profno (+)= p.profno;

--SAME

select s.name 학생명, p.name 교수명
from student s RIGHT OUTER JOIN professor p
USING(PROFNO); -- 공통칼럼 (ON s.profno (+)= p.profno 같음)

--4)ANSI LEFT OUTER JOIN: 지도 학생이 없는 교수

select s.name 학생명, p.name 교수명
from student s LEFT OUTER JOIN professor p
USING(PROFNO);


