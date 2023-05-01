from vook_db_v4.extract_item import extract_item_denim, extract_item_denim_jacket
from vook_db_v4.validates import validate_item_fullmatch


def test_valid_item_denim():
    ret = "denim"
    item_name = "リーバイス 40s VINTAGE 501XX 革パッチ 片面タブ デニムパンツ ヴィンテージ インディゴ"
    func = extract_item_denim
    actual = validate_item_fullmatch(ret, item_name, func)
    expected = None
    assert actual == expected


def test_valid_item_denim_jacket():
    ret = "denim jacket"
    item_name = (
        "リーバイス ジージャン Ｇジャン Levi's 米国製 70579 バレンシア工場製造 リジッド デニムジャケット MADE IN THE USA"
    )
    func = extract_item_denim_jacket
    actual = validate_item_fullmatch(ret, item_name, func)
    expected = None
    assert actual == expected


def test_valid_item_denim_none():
    ret = None
    item_name = (
        "Levi's リーバイス 1950 Levi's Vintage Big Poster ヴィンテージビッグポスター 広告用 ビンテージ ビッグサイズ"
    )
    func = extract_item_denim
    actual = validate_item_fullmatch(ret, item_name, func)
    expected = None
    assert actual == expected


def test_valid_item_denim_jacket_none():
    ret = None
    item_name = (
        "リーバイス ジージャン Ｇジャン Levi's 米国製 70579 バレンシア工場製造 リジッド デニムジャケット MADE IN THE USA"
    )
    func = extract_item_denim_jacket
    actual = validate_item_fullmatch(ret, item_name, func)
    expected = None
    assert actual == expected
