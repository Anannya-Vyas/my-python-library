from stattools import mean, median, percentile, iqr, detect_outliers_iqr

def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3.0

def test_median():
    assert median([1, 2, 3, 4, 5]) == 3

def test_percentile():
    assert percentile([10, 20, 30, 40, 50], 50) == 30

def test_iqr():
    assert iqr([10, 20, 30, 40, 50]) == 20

def test_outliers():
    data = [10, 12, 14, 16, 100]
    assert detect_outliers_iqr(data) == [100]
