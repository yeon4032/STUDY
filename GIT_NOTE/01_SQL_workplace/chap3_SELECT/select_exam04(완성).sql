-- <최종 연습문제> 

-- [문1] emp에서 30번 부서에 근무하는 사원의 이름, 급여, 사번 출력하기 
-- 사용 칼럼명 : 이름(ename),급여(sal),사번(empno) 출력하기
select ename, sal, empno from emp where deptno = 30;

-- [문2] student 테이블의 전체 학생들을 대상으로 다음 예)와 같이 출력하기 
-- 예) 홍길동의 키는 175cm, 몸무게는 65kg입니다.
-- 사용 컬럼명 : 키(height), 몸무게(weight)
select name ||'의 키는'||height||'cm,'||'몸무게는'||weight||'kg 입니다.' 
from student;


--[문3] student 테이블을 사용하여 2학년 중에서 키가 180cm 보다 크고,
--     몸무게가 70kg 보다 큰 학생들의 이름,학년,키,몸무게 출력하기
-- 사용 컬럼명 : 이름(name), 학년(grade), 키(height), 몸무게(weight)
select name, grade, height, weight
from student 
where grade=2 and (height >= 180 and weight >= 70); 

--[문4] student 테이블을 사용하여 1학년 학생의 이름, 키, 몸무게 출력하기 
--  (단, 키는 오름차순, 몸무게는 내림차순으로 정렬하여 출력)
select name, grade, height, weight
from student 
where grade = 1
order by height, weight desc;

--[문5] student 테이블을 사용하여 1학년 학생의 '이름'과  '키' 출력(별칭 이용)
--  (단, 이름 오름차순으로 정렬)
select name 이름,  height 키 
from student where grade = 1 order by 이름; -- 별칭 이용 

--[문6] professor 테이블에서 교수들의 이름을 조회하여 
-- 성 부분에 '김'이 포함된 사람의 이름을 오름차순으로 출력
select name from professor
where name like '김%' order by name;

--[문7] professor 테이블를 대상으로 '전임'으로 검색하여 전임강사를 모두 검색하기
-- 사용 칼럼명 : position
select * from professor 
where position like '전임%';

--[문8] 장바구니에 '우유'와 '빵'를 동시에 구입한 장바구니 ID 출력(table 별칭 이용) 
select * from CART_PRODUCTS;
 
SELECT DISTINCT c1.CART_ID, c1.NAME, c2.NAME 
FROM CART_PRODUCTS c1, CART_PRODUCTS  c2
WHERE c1.NAME ='우유'  AND c2.NAME ='빵'
ORDER BY c1.CART_ID;
/*
 * 101   우유    빵
 * 103   우유    빵
 */

