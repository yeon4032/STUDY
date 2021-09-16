-- Function_work.sql

/*
  함수명(인수1, 인수2, ...)
    - 특정 기능을 정의해 놓은 라이브러리 
*/


-- 1. 숫자 함수 

-- 1) ABS 함수 
SELECT -10, ABS(-10) FROM DUAL;  -- DUAL : 의사테이블 

-- 2) FLOOR 함수
SELECT 34.5678, FLOOR(34.5678) FROM DUAL; -- 34 : 절사 

-- 3) ROUND 함수
SELECT 34.5678, ROUND(34.5678) FROM DUAL; -- 35 : 반올림 
-- ROUND(상수, 자릿수)
SELECT 34.5678, ROUND(34.5678, 2) FROM DUAL; -- 34.57 : 양수(소숫점 자릿수 대상)
SELECT 34.5678, ROUND(34.5678, -1) FROM DUAL; -- 30 : 음수(정수 자릿수 대상)

-- 4)  MOD 함수 : 나머지값 반환 
SELECT MOD (27, 2), MOD (20, 5), MOD (20, 7) FROM DUAL; -- 1, 0, 6


-- <실습1> 사번이 홀수인 사람들을 검색해 보십시오.(EMP 테이블)
SELECT * FROM EMP WHERE MOD(EMPNO, 2) != 0;

-- 5) LOG 함수 : 자연로그(밑수 : 2, e)
SELECT LOG(2, 8) FROM DUAL; -- 8 = 2^3
SELECT LOG(2.71828, 8) FROM DUAL;-- 8 = e^2.0794

SELECT EXP(1) FROM DUAL; -- e=2.71828


-- 6) POWER 함수 : 제곱 
SELECT POWER(EXP(1), 2.07844) FROM DUAL; -- e^2.0794 = 7.9999

-- 7)  SQRT 함수 : 제곱근 
SELECT SQRT(49) FROM DUAL; -- 7



-- 2. 문자 처리 함수 

-- 1) UPPER 함수
SELECT 'Welcome to Oracle', UPPER('Welcome to Oracle') FROM DUAL;

-- 2) LOWER 함수
SELECT 'Welcome to Oracle', LOWER('Welcome to Oracle') FROM DUAL;

-- 3)  INITCAP 함수
SELECT 'WELCOME TO ORACLE', INITCAP('WELCOME TO ORACLE') FROM DUAL;

-- 실습2> 다음과 같이 쿼리문을 구성하면 직급이 'manager'인 사원을 검색할까? 
SELECT EMPNO, ENAME, JOB
FROM EMP
WHERE JOB=UPPER('manager');

-- 4) LENGTH 함수 
SELECT LENGTH('Oracle'), LENGTH('오라클') FROM DUAL;

-- LENGTHB 함수 
SELECT LENGTHB('Oracle'), LENGTHB('오라클') FROM DUAL;


-- 5) SUBSTR 함수
SELECT SUBSTR('Welcome to Oracle', 4, 3) FROM DUAL; -- com : 왼쪽 기준 

SELECT SUBSTR('Welcome to Oracle', -6, 6) FROM DUAL; -- Oracle : 오른쪽 기준 

-- 입사년도 -> 년, 월 구분 : 'YY/MM/DD'
SELECT SUBSTR(HIREDATE, 1, 2) 년도, SUBSTR(HIREDATE, 4, 2) 달 FROM EMP;

-- 2월 입사자 사원 정보 조회 
SELECT SUBSTR(HIREDATE, 1, 2) 년도, SUBSTR(HIREDATE, 4, 2) 달 
FROM EMP WHERE SUBSTR(HIREDATE, 4, 2) = '02';

-- 9월 입사 사원 
SELECT * FROM EMP WHERE SUBSTR(HIREDATE, 4, 2) = '09';

-- 6) TRIM 함수 : 앞/뒷 공백 제거 
SELECT TRIM(' Oracle XE') FROM DUAL;

-- 3. 날짜 함수 
-- 1) SYSDATE 함수
SELECT SYSDATE FROM DUAL;

-- 2) MONTHS_BETWEEN 함수
SELECT ENAME, SYSDATE, HIREDATE,
ROUND(MONTHS_BETWEEN(SYSDATE, HIREDATE)) "근무 개월수" 
FROM EMP; 

-- 3) ADD_MONTHS
SELECT ename, hiredate, ADD_MONTHS(hiredate, 12) FROM EMP;


-- 4. 형 변환 함수 
/*
  to_char() : 날짜, 숫자 -> 양식(format)을 이용한 문자형 변환 
  to_date() : 문자, 숫자 -> 양식(format)을 이용한 날짜형 변환 
  to_number() : 문자 -> 양식(format)을 이용한 숫자형 변환 
*/


-- 1)  TO_CHAR 함수

-- 날짜 -> 문자 양식 
SELECT SYSDATE, TO_CHAR(SYSDATE, 'YYYY-MM-DD') FROM DUAL;
SELECT HIREDATE, TO_CHAR (HIREDATE, 'YYYY/MM/DD DAY') FROM EMP; -- 요일 
SELECT TO_CHAR(SYSDATE, 'YYYY/MM/DD, HH24:MI:SS') FROM DUAL;

-- 숫자 -> 문자 양식 
SELECT ENAME, SAL, TO_CHAR (SAL, 'L999,999') FROM EMP;


-- 2) TO_DATE 함수 
SELECT ENAME, HIREDATE FROM EMP
WHERE HIREDATE=TO_DATE(19810220,'YYYYMMDD'); -- 숫자 -> 날짜형 

SELECT TO_DATE('1981-02-20', 'YYYY-MM-DD') FROM DUAL; -- 문자 -> 날짜형 

-- 3) TO_NUMBER 함수
SELECT TO_NUMBER('20,000', '99,999') - TO_NUMBER('10,000', '99,999') FROM DUAL; -- 10000

SELECT '20,000' - '10,000' FROM DUAL; -- ERROR : 문자 연산 불가 


-- 5. NULL 처리 함수 
-- NVL(대상, 대체값) vs NVL2(대상, NULL(X), NULL(O))

SELECT SAL*12+NVL(COMM, 0) 연봉 FROM EMP;
SELECT SAL, COMM, SAL*12+NVL2(COMM, COMM, 0) 연봉 FROM EMP;

-- 6. DECODE 함수 
-- encode vs decode
-- encode : 기계어 
-- decode : 인간어 

SELECT ename, deptno FROM emp;

SELECT ename, deptno, decode(deptno, 10, '기획실', 20, '연구실', 30, '영업부')
FROM emp;
