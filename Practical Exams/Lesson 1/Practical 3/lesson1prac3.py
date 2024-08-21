data = {}
try:
    with open('work_hours.txt', 'r', encoding='utf-8') as WorkHours_File:
        for line in WorkHours_File:
            line = line.strip()
            name, salary = line.split(',')
            print(line)
except:
    print()
