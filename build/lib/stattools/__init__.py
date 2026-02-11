"""
StatTools - A lightweight statistics library.
"""

from .descriptive import mean, median, percentile
from .outliers import iqr, detect_outliers

__all__ = ["mean", "median", "percentile", "iqr", "detect_outliers"]
