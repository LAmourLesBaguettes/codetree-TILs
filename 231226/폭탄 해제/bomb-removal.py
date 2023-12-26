class bomd:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

    def display(self):
        print(f"code : {self.code}")
        print(f"color : {self.color}")
        print(f"second : {self.second}")

def main():
    code, color, second = input().split()
    obj = bomd(code, color, int(second))
    obj.display()

if __name__ == "__main__":
    main()