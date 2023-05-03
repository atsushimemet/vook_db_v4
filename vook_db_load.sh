#!/bin/bash
# データの前処理
# ログファイルの名前を設定する
log_file="/home/ec2-user/vook_db_v4/log/vook_db_load_$(date +%Y%m%d%H%M%S).log"

# ログファイルにデータ前処理開始時間を書き込む
echo "Start time - get_yahoo_data_v2.py: $(date +%Y-%m-%d_%H:%M:%S)" >> "$log_file"
source /home/ec2-user/vook_db_v4/.venv/bin/activate
python /home/ec2-user/vook_db_v4/vook_db_v4/get_yahoo_data_v2.py
# ログファイルにデータ前処理終了時間を書き込む
echo "End time - get_yahoo_data_v2.py: $(date +%Y-%m-%d_%H:%M:%S)" >> "$log_file"

# DB設定値を読み込み
source /home/ec2-user/vook_db_v4/env/database.conf

# ログファイルにload infile開始時間を書き込む
echo "Start time - load_infile: $(date +%Y-%m-%d_%H:%M:%S)" >> "$log_file"
# CSVファイルをMySQLのplatformsテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE '/home/ec2-user/vook_db_v4/data/output/platforms.csv' 
  INTO TABLE platforms 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"
# CSVファイルをMySQLのagesテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE '/home/ec2-user/vook_db_v4/data/output/ages.csv' 
  INTO TABLE ages 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"
# CSVファイルをMySQLのbrandsテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE '/home/ec2-user/vook_db_v4/data/output/brands.csv' 
  INTO TABLE brands 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"
# CSVファイルをMySQLのitemsテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE '/home/ec2-user/vook_db_v4/data/output/items.csv' 
  INTO TABLE items 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"
# CSVファイルをMySQLのlineテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE '/home/ec2-user/vook_db_v4/data/output/line.csv' 
  INTO TABLE line 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"

# CSVファイルをMySQLのproductsテーブルに挿入する
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} --local-infile=1 ${DB_NAME} -e "
  LOAD DATA LOCAL INFILE '/home/ec2-user/vook_db_v4/data/output/products.csv' 
  INTO TABLE products 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '\"' 
  LINES TERMINATED BY '\n' 
  IGNORE 1 ROWS;
"

# ログファイルにload infile終了時間を書き込む
echo "Start time - load_infile: $(date +%Y-%m-%d_%H:%M:%S)" >> "$log_file"
