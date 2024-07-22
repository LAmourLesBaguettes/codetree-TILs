import datetime
n = int(input().strip())

forcast_data = []

for _ in range(n):
    data_str, weekday, weather = input().strip().split()
    forcast_data.append((data_str, weekday, weather))

earliest_rain_data = None
earliest_rain_info = None

for data_str, weekday, weather in forcast_data:
    if weather == "Rain":
        current_data = datetime.datetime.strptime(data_str, "%Y-%m-%d")
        if earliest_rain_data is None or current_data < earliest_rain_data:
            earliest_rain_data = current_data
            earliest_rain_info = (data_str, weekday, weather)

if earliest_rain_info:
    print(" ".join(earliest_rain_info))