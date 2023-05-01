import re
from typing import Callable, Tuple


def validate_19XX_fullmatch(
    ret: tuple, item_name: str, func: Callable[[str], Tuple[str, str]]
) -> None:
    if not re.fullmatch(r"19\d{2}", ret[0]) or not re.fullmatch(r"19\d{2}", ret[1]):
        raise Exception(f"\nitem_name: {item_name}\nvalue: {ret}\nfuncions: {func}")


def validate_item_fullmatch(
    ret: str, item_name: str, func: Callable[[str], str]
) -> None:
    if not ret:
        return None
    if not re.fullmatch(r"denim|denim\sjacket", ret):
        raise Exception(f"\nitem_name: {item_name}\nvalue: {ret}\nfuncions: {func}")
