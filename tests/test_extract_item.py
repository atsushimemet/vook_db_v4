import pytest

from vook_db_v4.extract_item import extract_item_denim, extract_item_denim_jacket

item_name_match = [
    "リーバイス 40s VINTAGE 501XX 革パッチ 片面タブ デニムパンツ ヴィンテージ インディゴ",
    "リーバイス ジージャン Ｇジャン Levi's 米国製 70579 バレンシア工場製造 リジッド デニムジャケット MADE IN THE USA",
]

item_name_not_match = [
    "Levi's リーバイス 1950 Levi's Vintage Big Poster ヴィンテージビッグポスター 広告用 ビンテージ ビッグサイズ"
    for _ in range(len(item_name_match))
]

extract_item_func_list = [extract_item_denim, extract_item_denim_jacket]
expected_list = ["denim", "denim jacket"]

parametrize_args_match = [
    (v1, v2, v3)
    for v1, v2, v3 in zip(item_name_match, extract_item_func_list, expected_list)
]
parametrize_args_not_match = [
    (v1, v2) for v1, v2 in zip(item_name_not_match, extract_item_func_list)
]


class TestExtractItem:
    @pytest.mark.parametrize(
        "item_name,func,expected",
        parametrize_args_match,
    )
    def test_valid_match(self, item_name, func, expected):
        actual = func(item_name)
        expected = expected
        assert actual == expected

    @pytest.mark.parametrize(
        "item_name,func",
        parametrize_args_not_match,
    )
    def test_valid_not_match(self, item_name, func):
        actual = func(item_name)
        expected = None
        assert actual == expected
