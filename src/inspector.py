import pandas as pd
from pathlib import Path


def inspect_dataset(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    df = pd.read_csv(file_path)

    findings = []

    # Check missing values
    missing_values = df.isnull().sum()

    for column, count in missing_values.items():
        if count > 0:
            findings.append({
                "type": "Missing Values",
                "column": column,
                "count": int(count),
                "severity": "Medium"
            })

    # Check duplicate rows
    duplicate_count = int(df.duplicated().sum())

    if duplicate_count > 0:
        findings.append({
            "type": "Duplicate Rows",
            "column": None,
            "count": duplicate_count,
            "severity": "Medium"
        })

    # Check negative numeric values
    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        negative_count = int((df[column] < 0).sum())

        if negative_count > 0:
            findings.append({
                "type": "Negative Values",
                "column": column,
                "count": negative_count,
                "severity": "Needs Review"
            })

    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "findings": findings
    }