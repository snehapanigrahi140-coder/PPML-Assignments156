import matplotlib.pyplot as plt
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]
plt.hist(data, bins=5, label="Histogram data")
plt.title("Histogram"); plt.xlabel("Bins"); plt.ylabel("Frequency")
plt.legend(); plt.show()
plt.boxplot(data)
plt.title("Box Plot"); plt.show()
