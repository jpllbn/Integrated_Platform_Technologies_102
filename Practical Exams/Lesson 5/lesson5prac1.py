import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('student_grades.csv')
df = pd.DataFrame(data)

Name = df['Name']
Math = df['Math']
Science = df['Science']
English = df['English']
History = df['History']
Physical_Education = df['Physical_Education']

average = (Math + Science + English + History + Physical_Education) / 5

newdata = {
    'Name': [Name],
    'Math': [Math],
    'Science': [50000, 60000, 70000],
    'English': [English],
    'History': [History],
    'Physical Education': [Physical_Education],
    'Average': [average]
}

print(df)


# Bar Graph

# import matplotlib.pyplot as plt
# import pandas as pd
#
# df = pd.read_csv('student_grades.csv')
#
# plt.title("Students Average Grades")
# plt.xlabel("student names ")
# plt.ylabel("Average Grade")
# plt.bar(color = "black", width = 0.4)
# plt.show()


# Line Plot
import matplotlib.pyplot as plt
import pandas as pd

# Reading the CSV
df = pd.read_csv('student_grades.csv')


# Extract Data

name = df['Name']
Math = df['Math']
Science = df['Science']
English = df['English']
History = df['History']
Physical_Education = df['Physical_Education']

plt.plot(name, Math, label="Math", marker='o', color="red")
plt.plot(name, Science, label="Science", marker='x', color="green")
plt.plot(name, English, label="English", marker='o', color="blue")
plt.plot(name, History, label="History", marker='x', color="black")
plt.plot(name, Physical_Education, label="Physical Education", marker='o', color="green")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

plt.title("Student's Average Grade")
plt.xlabel("Students")
plt.ylabel("Grades")
plt.legend(title="Legend:")
plt.tight_layout()
plt.show()
