def calculate_overlapped_distance(commands):
    position = 0
    visit_count = {}
    
    # Process each command
    for command in commands:
        distance, direction = command.split()
        distance = int(distance)
        
        if direction == "R":
            for _ in range(distance):
                if position in visit_count:
                    visit_count[position] += 1
                else:
                    visit_count[position] = 1
                position += 1
        elif direction == "L":
            for _ in range(distance):
                if position in visit_count:
                    visit_count[position] += 1
                else:
                    visit_count[position] = 1
                position -= 1
    
    # Count the length of the segments visited 2 or more times
    overlapped_distance = 0
    for count in visit_count.values():
        if count >= 2:
            overlapped_distance += 1
            
    return overlapped_distance

# Input
n = int(input().strip())
commands = [input().strip() for _ in range(n)]

# Output
result = calculate_overlapped_distance(commands)
print(result)