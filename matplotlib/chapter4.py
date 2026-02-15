import matplotlib.pyplot as plt

# Bar chart
categories=["Grains","Fruits","Vagetables","Protins","Dariy","Sweets"]
values=[4,3,2,5,3,1]

plt.title("Daily Consumption")
plt.bar(categories,values,color="tomato")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()
