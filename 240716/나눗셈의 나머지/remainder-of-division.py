def calculate_remainder_sum(a, b):
    remainder_count = [0] * b  # 나머지들의 등장 횟수를 저장할 리스트

    while a > 1:
        remainder = a % b
        remainder_count[remainder] += 1
        a //= b

    # 각 나머지의 등장 횟수를 제곱하여 합산
    result = sum(count ** 2 for count in remainder_count)
    
    return result

# 입력 받기
a, b = map(int, input().split())

# 결과 계산 및 출력
print(calculate_remainder_sum(a, b))