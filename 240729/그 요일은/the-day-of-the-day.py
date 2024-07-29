# Variables and input
m1, d1, m2, d2 = tuple(map(int, input().split()))

# Function to calculate the number of days from the start of the year
def num_of_days(m, d):
    # List representing the number of days in each month (0 index ignored)
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    # Summing up days from January to (m-1) months
    for i in range(1, m):
        total_days += days[i]
    
    # Adding days of the current month
    total_days += d
    
    return total_days    

# Calculate the difference in days between the two dates
diff = num_of_days(m2, d2) - num_of_days(m1, d1)

# Ensure the difference is non-negative by adding 7 if needed
while diff < 0:
    diff += 7

# List of day names
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Print the resulting day of the week
print(day_of_week[diff % 7])