import matplotlib.pyplot as plt


# Sac Cyberian Population Data

Year = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
NoofStudents = [180, 36, 60, 86, 156, 220, 280]
plt.title("SAC CYBERIAN POPULATION DATA")
plt.xlabel("Year")
plt.ylabel("Students")
plt.bar(Year,NoofStudents)
plt.show()