from pathlib import Path

import pandas as pd

from vook_db_v4.builder import AgeBuilder, ItemBuilder
from vook_db_v4.extract_age import extract_age_func_list
from vook_db_v4.extract_item import extract_item_func_list
from vook_db_v4.validates import validate_19XX_fullmatch, validate_item_fullmatch


def test_run_age_builder_extract():
    OUTPUT_PATH = Path("data/output/")
    file_name = "20230430_132941_for_issue_11.csv"
    item_name = pd.read_csv(OUTPUT_PATH / file_name)["itemName"]
    actual = AgeBuilder(
        item_name, extract_age_func_list, validate_19XX_fullmatch
    ).extract()
    assert actual


def test_run_item_builder_extract():
    OUTPUT_PATH = Path("data/output/")
    file_name = "20230430_132941_for_issue_11.csv"
    item_name = pd.read_csv(OUTPUT_PATH / file_name)["itemName"]
    actual = ItemBuilder(
        item_name, extract_item_func_list, validate_item_fullmatch
    ).extract()
    assert actual
