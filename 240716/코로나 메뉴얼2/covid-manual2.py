# 카운팅 배열의 1에는 A인 사람의 수가, 2에는 B가, 3에는 C가, 4에는 D가 들어감
count_arr = [0] * 5

# s와 t를 입력받은 후 카운팅 배열을 통해 각각의 빈도 저장
for _ in range(3):
	s, t = input().split()
	t = int(t)

	# type num = 분류 번호
	if t >= 37 and s == 'Y':
		type_num = 1
	elif t >= 37:
		type_num = 2
	elif s == 'Y':
		type_num = 3
	else:
		type_num = 4
		
	count_arr[type_num] += 1
	
# A부터 D까지 나온 횟수를 출력
for i in range(1, 5):
	print(count_arr[i], end=" ")
	
if count_arr[1] >= 2:
	print("E")