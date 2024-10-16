import mysql.connector


connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database = "cyberiandb"
)

# if connection.is_connected():
#     print("connected")

def RegisterData():
    cursor = connection.cursor()

    # insert_query

def ViewData():
    pass

def main():
    print("="*20, "CYBERIAN REGISTRATION SYSTEM", "="*20)
    print("(1) REGISTER STUDENT")
    print("(2) VIEW DATA")

    operation = int(input("Select an Operation (1 or 2: "))

    while True:
        if operation == 1:
            student_email = str(input("Enter Student Email: "))
            student_full_name = str(input("Enter Student Full Name: "))
            student_number = int(input("Enter Student Number: "))
            year_level = int(input("Enter Year Level: "))
            student_section = str(input("Enter Section: "))
        elif operation == 2:
            pass

        if operation not in [1,2]:
            continue

        add_more_data = str(input("Add more data? (Y/N): "))

        if add_more_data == "Y":
            continue
        else:
            pass

main()

