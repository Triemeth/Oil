import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../Early_data_test/oil_ships.csv")

    df.to_parquet('../Early_data_test/oil_ship.parquet')