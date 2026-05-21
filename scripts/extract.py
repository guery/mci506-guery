def extract_data(source):
    """
    Extrae datos desde una fuente.
    """
    print(f"Extrayendo datos desde: {source}")
    return {"status": "success", "rows": 1000}

# Test
if __name__ == "__main__":
    result = extract_data("database")
    print(result)