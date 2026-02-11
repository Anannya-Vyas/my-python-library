![PyPI version](https://img.shields.io/pypi/v/stattools-anannya)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

# 📊 StatTools

StatTools is a lightweight Python statistics library that provides basic descriptive statistics and outlier detection utilities.

It is designed for learning, projects, and simple statistical analysis without heavy dependencies.

---

## ✨ Features

- Mean
- Median
- Percentile
- Interquartile Range (IQR)
- Outlier detection using IQR method

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Anannya-Vyas/my-python-library.git
cd my-python-library
```

Install in editable mode:

```bash
pip install -e .
```

---

## 🚀 Usage

```python
from stattools import mean, median, percentile, iqr, detect_outliers_iqr

data = [10, 20, 30, 40, 100]

print("Mean:", mean(data))
print("Median:", median(data))
print("50th Percentile:", percentile(data, 50))
print("IQR:", iqr(data))
print("Outliers:", detect_outliers_iqr(data))
```

---

## 📘 Example

```python
data = [5, 7, 8, 10, 12, 100]

# Detect outliers
outliers = detect_outliers_iqr(data)
print(outliers)
```

Output:

```
[100]
```

---

## 🧪 Running Tests

```bash
python -m pytest
```

All tests should pass successfully.

---

## 📁 Project Structure

```
stattools/
    __init__.py
    descriptive.py
    outliers.py
tests/
    test_stattools.py
setup.py
README.md
```

---

## 👩‍💻 Author

Anannya Vyas  
GitHub: https://github.com/Anannya-Vyas

---

## 📄 License

This project is open-source and available under the MIT License.
