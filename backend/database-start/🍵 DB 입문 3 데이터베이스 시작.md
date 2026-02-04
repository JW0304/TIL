### 13강. 데이터베이스 시작하기 1

2026-02-02 월 - 2026-02-03 화

SQL<br>
처음에는 낯설고 어려울 수 있는데, 너무 쉬우니까 걱정할 것 없다

#### 데이터베이스와 테이블 생성

🟧 SQL문 실행
- 실행: 메뉴바 - Query - Execute Current Statement (단축키: Cmd + Enter)
- 실행 옵션: 전체 / 선택 영역 / 현재 커서가 있는 곳

🟧 데이터베이스 생성<br>

`CREATE DATABASE my_shop;`
- SQL문은 세미콜론( ; )으로 구분됨
- 앞으로는 생성한 데이터베이스 안에 테이블을 생성하게 됨

🟧 데이터베이스 사용 <br>

`USE my_shop`
- 데이터베이스 선택, 엑셀 파일 더블 클릭하는 것과 같음
- 프로그램 껐다 켜면 다시 실행해야 함

🟧 테이블 생성

```SQL
CREATE TABLE sample (
	product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price INT,
    stock_quantity INT,
    release_date DATE
);
```
- VARCHAR(n): 가변길이 글자 (Variable Character) (최대 n자)
- DATE: YYYY-MM-DD 형식 (주문일, 가입일, 상품 출시일 등)
- 만들고 나서 SCHEMAS 새로고침해주면 됨

▪ 테이블 설계/정의
- 데이터베이스 테이블에는 반드시 기본 키(PK가 있어야 한다)

#### 데이터베이스, 테이블 구조 확인과 삭제

🟧 테이블 구조 확인, 주석<br>
`DESC sample; -- 또는 DESCRIBE sample;`
- 원래 describe, 줄여서 DESC
- 주석은 `-- 주석입니다` 이렇게 적음

🟧 데이터베이스, 테이블 목록 확인<br>
`SHOW DATABASES;`<br>
`SHOW TABLES;`

🟧 데이터베이스, 테이블 삭제<br>
```sql
-- 테이블 삭제
DROP TABLE sample;

-- 데이터베이스 삭제
DROP DATABASE my_shop;
```

▪ 여러 개의 쿼리 실행
```sql
-- 데이터베이스 생성  
CREATE DATABASE my_shop;

-- 데이터베이스 선택 
USE my_shop;

-- 테이블 생성  
CREATE TABLE sample (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price INT,
    stock_quantity INT,
    release_date DATE
);
```
- 전체 SQL문 실행: Query Execute(All or Selection)
- 단축키: Shift + Cmd + Enter
- GUI: 번개 버튼 클릭

---
### 14강. 데이터베이스 시작하기 2

2026-02-03 화

#### CRUD 맛보기

데이터 관리의 가장 핵심적인 기능

INSERT 생성 (Create) - 데이터 삽입<br>
SELECT 조회 (Read) - 데이터 선택<br>
UPDATE 수정<br>
DELETE 삭제<br>

```sql
-- 생성
INSERT INTO sample (product_id, name, price, stock_quantity, release_date)
VALUES (1, '프리미엄 청바지', 59900, 100, '2025-10-11');

-- 조회 (SELECT * = 모든 컬럼 조회)
SELECT * FROM sample;

-- 조회 (이름과 가격만)
SELECT name, price FROM sample;

-- 수정
UPDATE sample
SET price = 40000
WHERE product_id = 1;

-- 삭제
DELETE FROM sample
WHERE product_id = 1;
```

데이터베이스는 별 거 없다<br>
데이터베이스 만들고, 테이블 만들고<br>
데이터 등록, 조회, 수정, 삭제<br>
-> 이게 전부다 (나머지는 디테일한 부분들)<br>

