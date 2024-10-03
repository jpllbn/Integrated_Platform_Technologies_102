import pandas as pd


def DisplayEmployee():
    data = {
        'ID': [],
        'Name': [],
        'Department': []
    }

    df = pd.read_csv('employee.csv')

    newdata = {
        'ID': [],
        'Salary': []
    }


    newdf = pd.read_csv('salary.csv')

    df1 = pd.DataFrame({'Key': ['ID', 'Salary'], 'Value1': [newdata['ID'], newdata['Salary']]})
    df2 = pd.DataFrame({'Key': ['ID', 'Name', 'Department'], 'Value1': [data['ID'], data['Name'], data['Department']]})

    dfMerge = pd.merge(df1, df2, on='Key', how='outer')

    print(df1)
    print(df2)
    print(dfMerge)

def DisplayStaticticalData():
    pass


def main():
    DisplayEmployee()
main()