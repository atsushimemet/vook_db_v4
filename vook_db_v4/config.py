import datetime

from vook_db_v4.local_config import ClientId, pid, sid

aff_id = f"//ck.jp.ap.valuecommerce.com/servlet/referral?vs={sid}&vp={pid}&vc_url="
REQ_URL_CATE = "https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch"

WANT_ITEMS = [
    "itemCode",
    "itemName",
    "itemPrice",
    "itemUrl",
]
PLATFORM_ID = 2
BRAND = "リーバイス"
BRAND_ID = 1
ITEM = "デニム"
ITEM_ID = 1
LINE = "66前期"
LINE_ID = 1
# START_AGE = 1974
# END_AGE = 1977
AGES_ID = 1
RUN_TIME = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
INFO_GET_DATE = datetime.datetime.today()
TABLE_COLUMNS = [
    "product_id",
    "product_name",
    "platform_id",
    "ages_id",
    "brand_id",
    "item_id",
    "line_id",
    "price",
    "info_get_date",
    "status",
]

query = f"{BRAND} ヴィンテージ {ITEM} {LINE}"

params = {
    "appid": ClientId,
    "output": "json",
    "query": query,
    "sort": "-price",
    "affiliate_id": aff_id,
    "affiliate_type": "vc",
    "results": 100,  # NOTE: 100個ずつしか取得できない。
}
