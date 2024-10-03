import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
)

if connection.is_connected():
    print("Connected to MySQL database")


def CreateOperation():
    cursor = connection.cursor()

    #Sample SQL

    insert_query = "INSERT INTO student_grade(student_name,student_id,grade) VALUES (%s,%s,%s)"
    # data = ("John Doe", 1100, "A")
    data = [
        ("John Doe", 20, "A"),
        ("Jane Smith", 22, "B"),
        ("Alice Joshson", 21, "A"),
        ("Bob Brown", 23, "C")
    ]

    cursor.executemany(insert_query, data)
    connection.commit()
    print(f"{cursor.rowcount} record(s) inserted.")
    cursor.close()

# CreateOperation()

def SelectOperation():
    cursor = connection.cursor()

    # select_query = "SELECT * FROM student_grade WHERE age = 21"
    # select_query = "SELECT * FROM student_grade WHERE  grade = 'A'"

    # ORDER BY
    select_query = "SELECT * FROM student_grade WHERE  grade = 'A' ORDER BY student_name"

    cursor.execute(select_query)

    records = cursor.fetchall()

    for row in records:
        print(row)
        # print(f"ID: {row[0]} Name: {row[1]} Age: {row[2]} Grade: {row[3]}")


SelectOperation()


