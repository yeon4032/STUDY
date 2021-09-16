-- 1.join.sql

/*
 *  물리적 조인(Join) 
 *   - 특정 칼럼(외래키)을 이용하여 두 개 이상의 테이블을 연결하는 DB 기법
 *  조인 절차
 *  1. 기본키가 포함된 테이블(master table) 생성  
 *  2. 기본키가 포함된 테이블에 레코드 삽입
 *  3. 외래키가 포함된 테이블(transaction table) 생성 
 *  4. 외래키가 포함된 테이블에 레코드 삽입
 * 
 *  조인 테이블 삭제 : 위 순서에 역순이다. 
 *  강제 테이블 삭제 : drop table 테이블명 cascade constraint;
 */

-- 1단계 : 기본키가 포함된 테이블 
drop table dept_tab purge; -- table 삭제 

create table dept_tab(
deptno number(2) primary key,  
dname varchar(30),
loc varchar(50)
);

-- 2단계 : 기본키가 포함된 테이블에 레코드 삽입
insert into dept_tab values(1, '기획부', '대전');
insert into dept_tab values(2, '영업부', '서울');
select * from dept_tab;

-- 3단계 : 외래키가 포함된 테이블(판매) 생성
drop table emp_tab purge; -- table 삭제 

create table emp_tab(
empno number(4) primary key,
ename varchar(30),
sal number(7),
deptno number(2) not null,
FOREIGN KEY(deptno) REFERENCES dept_tab(deptno) -- 외래키 지정 
);

-- 단계4 : 외래키가 포함된 테이블에 레코드 삽입
insert into emp_tab values(1001, '홍길동', 2500000, 1);
insert into emp_tab values(1002, '이순신', 3500000, 2);
insert into emp_tab values(1003, '유관순', 1500000, 3); -- error
-- 참조무결성 제약조건 위배 

commit work; -- [db 반영 -> 추가]



