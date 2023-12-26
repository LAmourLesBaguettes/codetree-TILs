class WeatherData:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

def main():
    n = int(input())
    data_list = []

    # n개의 날씨 정보 입력받기
    for _ in range(n):
        date, day, weather = input().split()
        data_list.append(WeatherData(date, day, weather))

    # 비가 오는 날 찾기
    for data in data_list:
        if data.weather == "Rain":
            print(f"{data.date} {data.day} {data.weather}")
            break

if __name__ == "__main__":
    main()