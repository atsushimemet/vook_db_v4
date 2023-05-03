#!/bin/bash
# データの前処理
# python ./vook_db_v4/get_yahoo_data_v2.py

# DB設定値を読み込み
source ./env/database.conf

# ログファイルの名前を設定する
log_file="./log/vook_db_load_$(date +%Y%m%d%H%M%S).log"

# ログファイルに開始時間を書き込む
echo "Start time: $(date +%Y-%m-%d_%H:%M:%S)" >> "$log_file"

# CSVファイルをMySQLのplatformsテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE './data/output/platforms.csv' 
  INTO TABLE platforms 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"
# CSVファイルをMySQLのagesテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE './data/output/ages.csv' 
  INTO TABLE ages 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"
# CSVファイルをMySQLのbrandsテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE './data/output/brands.csv' 
  INTO TABLE brands 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"
# CSVファイルをMySQLのitemsテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE './data/output/items.csv' 
  INTO TABLE items 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"
# CSVファイルをMySQLのlineテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE './data/output/line.csv' 
  INTO TABLE line 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"

# CSVファイルをMySQLのproductsテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE './data/output/products.csv' 
  INTO TABLE products 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"

# ログファイルに終了時間を書き込む
echo "End time: $(date +%Y-%m-%d_%H:%M:%S)" >> "$log_file"
