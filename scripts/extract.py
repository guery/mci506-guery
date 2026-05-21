import pandas as pd
import random
import os


def generate_sales_data():

    data = {
        'producto': [random.choice(['A', 'B', 'C']) for _ in range(10)],
        'venta': [random.randint(50, 100) for _ in range(10)]
    }

    df = pd.DataFrame(data)

    os.makedirs('data/raw', exist_ok=True)

    output_path = 'data/raw/sales.parquet'

    df.to_parquet(output_path)

    print("Archivo generado:")
    print(output_path)

    print("\nDatos:")
    print(df)


if __name__ == "__main__":
    generate_sales_data()