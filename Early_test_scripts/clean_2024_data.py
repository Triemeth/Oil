import pandas as pd

def read_data():
    ais_data = pd.read_csv("../Early_data_test/short_data_2024_01_02.csv")
    oil_price = pd.read_csv("../Early_data_test/DCOILBRENTEU.csv")

    oil_price = oil_price.rename(columns={'DCOILBRENTEU': 'oil_price', 'observation_date': 'date'}) 
    oil_price = oil_price.to_dict(orient='index')

    return ais_data, oil_price

def prep_AIS(ais_data, cols_to_drop):
    ais_data = ais_data.drop(columns=cols_to_drop, axis=0)

    ais_data["BaseDateTime"] = pd.to_datetime(ais_data["BaseDateTime"])
    ais_data["Date"] = ais_data["BaseDateTime"].dt.date

    return ais_data

def get_only_oil_data(ais_data):
    oil_codes = [75, 82]
    oil_ships = ais_data[prepped_ais_data["Cargo"].isin(oil_codes)]

    return oil_ships


if __name__ == "__main__":
    ais_data, oil_price = read_data()

    cols_to_drop_AIS = ["MMSI", "VesselName", "CallSign", "TransceiverClass", "IMO"]
    prepped_ais_data = prep_AIS(ais_data, cols_to_drop_AIS)

    oil_dict = {pd.to_datetime(v['date']): v['oil_price'] for v in oil_price.values()}

    prepped_ais_data["oilPrice"] = prepped_ais_data["Date"].map(oil_dict)

    oil_ships = get_only_oil_data(prepped_ais_data)

    oil_ships.to_csv("early_data_test/oil_ships.csv")