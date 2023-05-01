import pytest

from vook_db_v4.extract_age import (
    extract_age_both_pat_1,
    extract_age_both_pat_2,
    extract_age_both_pat_3,
    extract_age_both_pat_4,
    extract_age_both_pat_5,
    extract_age_both_pat_6,
)

item_name_match = [
    "Levi's リーバイス 1950~60年代 Levi's Vintage Big Poster ヴィンテージビッグポスター 広告用 ビンテージ ビッグサイズ",
    "Levi's リーバイス 50's 60's Levi's Vintage Big Poster ヴィンテージビッグポスター 広告用 ビンテージ ビッグサイズ",
    "Levi's リーバイス 50~60年代 Levi's Vintage Big Poster ヴィンテージビッグポスター 広告用 ビンテージ ビッグサイズ",
    "Levi's リーバイス 50s-60s Levi's Vintage Big Poster ヴィンテージビッグポスター 広告用 ビンテージ ビッグサイズ",
    "Levi's リーバイス 1950-1960 Levi's Vintage Big Poster ヴィンテージビッグポスター 広告用 ビンテージ ビッグサイズ",
    "Levi's,リーバイス,1950~60年代,Levi's,Vintage,Big,Poster,ヴィンテージビッグポスター,広告用,ビンテージ,ビッグサイズ",
]

item_name_not_match = [
    "Levi's リーバイス 1950 Levi's Vintage Big Poster ヴィンテージビッグポスター 広告用 ビンテージ ビッグサイズ"
    for _ in range(len(item_name_match))
]

extract_age_func_list = [
    extract_age_both_pat_1,
    extract_age_both_pat_2,
    extract_age_both_pat_3,
    extract_age_both_pat_4,
    extract_age_both_pat_5,
    extract_age_both_pat_6,
]

parametrize_args_match = [
    (v1, v2) for v1, v2 in zip(item_name_match, extract_age_func_list)
]
parametrize_args_not_match = [
    (v1, v2) for v1, v2 in zip(item_name_not_match, extract_age_func_list)
]


class TestExtractAge:
    @pytest.mark.parametrize(
        "item_name,func",
        parametrize_args_match,
    )
    def test_valid_match(self, item_name, func):
        actual = func(item_name)
        expected = ("1950", "1960")
        assert actual == expected

    @pytest.mark.parametrize(
        "item_name,func",
        parametrize_args_not_match,
    )
    def test_valid_not_match(self, item_name, func):
        actual = func(item_name)
        expected = None
        assert actual == expected
