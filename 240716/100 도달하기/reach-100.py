def generate_sequence(n):
    sequence = [1, n]  # 첫 번째 항은 1, 두 번째 항은 n으로 초기화
    while True:
        next_value = sequence[-1] + sequence[-2]  # 다음 항은 전전항과 전항의 합
        if next_value > 100:  # 다음 값이 100을 넘으면 종료
            break
        sequence.append(next_value)  # 리스트에 다음 값을 추가
    return sequence

# 입력 받기
n = int(input().strip())

# 시퀀스 생성
output_sequence = generate_sequence(n)

# 결과 출력
print(" ".join(map(str, output_sequence)))