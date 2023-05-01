#!/usr/bin/env python
# coding: utf-8

# # Import

# In[19]:


import sys

sys.path.append("../")
import json

import pandas as pd
import requests

from vook_db_v4.config import *


# # Global

# In[36]:


REQ_URL_CATE = "https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch"

WANT_ITEMS = [
    "itemCode",
    "itemName",
    "itemPrice",
    "itemUrl",
]
PLATFORM_ID = 2


# # Main

# In[11]:


query = "リーバイス ヴィンテージ"


# In[12]:


params = {
    "appid": ClientId,
    "output": "json",
    "query": query,
    "sort": "-price",
    "affiliate_id": aff_id,
    "affiliate_type": "vc",
    "results": 100,
    "start": 101,
}


# In[13]:


df = pd.DataFrame(columns=WANT_ITEMS)


# In[16]:


res = requests.get(url=REQ_URL_CATE, params=params)


# In[20]:


res_cd = res.status_code
if res_cd != 200:
    print(f"ErrCd:{res_cd}\nErr:{res['error']}\nPage:{cnt}")
else:
    res = json.loads(res.text)
    if len(res["hits"]) == 0:
        print("If the number of returned items is 0, the loop ends.")
    print(f"Get Data")
    l_hit = []
    for h in res["hits"]:
        l_hit.append(
            (
                h["index"],
                h["name"],
                h["price"],
                h["url"],
            )
        )
    df = pd.DataFrame(l_hit, columns=WANT_ITEMS)


# In[37]:


product_id_list = []
product_name_list = []
platform_id_list = []
for _, row in df.iterrows():
    product_id_list.append(hashlib.md5(str(row["itemCode"]).encode()).hexdigest())
    product_name_list.append(row["itemName"])
    platform_id_list.append(PLATFORM_ID)

