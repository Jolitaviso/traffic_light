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
    complete_cycle_count = 0
    last_color = None

    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            current_color = data[:3]

            if last_color:
                # cycle
                if current_color == ['0', '1', '0'] and last_color == ['1', '0', '0']:
                    complete_cycle_count += 1

            last_color = current_color

    print("Complete cycles:", complete_cycle_count)

    return complete_cycle_count

def count_lines_with_errors(file_path):
    error_count = 0
    multi_color_errors = 0
    no_color_errors = 0
    
    with open(file_path, 'r') as file:
        next(file)  
        for line in file:
            data = line.strip().split(',')
            active_colors = sum(int(color) for color in data[:3])

            if active_colors != 1: # all error
                error_count += 1

            if active_colors > 1:
                multi_color_errors += 1 
            
            if active_colors == 0:
                no_color_errors += 1

    print("Lines with errors:", error_count)
    print("Lines with mutiple colors:", multi_color_errors)
    print("Lines with no colors:", no_color_errors)
    
    return error_count, multi_color_errors, no_color_errors

file_path = 'data.txt' 

print("1. Find the number of red, yellow and green occurrences:")
color_occurrences = count_color_occurrences(file_path)
print("Color occurrences:", color_occurrences)

print("\n2. Find how long each colour was active for:")
color_times = calculate_color_active_time(file_path)
print("Color active times:", color_times)

print("\n3. Find all times when Green was active (by time):")
green_active_times = find_green_active_times(file_path)

print("\n4. Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data:")
cycle_count = count_complete_cycles(file_path)

print("\n5. Find number of lines with mistakes (multiple colours active at the same time or no colours active):")
error_count, multi_color_errors, no_color_errors = count_lines_with_errors(file_path)

