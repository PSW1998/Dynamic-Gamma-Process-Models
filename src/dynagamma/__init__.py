# Add package skeleton: src/dynagamma/init.py
from .core import greet, square    # import it here so users can call dynagamma.square

__all__: list[str] = ["greet", "square"]
__version__ = "0.1.0"
