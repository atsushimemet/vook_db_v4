import abc


class AbstractBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def extract(self, col_name, extract_func_list, validate_func):
        pass
