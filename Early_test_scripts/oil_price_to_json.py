import pandas as pd
import json

if __name__ == "__main__":
    oil_price = pd.read_csv("../Early_data_test/DCOILBRENTEU.csv")
    oil_price_dict = oil_price.to_dict(orient='index')

    with open("../Early_data_test/oil_price.json", "w") as json_file:
        json.dump(oil_price_dict, json_file, indent=4)


#py -3.12 oil_price_to_json.py