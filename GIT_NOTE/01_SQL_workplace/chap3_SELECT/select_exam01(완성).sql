-- <연습문제1>
-- 문1) 다음 문장에서 에러를 올바르게 수정(년봉은 별칭)
SELECT empno,ename,sal * 12 년봉 FROM emp;

-- 문2) EMP 테이블의 구조 조회(힌트 : DESC  테이블)
DESC EMP; -- editor 이용

-- 문3) EMP 테이블의 모든 내용 조회
SELECT * from emp;

-- 문4) EMP 테이블에서 중복되지 않는 deptno 출력(힌트 : distinct)
SELECT DISTINCT deptno from emp; -- 30, 20, 10

-- 문5) EMP 테이블의 ename과 job를 연결하여 출력
SELECT ename || ' ' || job from emp;

-- 문6) DEPT 테이블의 dname과 loc를 연결하여 출력
SELECT dname || ' -> ' || loc AS "부서명과 위치" from dept;

-- 문7) EMP 테이블의 job과 sal를 연결하여 출력
SELECT job || ' ' || sal AS "직책과 급여" from emp;

-- 문8) gift 테이블을 대상으로 별칭을 사용하여 <출력 형식>과 같이 출력 
select * from gift;
select gno as "선물번호", gname as "선물이름" from GIFT;
/* <출력 형식>
       선물번호      선물이름 
      1      참치세트
      2      샴푸세트   */ 