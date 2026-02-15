import matplotlib.pyplot as plt

x=[10,20,40,68]
y=[2025, 2027, 2029, 2045]
plt.title("Mytitle")
plt.plot(x,y)
plt.grid(
    axis="y",
    linewidth=2,
    color="lightgray",
    linestyle="dashed"
)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
