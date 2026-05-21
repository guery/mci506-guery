import pandas as pd
import os


def transform_sales_data():

    input_path = 'data/raw/sales.parquet'

    df = pd.read_parquet(input_path)

    result = (
        df
        .groupby('producto')['venta']
        .sum()
        .reset_index()
    )

    os.makedirs('data/processed', exist_ok=True)

    output_path = 'data/processed/sales_summary.parquet'

    result.to_parquet(output_path)

    print("Archivo procesado:")
    print(output_path)

    print("\nResumen:")
    print(result)


if __name__ == "__main__":
    transform_sales_data()