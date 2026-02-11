"""
Descriptive statistics functions.
"""

def mean(data):
    """
    Return the arithmetic mean of a list of numbers.
    """
    if not data:
        raise ValueError("Data list cannot be empty.")
    return sum(data) / len(data)


def median(data):
    """
    Return the median of a list of numbers.
    """
    if not data:
        raise ValueError("Data list cannot be empty.")

    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]


def percentile(data, p):
    """
    Return the pth percentile of a list of numbers.
    p should be between 0 and 100.
    """
    if not data:
        raise ValueError("Data list cannot be empty.")

    if not (0 <= p <= 100):
        raise ValueError("Percentile must be between 0 and 100.")

    sorted_data = sorted(data)
    k = (len(sorted_data) - 1) * (p / 100)
    f = int(k)
    c = f + 1

    if c >= len(sorted_data):
        return sorted_data[f]

    return sorted_data[f] + (k - f) * (sorted_data[c] - sorted_data[f])
