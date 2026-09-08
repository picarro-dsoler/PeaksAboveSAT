"""
query - Database query utilities with nested query support
"""
import inspect
import importlib
import pkgutil

from .Query import Query
from .QueryBank import *

__all__ = [
    'Query'
]

for module_info in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{__name__}.{module_info.name}")
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if obj.__module__ == module.__name__:
            globals()[name] = obj
            __all__.append(name)



