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
`SHOW DATABASES;`
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
