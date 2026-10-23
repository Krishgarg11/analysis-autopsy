from pathlib import Path
from pprint import pprint
import pandas as pd

from inspector import inspect_dataset


if __name__ == "__main__":
    dataset_path = (
        Path(__file__).parent.parent
        / "sample_data"
        / "sales_data.csv"
    )

    result = inspect_dataset(dataset_path)
    print("Duplicate count:", pd.read_csv(dataset_path).duplicated().sum())

    print("\n========== DATASET SUMMARY ==========")
    print(f"Rows: {result['rows']}")
    print(f"Columns: {result['columns']}")

    print("\n========== INVESTIGATION FINDINGS ==========")
    pprint(result["findings"])