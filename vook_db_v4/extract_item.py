import re


def extract_item_denim(item_name: str):
    match = re.search(r"デニムパンツ|デニム\sパンツ|デニム パンツ|ジーパン", item_name)
    if match:
        return "denim"
    else:
        return None


def extract_item_denim_jacket(item_name: str):
    match = re.search(r"ジージャン|Ｇジャン|デニムジャケット|デニム ジャケット", item_name)
    if match:
        return "denim jacket"
    else:
        return None


extract_item_func_list = [extract_item_denim, extract_item_denim_jacket]
