### 13강. 데이터베이스 시작하기 1

2026-02-02 월 - 2026-02-03 화

SQL
처음에는 낯설고 어려울 수 있는데, 너무 쉬우니까 걱정할 것 없다

#### 데이터베이스와 테이블 생성

🟧 SQL문 실행
- 실행: 메뉴바 - Query - Execute Current Statement (단축키: Cmd + Enter)
- 실행 옵션: 전체 / 선택 영역 / 현재 커서가 있는 곳

🟧 데이터베이스 생성
`CREATE DATABASE my_shop;`
- SQL문은 세미콜론( ; )으로 구분됨
- 앞으로는 생성한 데이터베이스 안에 테이블을 생성하게 됨

🟧 데이터베이스 사용 
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

🟧 테이블 구조 확인, 주석
`DESC sample; -- 또는 DESCRIBE sample;`
- 원래 describe, 줄여서 DESC
- 주석은 `-- 주석입니다` 이렇게 적음

🟧 데이터베이스, 테이블 목록 확인
`SHOW DATABASES;`
`SHOW TABLES;`

🟧 데이터베이스, 테이블 삭제
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