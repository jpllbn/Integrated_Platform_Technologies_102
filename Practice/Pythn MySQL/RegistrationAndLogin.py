import mysql.connector

# Database connection setup
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="logindb"
)

# Registration function to insert user data into the database
def Registration(name, username, password):
    try:
        cursor = connection.cursor()

        # Query to insert new user into login_table
        insert_query = """INSERT INTO login_table(name, username, password)
                          VALUES (%s, %s, %s)"""

        data = (name, username, password)

        cursor.execute(insert_query, data)
        connection.commit()

        print("Registered Successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

# Login function to check credentials from the database
def Login(username, password):
    try:
        cursor = connection.cursor()

        # Query to select user data matching the input username and password
        select_query = "SELECT * FROM login_table WHERE username=%s AND password=%s"
        cursor.execute(select_query, (username, password))

        # Fetch result
        result = cursor.fetchall()

        if result:
            print("Log in Successful")
            for row in result:
                print(f"Welcome {row[1]}")
        else:
            print("Log in Failed")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

# Main menu and options
def main():
    print("=" * 10, "WELCOME TO THE SYSTEM", "=" * 10)
    print("[1] Register an Account")
    print("[2] Login")
    print("[0] Exit")

    while True:
        option = input("Enter an option (1-2): ")
        if option not in ['1', '2', '0']:
            print("Invalid selection. Try again.")
            continue

        if option == '1':
            name = input("Enter Name: ").strip()
            username = input("Enter Username: ").strip()
            password = input("Enter Password: ").strip()

            # Validate input to ensure no empty values
            if not name or not username or not password:
                print("All fields are required. Try again!")
                continue

            Registration(name, username, password)
        elif option == '2':
            username = input("Enter Username: ").strip()
            password = input("Enter Password: ").strip()

            # Validate input to ensure no empty values
            if not username or not password:
                print("Username and Password are required. Try again!")
                continue

            Login(username, password)
            break
        elif option == '0':
            print("Exiting...")
            break

main()
