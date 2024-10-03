import pandas as pd

data = []
def AskUser():
    name = input("Enter name (or type 'exit' to finish): ")
    if name.lower() == 'exit':
        return None
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))
    return name, age, salary
def WriteData():
    df = pd.DataFrame(data, columns=["Name", "Age", "Salary"])
    df.to_csv("userdata.csv", index=False)
    print("Data has been saved to 'userdata.csv'")
def main():
    while True:
        result = AskUser()
        if result is None:
            break
        name, age, salary = result
        data.append([name, age, salary])

    WriteData()
main()