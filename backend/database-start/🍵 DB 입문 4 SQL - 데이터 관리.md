
2026-02-05 목

### 19강. DDL - 테이블 생성 1

쇼핑몰 테이블 설계

```SQL
CREATE TABLE customers (
	customer_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	address VARCHAR(255) NOT NULL,
	join_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
	product_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	description TEXT,
	price INT NOT NULL,
	stock_quantity INT NOT NULL DEFAULT 0
);

-- 어떤 고객이, 어떤 상품을 주문했는가: 주문 테이블이 가장 중요!
CREATE TABLE orders (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT '주문접수',
    
    -- FK 설정
    CONSTRAINT fk_orders_customers FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id),
    
    CONSTRAINT fk_orders_products FOREIGN KEY (product_id)
    REFERENCES products(product_id)
);

```

**자동 증가, 기본값**
- `AUTO_INCREMENT` 데이터를 저장할 때마다 값이 1씩 자동으로 증가
- `DEFAULT` 설정에 따라 현재 시각( `CURRENT_TIMESTAMP` )

**날짜와 기본값 설정 옵션** - 생성일, 수정일
```sql
CREATE TABLE test (
    ...
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

**외래 키 제약조건**
```sql
-- 부모에서 자식으로 PK -> FK
CONSTRAINT 제약조건_이름  
FOREIGN KEY (자식테이블_컬럼)
REFERENCES 부모테이블(부모테이블_컬럼)
-- 추가사항
[ON DELETE 옵션] [ON UPDATE 옵션]
```

`fk_orders_customers`
- `외래 키 제약조건`의 이름은 `orders -> customers` (자식이 부모를 참조)
- 오류가 뜰 때 `외래 키 제약조건`의 이름이 뜬다 ❗

참고
- 데이터베이스 설계만 해도 다룰 내용이 엄청 많다
- 하지만 여기선 일단 데이터베이스의 기본적 기능을 배우는 게 목적이다


### 20강. DDL - 테이블 생성 2

ERD(Entity Relationship Diagram)

**MySQL 워크벤치로 ERD 만들기** 
- MySQL 워크벤치 실행
- 상단 메뉴 바에서 Database > Reverse Engineer.. 실행 (역설계)

![MySQL 워크벤치 ERD](./attachments/🍵%20DB%20입문%204%20SQL%20-%20데이터%20관리-3.png)
아이콘 색에 따라 PK, FK, 일반 컬럼(채워져 있는 건 NOT NULL) 등이 나뉜다

ERD (DB 설계)
- 실무에서는 수십, 수백 개의 테이블을 사용하게 된다
- 까마귀발 모양은 일대다(1:N, One-to-Many) 관계를 나타낸다
- `customers (1)` -----< `orders (N)`
- 위의 표기법을 <u>까마귀발 표기법(Crow's Foot Notation)</u>이라고 한다

`orders` 테이블은 `customers` 와 `products` 의 중간에서 두 테이블을 연결하는 중요한 역할을 하고 있다
- **`orders` 테이블의 `customer_id` (FK)가 `customers` 테이블의 `customer_id` (PK)를 바라보고,** 
- **`orders` 테이블의 `product_id` (FK)가 `products` 테이블의 `product_id` (PK)를 바라보는 구조다.**

참고
- 테이블 간의 연관 관계는 1:N, N:1, N:N, 1:1 같은 다양한 관계가 있다.  
- 연관 관계와 ERD 설계에 관한 자세한 내용은 데이터베이스 설계 강의에서 다룬다.

실무에서의 이름 규칙 (Best Practice)
- 기본 규칙과 확장 규칙이 있음
- 기본 규칙: 숫자, 영문, `_`, $, 숫자는 맨 앞에 쓸 수 없음, 예약어 불가 etc.
- 확장 규칙: 백틱으로 감싸면 대부분 가능, 띄어쓰기, 하이픈(-), @ etc.
- 하지만 실제로는 **영문 소문자, 밑줄(`_`)만 사용**한다 (스네이크 케이스, snake_case)

### 21강. DDL - 테이블 변경, 제거

2026-02-06 금
#### ALTER TABLE: 테이블 구조 변경

alter - 바꾸다, 변경하다, 수선하다

```sql
-- 열 추가
ALTER TABLE customers
ADD COLUMN point INT NOT NULL DEFAULT 0;
-- 열 수정
ALTER TABLE customers
MODIFY COLUMN address VARCHAR(500) NOT NULL;
-- 열 삭제
ALTER TABLE customers
DROP COLUMN point;
```

실무 경고
ALTER는 실무에선 정말 조심해서 써야 함!!! 보통 점검 시간에 관리
(파일 변경 작업 중에는 파일 접근이 막히는 경우가 생긴다)

#### DROP TABLE vs TRUNCATE TABLE

drop - 떨어지다, 떨어트리다
truncate - 끝을 잘라내다 (원뿔이나 나무, 긴 인용구 따위를 잘라 줄이다)

- `DROP TABLE` : **테이블 자체를 삭제한다.**
- `TRUNCATE TABLE` : **테이블은 남기고, 내부 데이터만 모두 삭제한다.**

**TRUNCATE vs DELETE**
- `DELETE FROM products WHERE product_id = 1;` --> `DELETE`는 한 줄씩 없앤다 (`WHERE`조건이 있는 행을 삭제한다)
- `DELETE FROM products;` -->  `WHERE`조건이 없으므로 모든 행을 한 줄씩 없앤다. `TRUNCATE`가 훨씬 빠르다.
- `TRUNCATE` 는 `AUTO_INCREMENT` 값도 초기화한다. `DELETE`는 `AUTO_INCREMENT` 값을 초기화하지 않는다.

**외래키 제약 조건이 있는 경우 삭제 불가**
```sql
DROP TABLE products;

