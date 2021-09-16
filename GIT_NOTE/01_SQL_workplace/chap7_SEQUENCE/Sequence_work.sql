-- Sequence_work.sql

-- 1. 시퀀스 생성 
CREATE SEQUENCE DEPT_DEPTNO_SEQ
INCREMENT BY 1
START WITH 1;

-- 2. 테이블 생성 
DROP TABLE dept01 PURGE;

CREATE TABLE dept01
as
SELECT * FROM dept WHERE 1 = 0;

SELECT * FROM dept01;

-- 3. 레코드 삽입 : 객체.멤버 
INSERT INTO dept01 VALUES(DEPT_DEPTNO_SEQ.nextval, 'test', '서울시');
INSERT INTO dept01 VALUES(DEPT_DEPTNO_SEQ.nextval, 'test2', '대전시');

-- 4. 데이터 사전 뷰 : 시퀀스 정보 확인 
SELECT * FROM USER_SEQUENCES; 
SELECT * FROM USER_TABLES;

-- 5. 시퀀스 삭제 
DROP SEQUENCE DEPT_DEPTNO_SEQ;


-- [실습] 사번 시퀀스 객체 생성 
-- 1) 시퀀스 생성
CREATE SEQUENCE EMP_SEQ
START WITH 1 
INCREMENT BY 1 
MAXVALUE 100000 ;

-- 2) table 생성 
DROP TABLE EMP01;

CREATE TABLE EMP01(
EMPNO NUMBER(4) PRIMARY KEY,
ENAME VARCHAR2(10),
HIREDATE DATE
);

-- 3) 레코드 추가
INSERT INTO EMP01 VALUES(EMP_SEQ.NEXTVAL, 'JULIA' , SYSDATE); 

SELECT * FROM EMP01;

-- 4) 시퀀스 삭제 
DROP SEQUENCE emp_seq;

-- <문제>
CREATE TABLE DEPT_EXAMPLE(
DEPTNO NUMBER(4) PRIMARY KEY,
DNAME VARCHAR(15),
LOC VARCHAR(15)
);


CREATE SEQUENCE deptno_seq
START WITH 10 
INCREMENT BY 10 
MAXVALUE 60 ;


INSERT INTO DEPT_EXAMPLE VALUES(deptno_seq.nextval, '인사과', '서울'); -- 10
INSERT INTO DEPT_EXAMPLE VALUES(deptno_seq.nextval, '경리과', '서울');
INSERT INTO DEPT_EXAMPLE VALUES(deptno_seq.nextval, '총무과', '대전');
INSERT INTO DEPT_EXAMPLE VALUES(deptno_seq.nextval, '기술팀', '인천');
INSERT INTO DEPT_EXAMPLE VALUES(deptno_seq.nextval, '기술팀', '인천');
INSERT INTO DEPT_EXAMPLE VALUES(deptno_seq.nextval, '기술팀', '인천'); -- 60
INSERT INTO DEPT_EXAMPLE VALUES(deptno_seq.nextval, '기술팀', '인천'); -- Error -> 시퀀스 수정 해결 
SELECT * FROM DEPT_EXAMPLE;


-- 6. 시퀀스 수정 : 최대값 수정 
ALTER SEQUENCE deptno_seq MAXVALUE 1000;

SELECT * FROM USER_SEQUENCES; 
