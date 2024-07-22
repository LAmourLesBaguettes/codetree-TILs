# 사용자 클래스를 정의합니다.
class User:
    def __init__(self, user_id, level):
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f"user {self.user_id} lv {self.level}"

# 첫 번째 객체는 미리 정의된 값으로 초기화합니다.
user1 = User("codetree", 10)

# 두 번째 객체는 입력받은 값으로 초기화합니다.
user_id, level = input().split()
user2 = User(user_id, int(level))

# 결과를 출력합니다.
print(user1)
print(user2)