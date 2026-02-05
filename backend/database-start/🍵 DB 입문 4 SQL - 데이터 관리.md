
2026-02-05 목

### DDL - 테이블 생성 1

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


### DDL - 테이블 생성 2

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

