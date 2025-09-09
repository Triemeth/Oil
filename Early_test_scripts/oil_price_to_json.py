import pandas as pd
import json

if __name__ == "__main__":
    oil_price = pd.read_csv("../Early_data_test/DCOILBRENTEU.csv")
    oil_price_json = oil_price.to_json()

    print(oil_price_json)
