# Name
# Age
# Address
try:
    student_data = []

    while True:
        ask = str(input("Add Student Data? (Y/N): "))
        if ask.upper() == "Y":
            FullName = str(input("Enter  a Full Name: "))
            Age = str(input("Enter  Age: "))
            Address = str(input("Enter  Address: "))
            student_data.append(FullName)
            student_data.append(Age)
            student_data.append(Address)
        elif ask.upper() == "N":
            with open('enrollment.txt', 'w', encoding='utf-8') as AddStudent:
                for FullName, Age, Address in student_data:
                    AddStudent.write(f"{FullName}, {Age}, {Address}\n")
                print("Data has been saved to enrollment.txt. Thank you!")
                break
        else:
            print("Invalid Input!, Please enter Y or N")
except FileNotFoundError:
    print("The file does not exist.")