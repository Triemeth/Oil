import pandas as pd

if __name__ == "__main__":
    df = pd.read_parquet("../Early_data_test/oil_ship.parquet")

    print(df.head())