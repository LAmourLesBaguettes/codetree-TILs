def calculate_overlapped_distance(commands):
    position = 0
    visit_count = {}
    
    # Initialize the visit_count dictionary with the starting point
    visit_count[position] = 1
    
    # Process each command
    for command in commands:
        distance, direction = command.split()
        distance = int(distance)
        
        if direction == "R":
            for _ in range(distance):
                position += 1
                if position in visit_count:
                    visit_count[position] += 1
                else:
                    visit_count[position] = 1
        elif direction == "L":
            for _ in range(distance):
                position -= 1
                if position in visit_count:
                    visit_count[position] += 1
                else:
                    visit_count[position] = 1
    
    # Calculate the overlapped distance
    overlapped_distance = 0
    for pos, count in visit_count.items():
        if count >= 2:
            overlapped_distance += 1
            
    return overlapped_distance



result = calculate_overlapped_distance(commands)
print(result)  # Output: 6