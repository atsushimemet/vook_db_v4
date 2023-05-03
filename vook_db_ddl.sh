#!/bin/bash

# DDLファイルが格納されたディレクトリ
DDL_DIR=./vook_db_v4/ddl

# DDLファイルの一覧を取得
DDL_FILES=$(ls $DDL_DIR/*.ddl)

# DB設定値を読み込み
source ./env/database.conf

# 各DDLファイルを順に実行する
for DDL_FILE in $DDL_FILES; do
    echo "Executing $DDL_FILE..."
    mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME < $DDL_FILE
done
