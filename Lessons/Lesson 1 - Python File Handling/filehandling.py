# Basic Syntax Coding
# var = open('file.txt','r') # open a file
# filecontent = var.read() # execute the read mode
# print(filecontent) # print the content

# Contextual Coding
# with open('file.txt','r') as var:
#     filecontent = var.readlines() # execute the read mode
#     print(filecontent)

# Looping in File Handling
# with open('student.txt', 'r') as file:
#     for line in file:
#         line = line.strip()
#         name, age, address = line.split('/ ')
#         print(f'Name: {name} Age: {age} Address: {address}')

# Looping in File Handling with Error Handling

# Write/Append Mode

# with open('file.txt', 'w') as writefile:
    # writefile.write("Hello World \n")
    # writefile.writelines(["Hello World\n", "I am John\n"])

# with open('file.txt', 'a') as appendfile:
#     appendfile.write("I am a BSIT Student\n")
#     appendfile.writelines(["My age is 18\n","I live in Brgy 8. San Jose"])
#     print("Append Successfully!")

# Exercise 1.1
# user = str(input("Enter a Name: "))
# salary = str(input("Enter a Salary: "))
#
# with open('file.txt', 'w') as file:
#     file.write(f"{user}/{salary}")
#     print("Added Successfully")

# Looping in Write Mode

# data = {}
#
# while True:
#     ask = str(input("Add Data? (Y/N): "))
#     if ask.upper() == "Y":
#         employee = str(input("Enter a Name: "))
#         salary = str(input("Enter a Salary: "))
#         data[employee] = salary
#     elif ask.upper() == "N":
#         with open('file.txt', 'w') as file:
#             for employee, salary in data.items():
#                 file.write(f"{employee}/{salary}\n")
#             print("Data Added Successfully")
#             break
#     else:
#         print("Invalid Input!")

# Looping in Write Mode with Error Handling
try:
    data = {}

    while True:
        ask = str(input("Add Data? (Y/N): "))
        if ask.upper() == "Y":
            employee = str(input("Enter a Name: "))
            salary = str(input("Enter a Salary: "))
            data[employee] = salary
        elif ask.upper() == "N":
            with open('files', 'x', encoding='utf-8') as file:
                for employee, salary in data.items():
                    file.write(f"{employee}/{salary}\n")
                print("Data Added Successfully")
                break
        else:
            print("Invalid Input!")
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to access this file.")