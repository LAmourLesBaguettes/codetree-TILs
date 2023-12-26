class objcode:
    def __init__(self, name, code):
        self.name = name
        self.code = code

def main():

    objcode1 = objcode('codetree', 50) 

    name, code = input().split()

    objcode2 = objcode(name, int(code))

    print(f"product {objcode1.code} is {objcode1.name}")
    print(f"product {objcode2.code} is {objcode2.name}")

if __name__ == "__main__":
    main()