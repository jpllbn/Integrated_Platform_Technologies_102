import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cyberiandb"
)

# if connection.is_connected():
#     print("Connected to MySQL database")

data = []

def RegisterData():
    cursor = connection.cursor()

    insert_query = """INSERT INTO 
        cyberian_table(student_email,student_fullname,student_number,year_level,section)
        VALUES (%s,%s,%s,%s,%s)"""

    cursor.executemany(insert_query, data)
    connection.commit()
    print(f"{cursor.rowcount} record(s) inserted.")
    cursor.close()

def ViewYearLevel1():
    cursor = connection.cursor()

    select_query = "SELECT * FROM cyberian_table WHERE  year_level = 1"

    cursor.execute(select_query)

    records = cursor.fetchall()

    for row in records:
        print("Students in Year Level 1:")
        print(f"Email: {row[1]} Full Name: {row[2]} Student Number: {row[3]} Section: {row[5]}")

    print("No records found for Year Level 1.")

def ViewYearLevel2():
    cursor = connection.cursor()

    select_query = "SELECT * FROM cyberian_table WHERE  year_level = 2"

    cursor.execute(select_query)

    records = cursor.fetchall()

    for row in records:
        print("Students in Year Level 2:")
        print(f"Email: {row[1]} Full Name: {row[2]} Student Number: {row[3]} Section: {row[5]}")

    print("No records found for Year Level 2.")

def ViewYearLevel3():
    cursor = connection.cursor()

    select_query = "SELECT * FROM cyberian_table WHERE year_level = 3"

    cursor.execute(select_query)

    records = cursor.fetchall()

    for row in records:
        print("Students in Year Level 3:")
        print(f"Email: {row[1]} Full Name: {row[2]} Student Number: {row[3]} Section: {row[5]}")

    print("No records found for Year Level 3.")

def ViewYearLevel4():
    cursor = connection.cursor()

    select_query = "SELECT * FROM cyberian_table WHERE  year_level = 4"

    cursor.execute(select_query)

    records = cursor.fetchall()

    for row in records:
        print("Students in Year Level 4:")
        print(f"Email: {row[1]} Full Name: {row[2]} Student Number: {row[3]} Section: {row[5]}")

    print("No records found for Year Level 4.")

def main():
    try:
        print("=" * 20, "CYBERIAN REGISTRATION SYSTEM", "=" * 20)
        print("(1) REGISTER ACCOUNT")
        print("(2) VIEW DATA")
        while True:
            operation = int(input("Select an Operation (1-2): "))

            if operation not in [1, 2]:
                print("Invalid Option. Please select either 1 or 2.")
                continue

            if operation == 1:
                student_email = str(input("Enter Student Email: "))
                student_fullname = str(input("Enter Student Full Name: "))
                student_number = int(input("Enter Student Number: "))
                year_level = str(input("Enter Year Level: "))
                section = str(input("Enter Section: "))

                registered_data = student_email, student_fullname, student_number, year_level, section

                data.append(registered_data)

                add_more = input("Add more data? (Y/N): ")

                if add_more == "Y":
                    continue
                else:
                    RegisterData()
                    break
            elif operation == 2:
                year_level = int(input("Enter the Year Level (1-4): "))

                if year_level == 1:
                    ViewYearLevel1()
                    exit()
                elif year_level == 2:
                    ViewYearLevel2()
                    exit()
                elif year_level == 3:
                    ViewYearLevel3()
                    exit()
                elif year_level == 4:
                    ViewYearLevel4()
                    exit()
                else:
                    print(f"No records found for {year_level}.")
            else:
                print("Invalid input.")
            break
    except ValueError:
        print("Invalid input")

    except ModuleNotFoundError:
        print("Module not Found")





main()









main()
