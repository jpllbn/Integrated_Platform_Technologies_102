import matplotlib.pyplot as plt
import numpy as np

# sample data
# x = [1,2,3,4,5]
# y = [10,15,7,10,20]
#
# plt.title("Basic Line Plot")
# plt.xlabel("X-axis label")
# plt.ylabel("Y-axis label")
# plt.plot(x,y)
# plt.show()


# No X-axis
# y = [10,15,7,10,20]
# plt.title("Basic Line Plot")
# plt.xlabel("X-axis label")
# plt.ylabel("Y-axis label")
# plt.plot(y)
# plt.show()


# Customize Design
# x = [1,2,3,4,5]
# y = [10,15,7,10,20]

# plt.title("Basic Line Plot")
# plt.xlabel("X-axis label")
# plt.ylabel("Y-axis label")

# Use to design the line
# plt.plot(x,y, linestyle="dotted")
# plt.plot(x,y, linestyle="dashed")
# plt.plot(x,y, linestyle="dashdot")

# with color
# plt.plot(x,y, linestyle="dotted", color = "red")

# with line width
# plt.plot(x,y, linestyle="dotted", color = "red", linewidth = "5")

# with Markers
# plt.plot(x,y, linestyle="dotted", color = "red", linewidth = "5", marker= "s")
#
# plt.show()

# Set Font Properties for Title and Labels

# import matplotlib.pyplot as plt
#
# x = [80,85,90,95,100]
# y = [240, 250, 260, 270, 280]
#
# font1 = {'family':'serif', 'color':'blue', 'size':20}
# font2 = {'family':'serif', 'color':'darkred', 'size':15}
#
# # plt.title("Athlete Data", fontdict=font1)
#
# # Position and Title in left
# plt.title("Athlete Data", fontdict=font1, loc="left")
# plt.xlabel("Average Pulse", fontdict=font2)
# plt.ylabel("Calorie Burnage", fontdict=font2)
# plt.plot(x,y)
# plt.show()

# Grid Lines
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.plot(x, y)
#
# plt.grid()
#
# plt.show()


# Customize Grid
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.plot(x, y)
#
# plt.grid(axis= "x")
# plt.grid(axis = "y")
# plt.grid(color = "green", linestyle = "--", linewidth = "0.5")
#
# plt.show()


# Multiple Lines
# import matplotlib.pyplot as plt
# import numpy as np
#
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
#
# plt.plot(y1, color = "red", linestyle = "dotted", marker = "s")
# plt.plot(y2, color = "blue", linestyle = "dashed", marker = "*")
#
# plt.grid(color = "green", linewidth = "2", linestyle = "dotted")
# plt.show()

# Scatter Plot
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#
# plt.title("Scatter Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
#
# plt.scatter(x, y,  color="red", marker="*", s=100)
# plt.show()

# Bar Graph
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.title("Bar Chart")
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.bar(x,y, color = "black", width = 0.4)
# plt.show()


# Histogram
# import numpy as np
#
# x = np.random.normal(170, 10, 250)
#
# print(x)
# plt.hist(x)
# plt.show()

# import matplotlib.pyplot as plt
#
# data = [1,2,2,3,3,3,3,4,4,4,4,5,5,6]
#
# # Create Histogram
# # The number of bins can be customized
#
# plt.hist(data, bins=13, color = "#333", alpha = 0.8)
# plt.title("Basic Histgram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

# Pie Chart - Data Comparison

import matplotlib.pyplot as plt
import numpy as np
label = ['A', 'B', 'C', 'D']
sizes = np.array([35, 25, 25, 15])
colors = ['yellow', 'blue', 'red', 'green']
plt.title("Pie Chart")

# autopct = '%1.1t%%' - Decimal Number
# autopct = '%1.1d%%' - Whole Number
plt.pie(sizes, labels= label, colors = colors, autopct = '%1.1d%%', shadow=True, explode = (0.1, 0,0,0))
plt.show()









