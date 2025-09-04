import json

if __name__ == "__main__":

    start_string = "https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2024/"

    dat = { "url_list": []}

    months_30_days = [4, 6, 9, 11]

    for i in range(1, 13):

        if i in months_30_days:
            j_range = 30
        elif i == 2:
            j_range = 29
        else:
            j_range = 31

        for j in range(1, j_range + 1):
            if j < 10 and i < 10:
                dat["url_list"].append(f"{start_string}AIS_2024_0{i}_0{j}.zip")
            elif j < 10 and i >= 10:
                dat["url_list"].append(f"{start_string}AIS_2024_{i}_0{j}.zip")
            elif j >= 10 and i < 10:
                dat["url_list"].append(f"{start_string}AIS_2024_0{i}_{j}.zip")
            else:
                dat["url_list"].append(f"{start_string}AIS_2024_{i}_{j}.zip")

    with open("early_data_test/url.json", "w") as json_file:
        json.dump(dat, json_file, indent=4)
