-- 1. 보호동물 테이블 
create table ANIMAL_INS(
AID int primary key, -- 동물 ID
ATYPE varchar(20) not null, -- 동물 유형 
DATETIME date not null, -- 보호 시작일 
CONDITON varchar(30), -- 상태
NAME varchar(20) -- 동물 이름 
);

create sequence ani_id increment by 1 start with 1001;

insert into ANIMAL_INS values(ani_id.nextval, '강아지', sysdate,	'양호','푸들');
insert into ANIMAL_INS values(ani_id.nextval, '강아지', sysdate,	'부상','진도');
insert into ANIMAL_INS values(ani_id.nextval, '고양이', sysdate,'양호',	'러시안블루');
insert into ANIMAL_INS values(ani_id.nextval, '강아지', sysdate,	'부상', 	'달마티안');
insert into ANIMAL_INS values(ani_id.nextval, '고양이', sysdate,'양호', '봄베이');
insert into ANIMAL_INS values(ani_id.nextval, '고양이', sysdate,'부상', '메이쿤');
insert into ANIMAL_INS values(ani_id.nextval, '강아지', sysdate,	'양호', 	'차우차우');
insert into ANIMAL_INS values(ani_id.nextval, '고양이', sysdate,'부상', '버만');
insert into ANIMAL_INS values(ani_id.nextval, '강아지', sysdate,	'부상', 	'블록');


select * from ANIMAL_INS;


-- [문1] 2. 입양동물 테이블   작성 
/*
 * 테이블명 : ANIMAL_OUTS
 * 칼럼명 : AID -> 자료형 : int, 제약조건 : 생략불가, 중복 불가
 * 칼럼명 : ATYPE -> 자료형 : 고정길이 문자(10자리), 제약조건 : 생략 불가
 * 칼럼명 : DATETIME -> 자료형 : 날짜형, 제약조건 : 생략 불가
 * 칼럼명 : NAME -> 자료형 : 가변길이 문자(최대 20자리), 제약조건 : 생략 가능  
 * 외래키 : AID 칼럼 -> ANIMAL_INS의 기본키 적용  
 */

CREATE TABLE ANIMAL_OUTS(
AID int not null unique,
ATYPE char(10) not null,
DATETIME date not null,  -- 입양일 
NAME varchar(20),
FOREIGN KEY(AID) REFERENCES ANIMAL_INS(AID) -- 외래키 지정 
);


-- ANIMAL_OUTS 테이블 레코드 추가 
insert into ANIMAL_OUTS values(1001, '강아지', '2020-10-03', '푸들');
insert into ANIMAL_OUTS values(1003, '고양이', '2020-12-10','러시안블루');
insert into ANIMAL_OUTS values(1004, '강아지', '2020-03-12', '달마티안');
insert into ANIMAL_OUTS values(1005, '고양이', '2020-12-25', '봄베이');
insert into ANIMAL_OUTS values(1006, '고양이', '2020-06-10', '메이쿤');

select * from ANIMAL_OUTS;


/*
 * [문2] TABLE 별칭 이용 
 * 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었다. 보호 시작일 보다 
 * 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 다음 SQL문을 완성하시오.
 * (단, 보호 시작일이 빠른 순서로 정렬)
 */ 

/*
 * <조회 결과> 
 * 1001
 * 1003
 * 1004
 * 1005
 * 1006
 */

-- SQL문
SELECT I.AID
FROM ANIMAL_INS I, ANIMAL_OUTS O;


/*
 * [문3] SUBQUERY 이용 
 * 천재지변으로 인해 일부 데이터가 유실되었다. 입양을 간 기록은 있는데,
 * 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID순으로 조회하시오.
 * 사용 테이블 
 *    - 유실된 테이블 : ANIMAL_INS2
 *    - 입양된 테이블 : ANIMAL_OUTS
 */

/*
 * <조회결과>
 * 1003
 * 1005
 * 1006
 */

-- 유실된 테이블 Table 생성 
CREATE TABLE ANIMAL_INS2 
AS 
SELECT * FROM ANIMAL_OUTS 
where ATYPE = '강아지';



/*
 * [문4] SUBQUERY & ROWNUM 이용 
 * 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과
 * 보호 시작일을 조회하는 SQL문을 작성하시오.(단 결과는 보호 시작일 순으로 조회)
 * 힌트 : ROWNUM 사용
 * 사용 테이블 : ANIMAL_INS, ANIMAL_OUTS
 */


/*
 * <조회결과>
 * 1002 
 * 1007 
 * 1008 
 */


