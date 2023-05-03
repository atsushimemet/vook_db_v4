#!/bin/bash
# データの前処理
# python ./vook_db_v4/get_yahoo_data_v2.py

# DB設定値を読み込み
source ./env/database.conf

# CSVファイルをMySQLのproductsテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE './data/output/products.csv' 
  INTO TABLE products 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"
