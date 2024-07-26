a,b,c,d = map(int, input().split())

start_time_minute = a * 60 + b
end_time_minute = c * 60 + d

elapsed_minute = end_time_minute - start_time_minute

print(elapsed_minute)