import matplotlib.pyplot as plt

x=[10,20,25,89]
y=[2000,3000,3500,5000]

# plt.plot(x,y,marker=".", markersize=30, markerfacecolor="cyan",markeredgecolor="red",linestyle="dashed",linewidth=4,color="green")
lineStyle=dict(marker=".", markersize=30, markerfacecolor="cyan",markeredgecolor="red",linestyle="dashed",linewidth=4)
titleStyle=dict(fontsize=20,
                family="Arial",
                fontweight="bold",
                color="green"
                )
plt.xlabel("year",**titleStyle)
plt.title("MyTitle",**titleStyle)
plt.plot(x,y,color="green",**lineStyle)  # unpacking to use it
plt.tick_params(axis="both",colors="blue")
plt.xticks(x)
plt.show()
