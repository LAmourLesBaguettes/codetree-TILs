start_day = 11
start_hour = 11
start_minute = 11
start_total_minutes = start_day * 24 * 60 + start_hour*60 + start_minute

a, b, c = map(int, input().split())

end_total_minutes = a*24*60 + b*60 + c

elapsed_minutes = end_total_minutes - start_total_minutes

if elapsed_minutes < 0:
    print(-1)
else:
    print(elapsed_minutes)