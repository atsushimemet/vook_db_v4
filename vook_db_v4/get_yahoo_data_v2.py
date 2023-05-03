#!/usr/bin/env python
# coding: utf-8
import json

import pandas as pd
import requests

from vook_db_v4.config import (
    AGES_ID,
    BRAND,
    BRAND_ID,
    INFO_GET_DATE,
    ITEM,
    ITEM_ID,
    LINE,
    LINE_ID,
    PLATFORM_ID,
    REQ_URL_CATE,
    RUN_TIME,
    TABLE_COLUMNS,
    WANT_ITEMS,
    params,
)


def create_lines_raw(
    params: dict,
    max_products: int = 1000,
    step: int = 100,
    start_num: int = 1,
) -> pd.DataFrame:
    l_df = []
    for inc in range(0, max_products, step):
        params["start"] = start_num + inc
        df = pd.DataFrame(columns=WANT_ITEMS)
        res = requests.get(url=REQ_URL_CATE, params=params)
        res_cd = res.status_code
        if res_cd != 200:
            print("Bad request")
            break
        else:
            data = json.loads(res.text)
            if len(data["hits"]) == 0:
                print("If the number of returned items is 0, the loop ends.")
                break
            print("Get Data")
            l_hit = []
            for h in data["hits"]:
                l_hit.append(
                    (
                        h["index"],
                        h["name"],
                        h["price"],
                        h["url"],
                    )
                )
            df = pd.DataFrame(l_hit, columns=WANT_ITEMS)
            l_df.append(df)
    lines_raw = pd.concat(l_df, axis=0, ignore_index=True)
    lines_raw.to_csv(
        f"./data/output/{RUN_TIME}_lines_raw_{BRAND}_{ITEM}_{LINE}.csv", index=False
    )
    return lines_raw


def create_lines(lines_raw: pd.DataFrame) -> pd.DataFrame:
    product_id_list = []
    product_name_list = []
    price_list = []
    for _, row in lines_raw.iterrows():
        product_id_list.append(row["itemCode"])
        product_name_list.append(row["itemName"])
        price_list.append(row["itemPrice"])
    tmp_cols = ["product_id", "product_name", "price"]
    tmp_df = pd.DataFrame(
        zip(product_id_list, product_name_list, price_list),
        columns=tmp_cols,
    )
    tmp_df["platform_id"] = PLATFORM_ID
    tmp_df["ages_id"] = AGES_ID
    tmp_df["brand_id"] = BRAND_ID
    tmp_df["item_id"] = ITEM_ID
    tmp_df["line_id"] = LINE_ID
    tmp_df["info_get_date"] = INFO_GET_DATE
    tmp_df["status"] = "S"
    tmp_df = tmp_df[TABLE_COLUMNS]
    lines = tmp_df.copy()
    return lines


def main():
    lines_raw = create_lines_raw(params)
    lines = create_lines(lines_raw)
    lines.to_csv("./data/output/products.csv", index=False)


if __name__ == "__main__":
    main()
