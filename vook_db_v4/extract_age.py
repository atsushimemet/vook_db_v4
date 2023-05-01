import re


def extract_age_both_pat_1(item_name: str):
    match = re.search(r"\s19\d{2}~\d{2}年代\s", item_name)
    if match:
        start = match.group().split("~")[0].strip()
        end = "19" + match.group().split("~")[1].replace("年代", "").strip()
        return (start, end)
    else:
        return None


def extract_age_both_pat_2(item_name: str):
    match = re.search(r"\s\d{2}'s\s\d{2}'s\s", item_name)
    if match:
        start = "19" + match.group().split(" ")[1].replace("'s", "")
        end = "19" + match.group().split(" ")[2].replace("'s", "")
        return (start, end)
    else:
        return None


def extract_age_both_pat_3(item_name: str):
    match = re.search(r"\s\d{2}~\d{2}年代\s", item_name)
    if match:
        start = "19" + match.group().split("~")[0].strip()
        end = "19" + match.group().split("~")[1].replace("年代", "").strip()
        return (start, end)
    else:
        return None


def extract_age_both_pat_4(item_name: str):
    match = re.search(r"\s\d{2}s-\d{2}s\s", item_name)
    if match:
        start = "19" + match.group().split("-")[0].replace("s", "").strip()
        end = "19" + match.group().split("-")[1].replace("s", "").strip()
        return (start, end)
    else:
        return None


def extract_age_both_pat_5(item_name: str):
    match = re.search(r"\s\d{4}-\d{4}\s", item_name)
    if match:
        start = match.group().split("-")[0].strip()
        end = match.group().split("-")[1].strip()
        return (start, end)
    else:
        return None


def extract_age_both_pat_6(item_name: str):
    match = re.search(r",19\d{2}~\d{2}年代,", item_name)
    if match:
        start = match.group().split("~")[0].replace(",", "")
        end = "19" + match.group().split("~")[1].replace("年代", "").replace(",", "")
        return (start, end)
    else:
        return None


def extract_age_only_pat_1(item_name: str):
    match = re.search(r"\s\d{2}s\s", item_name)
    if match:
        start = end = "19" + match.group().replace("s", "").strip()
        return (start, end)
    else:
        return None


def extract_age_only_pat_2(item_name: str):
    match = re.search(r"\s\d{2}年代\s", item_name)
    if match:
        start = end = "19" + match.group().replace("年代", "").strip()
        return (start, end)
    else:
        return None


def extract_age_only_pat_3(item_name: str):
    match = re.search(r"\s\d{2}'s\s", item_name)
    if match:
        start = end = "19" + match.group().replace("'s", "").strip()
        return (start, end)
    else:
        return None


def extract_age_only_pat_4(item_name: str):
    match = re.search(r"\s\d{2}’s\s", item_name)
    if match:
        start = end = "19" + match.group().replace("’s", "").strip()
        return (start, end)
    else:
        return None


def extract_age_only_pat_5(item_name: str):
    match = re.search(r"\s\d{2}S\s", item_name)
    if match:
        start = end = "19" + match.group().replace("S", "").strip()
        return (start, end)
    else:
        return None


extract_age_func_list = [
    extract_age_both_pat_1,
    extract_age_both_pat_2,
    extract_age_both_pat_3,
    extract_age_both_pat_4,
    extract_age_both_pat_5,
    extract_age_both_pat_6,
    extract_age_only_pat_1,
    extract_age_only_pat_2,
    extract_age_only_pat_3,
    extract_age_only_pat_4,
    extract_age_only_pat_5,
]
