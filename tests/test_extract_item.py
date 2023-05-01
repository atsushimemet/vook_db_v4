import pytest

from vook_db_v4.extract_item import extract_item_denim

item_name_match = ["リーバイス 40s VINTAGE 501XX 革パッチ 片面タブ デニムパンツ ヴィンテージ インディゴ"]

item_name_not_match = [
    "Levi's リーバイス 1950 Levi's Vintage Big Poster ヴィンテージビッグポスター 広告用 ビンテージ ビッグサイズ"
    for _ in range(len(item_name_match))
]

extract_item_func_list = [
    extract_item_denim,
]

parametrize_args_match = [
    (v1, v2) for v1, v2 in zip(item_name_match, extract_item_func_list)
]
parametrize_args_not_match = [
    (v1, v2) for v1, v2 in zip(item_name_not_match, extract_item_func_list)
]


class TestExtractItem:
    @pytest.mark.parametrize(
        "item_name,func",
        parametrize_args_match,
    )
    def test_valid_match(self, item_name, func):
        actual = func(item_name)
        expected = "denim"
        assert actual == expected

    @pytest.mark.parametrize(
        "item_name,func",
        parametrize_args_not_match,
    )
    def test_valid_not_match(self, item_name, func):
        actual = func(item_name)
        expected = None
        assert actual == expected
