
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
