import sys

from os import environ
from enum import Enum
from typing import Any, Dict

def init_module_from_env(module_name: str):
    module = sys.modules[module_name]
    for var_key in dir(module):
        if not var_key.startswith("ENV_"):
            continue
        var_value = environ.get(var_key)
        if var_value is not None:
            module.__setattr__(var_key, var_value)


def expand_enum(data: Dict[str, Any]) -> Dict[str, Any]:
    for k in data.keys():
        v = data[k]
        if isinstance(v, Enum):
            data[k] = v.value
    return data
