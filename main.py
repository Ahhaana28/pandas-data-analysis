import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

print(data)

print("Average Marks:", data["Marks"].mean())

plt.bar(data["Name"], data["Marks"])
plt.title("Student Marks")
plt.show()

plt.scatter(data["Age"], data["Marks"])
plt.title("Age vs Marks")
plt.show()

plt.imshow(data.corr(numeric_only=True))
plt.colorbar()
plt.title("Heatmap")
plt.show()