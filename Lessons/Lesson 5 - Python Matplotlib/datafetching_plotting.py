# Python Advanced Plotting

# Health Data
# import matplotlib.pyplot as plt
# import pandas as pd
#
# df = pd.read_csv('health.csv')
#
# ax = df.plot()
#
# plt.title("Health Data Overview")
# plt.xlabel("Index")
# plt.ylabel("Values")
# plt.legend(title="Legend:")
# plt.tight_layout()
# plt.show()


# Sales

import matplotlib.pyplot as plt
import pandas as pd

# Reading the CSV
df = pd.read_csv('sales.csv')


# Extract Data

dates = df['Date']
sales = df['Sales']
profit = df['Profit']

plt.plot(dates, sales, label="Sales", marker='o', color="blue")
plt.plot(dates, profit, label="Profit", marker='x', color="green")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

plt.title("Sales and Profit Over Time")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.legend(title="Legend:")
plt.tight_layout()
plt.show()
