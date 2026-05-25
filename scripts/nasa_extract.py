import os
import requests
import pandas as pd
from pathlib import Path


API_KEY = os.getenv("NASA_API_KEY")

if not API_KEY:
    raise ValueError("No se encontró la variable NASA_API_KEY")


def main():
    url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": API_KEY
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame([data])

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "nasa_apod.parquet"

    df.to_parquet(output_path, index=False)

    print("Datos descargados correctamente")
    print(df[["date", "title", "media_type"]])
    print(f"Archivo generado: {output_path}")


if __name__ == "__main__":
    main()