class Day:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c


def main():
    n = int(input())
    day_list = []

    for _ in range(n):
        a, b, c = input().split()
        day_list.append(Day(a,b,c))

    
    for day in day_list:
        if day.c == "Rain":
            print(f"{day.a} {day.b} {day.c}")
            break
if __name__ == "__main__":
    main()