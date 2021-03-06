# coding=utf-8
from typing import Dict, Union, List

from . import BaseDataType

class Secret(BaseDataType):
    original: Dict[str, Union[str, int, Dict, List]] = {}

    def __init__(self, config: Dict[str, Union[str, int, Dict, List]]) -> None:
        self.original = config

        if self.original:
            [setattr(self, k, v) for k, v in self.original.items()]
