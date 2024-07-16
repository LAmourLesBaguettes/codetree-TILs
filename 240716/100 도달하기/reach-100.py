def generate_sequence(n):
    sequence = [1, n]
    while True:
        next_value = sequence[-1] + sequence[-2]
        if next_value > 100:
            break
        sequence.append(next_value)
    return sequence

# 입력 받기
n = int(input().strip())

# 시퀀스 생성
output_sequence = generate_sequence(n)

# 결과 출력
print(" ".join(map(str, output_sequence)))