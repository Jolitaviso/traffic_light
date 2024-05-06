def count_color_occurrences(file_path):
    red_count = 0
    yellow_count = 0
    green_count = 0

    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            red_count += int(data[0])
            yellow_count += int(data[1])
            green_count += int(data[2])

    print("Red =", red_count)
    print("Yellow =", yellow_count)
    print("Green =", green_count)

    return {'Red': red_count, 'Yellow': yellow_count, 'Green': green_count}

def calculate_color_active_time(file_path):
    red_time = 0
    yellow_time = 0
    green_time = 0

    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            time_active = int(data[3])
            if data[0] == '1':
                red_time += time_active
            elif data[1] == '1':
                yellow_time += time_active
            elif data[2] == '1':
                green_time += time_active

    print("Red active time =", red_time, "seconds")
    print("Yellow active time =", yellow_time, "seconds")
    print("Green active time =", green_time, "seconds")

    return {'Red': red_time, 'Yellow': yellow_time, 'Green': green_time}

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

    with open(file_path, 'r') as file:
        next(file)  
        for line in file:
            data = line.strip().split(',')
            active_colors = sum(int(color) for color in data[:3])

            # error
            if active_colors != 1:
                error_count += 1

    print("Lines with errors:", error_count)

    return error_count

file_path = 'data.txt' 

print("1. Find the number of red, yellow and green occurrences:")
color_occurrences = count_color_occurrences(file_path)

print("\n2. Find how long each colour was active for:")
color_active_time = calculate_color_active_time(file_path)

print("\n3. Find all times when Green was active (by time):")
green_active_times = find_green_active_times(file_path)

print("\n4. Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data:")
cycle_count = count_complete_cycles(file_path)

print("\n5. Find number of lines with mistakes (multiple colours active at the same time or no colours active):")
error_count = count_lines_with_errors(file_path)
