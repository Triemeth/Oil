
if __name__ == "__main__":

    month_count = 0
    day_count = 0

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
                print(f"AIS_2024_0{i}_0{j}")
            elif j < 10 and i >= 10:
                print(f"AIS_2024_{i}_0{j}")
            elif j >= 10 and i < 10:
                print(f"AIS_2024_0{i}_{j}")
            else:
                print(f"AIS_2024_{i}_{j}")

            day_count = day_count + 1

        month_count = month_count + 1
        
    print("Day count:", day_count)
    print("Month count:", month_count)