▪ 데이터베이스의 대소문자 구분
- SQL 키워드는 대소문자 구분하지 않음 (select = SELECT = seLeCT)
- 하지만 직접 지정한 테이블명, 컬럼명은 DB/서버/설정에 따라 대소문자를 구분하기도 한다. -> 따라서 아래와 같은 관례를 따른다. (컨벤션)
- 실무에서는 SQL 키워드는 대문자, 이름은 소문자 (가독성 좋음)
- 실무에서는 대소문자 변환이 번거로워 다 소문자를 쓰는 경우도 있다.
- 이름은 소문자와 언더스코어( _ )로 짓는다.
- 데이터 자체는 대소문자를 구분한다.
- 이 원칙들을 지켜야 어떤 환경(DBMS)에서든 동일하게 작동한다.
```SQL
-- 데이터에서의 kim, KIM은 다르다
SELECT * FROM customers WHERE name = 'kim'
SELECT * FROM customers WHERE name = 'KIM'
```
---

### 15강. SQL이란?

SQL이란?
구조화된 질의 언어
국제 표준 기구에 의해 정해진 '**관계형 데이터베이스의 표준 언어**'

DBMS별 특징
DBMS마다 존재하는 추가 기능이나 문법을 방언(Dialect)라고 함

SQL의 특징
- ==선언적 언어== - 절차적 언어처럼 어떻게(How)를 명시하는 게 아니라, 어떤 데이터를 가져올지 무엇을(What) 명시함.
- 따라서 데이터 처리의 본질에만 집중할 수 있다.

<h3>SQL 명령어의 4가지 종류</h3>

목적, 기능에 따라 4가지 그룹이 있다.
#### 1. DDL - 데이터 정의어
- ==DB나 테이블==의 ==구조==를 정의하고 관리함.
- 명령어 - CREATE, ALTER, DROP etc.
#### 2. DML - 데이터 조작어
- 테이블 안에 있는 실제 '==데이터=='를 조작함. SQL에서 가장 빈번하게 사용되는 명령어들이 속한다.
- 명령어 - INSERT, SELECT, UPDATE, DELETE etc. (==CRUD==)
#### 3. DCL - 데이터 제어어
- 데이터 접근 권한의 부여나 회수(GRANT, REVOKE)를 말함, 데이터의 ==보안==과 관련된 ==권한 제어==
- 명령어 - GRANT, REVOKE
- 참고 - DCL은 협업 환경이나 고객이 이용하는 실무에서는 쓰지만, 혼자 공부할 때나 강의에서는 다루지 않음.
#### 4. TCL - 트랜잭션 제어어
- 목적 - DML에 의해 수행된 ==데이터 변경==(예: UPDATE)에 문제가 생겨서(서버 다운 등) 롤백하거나 그럴 때 필요함. 데이터의 일관성을 보장
- 개념 - 트랜잭션이란 '거래'를 말함(하나의 단위로 묶어서 데이터를 변경, 예: 계좌이체), ==둘 다 성공하거나 둘 다 실패해야== 함(COMMIT, ROLLBACK)
- 명령어 - COMMIT, ROLLBACK
- 참고 - 실무에서 매우 중요하지만, 좀 어려워서 DB 기본 강의에서 다룸

**결론**<br>
SQL은 데이터의 구조를 정의(DDL), 데이터를 조작(DML), 접근 권한을 제어(DCL), 작업 안정성을 보장(TCL)함.

---
### 16강. 데이터 타입

DB 설계
- 건물을 처음에 잘못 지으면 나중에 매우 힘들어지듯, DB도 잘못 설계하면 나중에 많은 문제를 일으킨다. 따라서 처음에 설계를 잘 해야된다. 
- 그러려면 **데이터 타입, 제약 조건**에 대해 알아야 한다.

다양한 데이터 타입
- 숫자, 문자 - 저장 공간(디스크)과 메모리를 아끼고(효율적 사용), 데이터 정확성을 높임(세 글자까지만 들어와야 하는데 열 글자인 경우 제약 등)
- 다양한 이유 - **효율성, 정확성**

정확한 숫자 타입 (Exact Value Numeric Types)
- 정수, 고정 소수점 숫자 (`INT`, `DECIMAL`, `NUMERIC`, `BIT`)
- `UNSIGNED INT`와 같이 `UNSIGNED`를 쓰는 경우, 음수 없이 숫자 영역을 두 배로 쓸 수 있게 된다 (`UNSIGNED INT`의 경우는 0부터 42억까지 저장 가능)