-- 에러 문구: orders 테이블의 FK가 products를 참조하고 있다고 한다
Error Code: 3730. Cannot drop table 'products' referenced by a foreign key constraint 'fk_orders_products' on table 'orders'.

-- 만약 삭제가 된다면 "상품이 없는 주문"이 되는 문제가 생길 것이다!
```
에러 문구가 다 안 보이면 우클릭 -> copy response로 sql 내에 붙여넣기해보자

```sql
TRUNCATE TABLE products;

-- 에러 문구
Error Code: 1701. Cannot truncate a table referenced in a foreign key constraint (`my_shop`.`orders`, CONSTRAINT `fk_orders_products`)

-- 마찬가지다. 참고로 truncate는 데이터가 있는지 없는지 상관 안 한다.
```

**외래키 제약조건 무시 설정하기**

```sql
-- 외래키 체크 설정 끄기
SET FOREIGN_KEY_CHECKS = 0; -- 비활성화

TRUNCATE TABLE products;

-- 외래키 체크 설정 다시 켜기: 외래키 체크 설정을 끄면 데이터 무결성이 깨질 수 있으므로, 필요한 작업을 마친 후에는 반드시 다시 켜줘야 한다!
SET FOREIGN_KEY_CHECKS = 1; -- 활성화

--SET XXX은 데이터베이스 접속이 연결되는 동안 유효하다. 따라서 MySQL 워크벤치 프로그램을 껐다 켜면 다시 설정해줘야 한다.
```

### 22강. DML - 데이터 등록

실무에서 가장 많이 사용하는 명령어들이다. `INSERT`, `UPDATE`, `DELETE`를 깊이 있게 알아보자.
#### INSERT - 행 생성

행을 생성하는 방법은 세 가지가 있다

```sql
-- 방법 1. 컬럼 지정하지 않고, 모든 열에 대한 데이터 추가하기
INSERT INTO customers 
VALUES (NULL, '강감찬', 'kkc@email.com', 'password123', '서울시 동작구', '2026-02-06 18:58:30');

INSERT INTO customers 
VALUES (NULL, '이순신', 'lss@email.com', 'password456', '서울시 관악구', '2026-02-06 18:59:50')

-- 방법 2. 컬럼 지정하기, 선택한 열에 대한 데이터 추가하기
INSERT INTO customers (name, email, password, address)
VALUES ('세종대왕', 'sj@email.com', 'password789', '서울시 종로구');

INSERT INTO products (name, price, stock_quantity)
VALUES ('베이직 반팔 티셔츠', 19900, 200);

-- 방법 2에 대해서
실무에서 가장 흔하게 사용하는 방식이다!
왜냐하면 방법1은 나중에 열이 추가/수정될 경우 오류를 일으킬 수 있기 때문이다
따라서 방법2로 열 목록을 명시적으로 넣는 게 안전하고 좋은 방법이다

-- 빠진 열
- 기본적으로는 null이 들어가게 됨, default 값이 있으면 기본값 들어감
- customer_id 자동으로 지정(auto_increment)
- join_date(datetime)도 자동으로 현재 시간이 저장되었음(null, default current_timestamp로 지정된 컬럼)

-- 방법 3. 한 번에 등록하기
INSERT INTO products (name, price, stock_quantity)
VALUES 
('검정 양말', 3000, 500),
('회색 양말', 3000, 500),
('흰색 양말', 3000, 500);

```
customer_id는 NULL로 넣어도 auto_increment 된다

```sql
-- (복습) 조회 - 테이블 구조, 테이블 데이터
desc customers;
select * from customers;
```
혼자 간단하게 실행할 때는 소문자로 쭉 작성해도 된다 ❗

---
추가

◾ 역설계<br>
원래는 설계를 하고 DB를 만드는데 DB를 먼저 만들고 ERD를 보는 것
리버스 엔지니어링이라고 함