"""
Outlier detection functions.
"""

from .descriptive import percentile


def iqr(data):
    """
    Return the Interquartile Range (IQR) of the data.
    """
    if not data:
        raise ValueError("Data list cannot be empty.")

    q1 = percentile(data, 25)
    q3 = percentile(data, 75)
    return q3 - q1


# def detect_outliers(data):
def detect_outliers_iqr(data):

    """
    Return a list of outliers using the IQR method.
    """
    if not data:
        raise ValueError("Data list cannot be empty.")

    q1 = percentile(data, 25)
    q3 = percentile(data, 75)
    iqr_value = q3 - q1

    lower_bound = q1 - 1.5 * iqr_value
    upper_bound = q3 + 1.5 * iqr_value

    return [x for x in data if x < lower_bound or x > upper_bound]
