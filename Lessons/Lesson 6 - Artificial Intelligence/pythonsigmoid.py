import numpy as np
import matplotlib.pyplot as plt

def sig(x):
    return 1/ (1 + np.exp(-x))

# x = 1.0
# print(f"{x} is equal to {sig(x)} or {sig(x):.2f}")
# x = 10.0
# print(f"{x} is equal to {sig(x)} or {sig(x):.2f}")
# x = 0.0
# print(f"{x} is equal to {sig(x)} or {sig(x):.2f}")
# x = 15.0
# print(f"{x} is equal to {sig(x)} or {sig(x):.2f}")
# x = -2.0
# print(f"{x} is equal to {sig(x)} or {sig(x):.2f}")

# x = np.linspace(-10, 10, 50)
# p = sig(x)
# plt.xlabel("x")
# plt.ylabel("Sigmoid(x)")
# plt.plot(x, p, marker = "o")
# plt.grid()
# plt.show()

x = np.linspace(1, 9, 5)
p = sig(x)
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.plot(x, p, marker = "o")
plt.grid()
plt.show()

