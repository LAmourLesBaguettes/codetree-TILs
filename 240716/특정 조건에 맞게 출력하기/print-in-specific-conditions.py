def process_numbers(numbers):
    result = []
    for number in numbers:
        if number == 0:
            break
        if number % 2 == 0:
            result.append(number // 2)
        else:
            result.append(number + 3)
    return result

# 입력 받기
input_numbers = list(map(int, input().strip().split()))

# 숫자 처리
output_numbers = process_numbers(input_numbers)

# 결과 출력
print(" ".join(map(str, output_numbers)))