근사치 숫자 타입 (Approximate Value Numeric Types)
- 부동 소수점 숫자 (`FLOAT`, `DOUBLE`)
- 매우 크거나 매우 작은 숫자를 표현할 수 있지만, 약간의 오차가 발생할 수 있음
- 참고 - `FLOAT`는 단정밀도, 정밀도가 아주 중요하지 않은 실수 값의 경우. `DOUBLE`는 배정밀도, 과학 계산이나 공학 데이터처럼 더 큰 범위와 높은 정밀도가 필요한 경우

문자열 타입
-  `VARCHAR(n)`: 가장 많이 쓰임, **최대 n글자까지** (예: '홍길동' 3글자)
-  `CHAR(n)`: **항상 n글자일 때** (예: '남' '여', 'KR' 'US')
-  `TEXT`: 매우 긴 텍스트 (예: 상품 상세 설명, 블로그 게시글, 대화문 등)

`VARCHAR` vs `CHAR`
- 실무에서는 `VARCHAR`를 보편적으로 사용함
- 길이가 완벽하게 고정된 경우 `CHAR` 사용을 고려함(예: 주민등록번호, 국가 코드, 우편번호, 남녀 구분, MDS 해시값(32자리) 등)

날짜와 시간 타입
- 종류: `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, `YEAR`
- `DATE`: 날짜 ('YYYY-MM-DD')
- `DATETIME`: 날짜와 시간 ('YYYY-MM-DD HH:MM:SS')
- `TIMESTAMP`: 날짜와 시간 + 타임존 변환
	- **타임존(Timezone) 자동 변환**: UTC로 변환해서 저장, 보여줄 때는 서버 타임존에 맞춰서 보여줌 (조회)
	- **UTC**(협정 세계시): 세계에서 정한 **기준 시간**. 예전엔 영국 그리니치 천문대. 현재는 조금 더 조정이 들어감. 거의 영국 시간이라 보면 됨

`DATETIME` vs `TIMESTAMP`
- 실무에서는 `DATETIME`을 사용하면 됨 (요즘은 `TIMESTAMP` 잘 안 쓰고, `DATETIME`을 씀)
- `TIMESTAMP`는 1970-2038년까지, 얼마 안 남았음
- 어차피 타임존 변환은 애플리케이션에서 하면 된다 함

기타 타입
- `BLOB`: 이미지, 오디오, 비디오같은 **이진(Binary) 대용량 데이터**를 DB에 저장
- `ENUM`: 단일 선택 타입. 미리 정의한 값 목록 중 하나만 선택
- `SET`: 다중 선택 타입. 미리 정의한 값 목록 중 여러 개를 동시에 선택
- 실무에서 `ENUM`, `SET`은 잘 안 씀. (애플리케이션에서 사용, DB에서는 X)

---

### 17강. 제약조건

테이블에 데이터를 저장할 때, 특정 규칙을 지키도록 강제하는 장치
데이터의 일관성, 무결성 유지

타입 검증, 길이 검증, 날짜 형식 검증. 안 맞으면 오류. 하지만 이걸로는 부족함.
추가적인 제약 조건이 필요

-  `NOT NULL` : **필수 입력 항목 지정** - 빈값불가 (NULL 불가)
-  `UNIQUE` : **중복 불가 항목 지정** - 중복불가 (테이블 내에서 고유값) 
	- 예: 고객 ID, 이메일, 사업자 등록번호 등
	- PK와 차이점: PK는 `NOT NULL` + `UNIQUE`, 고유값인데 NULL은 가능
-  `PRIMARY KEY (PK)` : **테이블의 대표 식별자** - 모든 테이블에서 필수
	- `AUTO_INCREMENT` : 1씩 자동 증가
-  `FOREIGN KEY (FK)` : **테이블 간의 관계 설정** - 참조 무결성을 강제
-  `DEFAULT` : **기본값 설정** - 데이터를 `INSERT` 할 때 기본값
- `CHECK` : 컬럼에 입력되는 값이 특정 조건을 만족하는지 검사
