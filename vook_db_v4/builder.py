import abc
from dataclasses import dataclass
from typing import Callable, List, Tuple

import pandas as pd


class AbstractBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def extract(self, col_name, extract_func_list, validate_func):
        pass


@dataclass
class AgeBuilder(AbstractBuilder):
    col: pd.Series
    extract_func_list: List[Callable[[str], Tuple[str, str]]]
    validate_func: Callable[
        [Tuple[str, str], str, Callable[[str], Tuple[str, str]]], None
    ]

    def extract(self):
        l_extracted = []
        for i, item_name in enumerate(self.col):
            for func in self.extract_func_list:
                if func(item_name):
                    ret = func(item_name)
                    break
                else:
                    continue
            # 不正な値が入っている場合は、item_nameとretと適用された関数を表示する。
            self.validate_func(ret, item_name, func)
            # 出力
            if ret:
                l_extracted.append(ret)
            else:
                l_extracted.append(None)
        return l_extracted
