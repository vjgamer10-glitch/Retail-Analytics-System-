CREATE DATABASE IF NOT EXISTS retail_db;
USE retail_db;

CREATE TABLE IF NOT EXISTS sales_data (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    store_id VARCHAR(50),
    store_location VARCHAR(100),
    product_id VARCHAR(50),
    product_category VARCHAR(100),
    product_subcategory VARCHAR(100),
    brand VARCHAR(100),
    unit_price DECIMAL(10,2),
    units_sold INT,
    total_sales DECIMAL(12,2),
    discount_percentage DECIMAL(5,2),
    revenue DECIMAL(12,2),
    customer_type VARCHAR(50),
    payment_mode VARCHAR(50),
    promotion_applied VARCHAR(10),
    stock_on_hand INT,
    store_rating DECIMAL(3,1),
    region VARCHAR(50),
    holiday_flag INT
);