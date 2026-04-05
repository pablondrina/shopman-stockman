"""
Stockman Adapters.

Implementations of protocols for external systems.
"""

from shopman.stockman.adapters.craftsman import CraftsmanBackend, get_production_backend
from shopman.stockman.adapters.noop import NoopSkuValidator
from shopman.stockman.adapters.offerman import (
    get_sku_validator,
    reset_sku_validator,
)

__all__ = [
    "CraftsmanBackend",
    "NoopSkuValidator",
    "get_production_backend",
    "get_sku_validator",
    "reset_sku_validator",
]
