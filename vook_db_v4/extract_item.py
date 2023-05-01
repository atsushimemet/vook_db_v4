import re


def extract_item_denim(item_name: str):
    match = re.search(r"デニムパンツ|デニム\sパンツ|デニム パンツ|ジーパン", item_name)
    if match:
        return "denim"
    else:
        return None
