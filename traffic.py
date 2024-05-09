def count_color_occurrences(file_path):
    color_counts = {'Red': 0, 'Yellow': 0, 'Green': 0}
    
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            color_counts['Red'] += int(data[0])
            color_counts['Yellow'] += int(data[1])
            color_counts['Green'] += int(data[2])
              
    return color_counts   
    
def calculate_color_active_time(file_path):
    color_times = {'Red': 0, 'Yellow': 0, 'Green': 0}

    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            time_active = int(data[3])
            color = ['Red', 'Yellow', 'Green'][data.index('1')]
            color_times[color] += time_active

    return color_times

def find_green_active_times(file_path):
    green_active_times = []

    with open(file_path, 'r') as file:
        next(file) 
        for line in file:
            data = line.strip().split(',')
            if data[2] == '1':
                green_active_times.append(data[4])

    print("Green active times:", green_active_times)

    return green_active_times

def count_complete_cycles(file_path):
    
    with open(file_path, 'r') as file:
        data = [line.strip().split(',')[:3] for line in file.readlines()]
        
    complete_cycle_count = 0
      
    for i in range(len(data)):
        if data[i]== ['1','0','0'] and \
            data[(i+1) % len(data)] == ['0', '1', '0'] and \
            data[(i+2) % len(data)] == ['0', '0', '1'] and \
            data[(i+3) % len(data)] == ['0', '1', '0'] and \
            data[(i+4) % len(data)] == ['1', '0', '0']:
                complete_cycle_count += 1

    return complete_cycle_count

def count_lines_with_errors(file_path):
    error_count = 0

    with open(file_path, 'r') as file:
        next(file)  
        for line_num, line in enumerate(file, start=2):
            data = line.strip().split(',')
            active_colors = sum(int(color) for color in data[:3])

            if active_colors != 1:
                """print(f"Line with errors {line_num}: {line.strip()}")""" #We can check the error lines
                error_count += 1

    print("Lines with errors:", error_count)
 
    return error_count

file_path = 'data.txt' 

print("1.Find the number of RED, YELLOW and GREEN occurrences:")
color_occurrences = count_color_occurrences(file_path)
print("Color occurrences:", color_occurrences)

print("\n2. Find how long each colour was active for:")
color_times = calculate_color_active_time(file_path)
print("Color active times:", color_times)

print("\n3. Find all times when GREEN was active (by time):")
green_active_times = find_green_active_times(file_path)

print("\n4. Find the number of complete cycles RED-YELLOW-GREEN-YELLOW-RED in the data:")
cycle_count = count_complete_cycles(file_path)
print("RED-YELLOW-GREEN-YELLOW-RED cycles:", cycle_count)

print("\n5. Find number of lines with mistakes:")
error_count = count_lines_with_errors(file_path)

