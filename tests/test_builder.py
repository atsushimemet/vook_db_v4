from pathlib import Path

import pandas as pd

from vook_db_v4.builder import AgeBuilder
from vook_db_v4.extract_decades import extract_decades_func_list
from vook_db_v4.validates import validate_19XX_fullmatch


def test_run_age_builder_extract():
    OUTPUT_PATH = Path("data/output/")
    file_name = "20230430_132941_for_issue_11.csv"
    item_name = pd.read_csv(OUTPUT_PATH / file_name)["itemName"]
    actual = AgeBuilder(
        item_name, extract_decades_func_list, validate_19XX_fullmatch
    ).extract()
    assert actual
