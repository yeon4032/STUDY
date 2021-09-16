-- sql_cp.sql



/*
  SQL(Structured Query Language) : 구조화된 질의 언어 
  - DDL, DML, DCL
  1. DDL : 데이터 정의어 -> DBA, USER(TABLE 생성, 구조변경, 삭제)
  2. DML : 데이터 조작어 -> USER(SELECT, INSERT, DELETE, UPDATE)
  3. DCL : 데이터 제어어 -> DBA(권한설정, 사용자 등록 등) 
*/

-- 1. DDL : 데이터 정의어

-- 1) Table 생성 
/*
 * create table 테이블명(
 *   칼럼명 데이터형 [제약조건],
 *   칼럼명 데이터형
 *   );
 */
 
 create table test2(
 id varchar2(20) primary key,
 passwd varchar2(50) not null,
 name varchar2(25) not null 
 ); 

-- 테이블 목록 조회 
select * from tab;
select * from test2; -- 테이블 내용 확인 
select * from member;

-- desc test2; -- 테이블 구조(스키마) 확인 

-- 2) Table 구조 변경 
-- (1) 테이블 이름 변경 
-- 형식) alter table 구테이블명 rename to 새테이블명;
alter table test2 rename to member;

-- (2) 테이블 칼럼 추가 
-- 형식) alter table 테이블명 add (칼럼명 자료형(n));
alter table member add(reg_date date);

--(3) 테이블 칼럼 수정 : 이름변경(x), type, 제약조건 수정 
-- 형식) alter table 테이블명 modify (칼럼명 자료형(n) 제약조건); 
alter table member modify(passwd varchar2(25));

-- (4) 테이블 칼럼 삭제 
-- 형식) alter table 테이블명 drop column  칼럼명;
alter table member drop column passwd;

-- 3) Table 제거 
-- 형식) drop table 테이블명 purge;
-- purge 속성 : 임시파일 제거 
drop table member purge;


-- 2. DML : 데이터 조작어
create table depart(
dno number(4),
dname varchar(50),
daddress varchar(100)
);

-- 1) insert : 레코드 삽입
-- 형식) insert into 테이블명(칼럼명1, .. 칼럼명n) values(값1, ... 값n);
insert into depart(dno, dname, daddress) values(1001, '기획실', '서울');
-- 칼럼명 생략한 경우 : 전체 칼럼 입력 
insert into depart values(1002, '영업부', '싱가폴');  
-- 부분 칼럼명 입력 
insert into depart(dno, dname) values(1003, '총무부');


-- 2) select : 레코드 검색 
-- 형식) select 칼럼명 from 테이블명 [where 조건식];
select * from depart; -- 전체 칼럼 
select dno, dname from depart; -- 특정 칼럼 
select * from depart where dno = 1002;
select * from depart where daddress is null; -- 주소 없는 경우 
select * from depart where daddress is not null; -- 주소 있는 경우 

-- 3) update : 레코드 수정 
-- 형식) update 테이블명 set 칼럼명 = 값 where 조건식;
update depart set daddress='대전시' where dno = 1003;

-- 4) delete : 레코드 삭제 
-- 형식) delete from 테이블명 where 조건식;
delete from depart where dno = 1003;

-- 3. DCL : 데이터 제어어
-- 1) 권한 설정 : grant 권한, ... to user;
-- 2) 권한 해제 : revoke 권한, ... to user;

grant connect to scott;
revoke connect to scott;
create user scott ~;

-- db 반영 : 작업내용 
commit;

