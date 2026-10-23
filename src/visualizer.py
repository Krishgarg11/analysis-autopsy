import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def generate_graphs(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    df = pd.read_csv(file_path)

    output_dir = Path(__file__).parent.parent / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Graph 1: Product-wise sales
    if {"Product", "Sales"}.issubset(df.columns):
        sales_data = df.dropna(subset=["Product", "Sales"])

        product_sales = sales_data.groupby("Product")["Sales"].sum()

        plt.figure(figsize=(8, 5))
        product_sales.plot(kind="bar")

        plt.title("Total Sales by Product")
        plt.xlabel("Product")
        plt.ylabel("Total Sales")
        plt.tight_layout()

        plt.savefig(output_dir / "product_sales.png")
        plt.close()

        print("Created: product_sales.png")

    # Graph 2: Numerical column distributions
    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        plt.figure(figsize=(8, 5))
        df[column].dropna().plot(kind="hist", bins=10)

        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.tight_layout()

        filename = f"{column.lower()}_distribution.png"
        plt.savefig(output_dir / filename)
        plt.close()

        print(f"Created: {filename}")


if __name__ == "__main__":
    dataset_path = (
        Path(__file__).parent.parent
        / "sample_data"
        / "sales_data.csv"
    )

    generate_graphs(dataset_path)