import pandas as pd
import json

if __name__ == "__main__":
    
    oil_price = pd.read_csv("../Early_data_test/DCOILBRENTEU.csv")

    dat = { "oil_prices": []}

    print(oil_price.tail())
    print(oil_price.head())

    for i in range(0, len(oil_price)):
        row = {
            "observation_date": oil_price["observation_date"].iloc[i],
            "Price": oil_price["DCOILBRENTEU"].iloc[i]
        }

        dat["oil_prices"].append(row)

    with open("../Early_data_test/oil_price.json", "w") as json_file:
        json.dump(dat, json_file, indent=4)

#py -3.12 oil_price_to_json.py