from importlib.metadata import metadata

from .holidays import (
    MAX_YEAR,
    MIN_YEAR,
    ColorTextCalendar,
    DateWithName,
    holidays,
    main,
)

_package_metadata = metadata(str(__package__))  # ruff:ignore[non-empty-init-module]
__version__ = _package_metadata["Version"]
__author__ = _package_metadata.get("Author-email", "")

__all__ = [
    "MAX_YEAR",
    "MIN_YEAR",
    "ColorTextCalendar",
    "DateWithName",
    "holidays",
    "main",
]
