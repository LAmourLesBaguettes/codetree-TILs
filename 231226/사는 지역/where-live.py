class region:
    def __init__ (self, name, num, place):
        self.name = name
        self.num = num
        self.place = place


def main():
    n = int(input())
    people = []

    for _ in range(n):
        name,num, place =input().split()
        people.append(region(name, num, place))

    people.sort(key = lambda x: x.name)

    slowest_person = people[-1]
    print(f"name {slowest_person.name}")
    print(f"addr {slowest_person.num}")
    print(f"city {slowest_person.place}")

if __name__ == "__main__":
    main()