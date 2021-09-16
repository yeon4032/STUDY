select * from student; -- profno, deptno01
select * from PROFESSOR; -- profno

--[문1] STUDENT 테이블 검색 결과(sub)를 이용하여 STUDENT01 테이블 생성(main) 
-- Sub(STUDENT), Main(STUDENT01)
create table STUDENT01
as
select * from STUDENT;


-- [문2] 교수번호가 2001인 지도교수를 모시는 전체 학생 명부 출력
-- Sub(PROFESSOR), Main(STUDENT01)
select * from STUDENT01 where profno 
          = (select profno from PROFESSOR where profno = 2001); 


-- [문3] 보너스를 받는 교수들의 이름, 직위, 급여, 보너스 출력
-- 조건)   IN()함수 이용 : 다중 행 처리  
SELECT NAME, POSITION, PAY, BONUS FROM PROFESSOR WHERE PROFNO 
       IN(SELECT PROFNO FROM PROFESSOR WHERE BONUS IS NOT NULL);
      
-- [문4] 301 학과(DEPTNO) 교수들 보다 더 많은 급여를 받는 교수들의 이름, 직위, 급여, 학과 출력
-- 조건) ALL()함수 이용 : 다중 행 처리 
SELECT NAME, POSITION, PAY, DEPTNO FROM PROFESSOR WHERE PAY 
       > ALL(SELECT PAY FROM PROFESSOR WHERE DEPTNO = 301);
 
       
--[문5] 장바구니에 '우유'와 '빵'를 동시에 구입한 장바구니 ID 출력(subQuery 이용) 
select * from CART_PRODUCTS;

SELECT DISTINCT CART_ID
FROM CART_PRODUCTS 
WHERE CART_ID IN 
      (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = '빵') -- IN (1001, 1002, 1003)
AND NAME = '우유';
/* 
 * <장바구니 ID>
 * 101
 * 103
 */
      





