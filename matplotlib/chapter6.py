import matplotlib.pyplot as plt

#Scatter plot
x=[0,1,1,2,3,4,5,6,8]
y=[55,60,65,62,68,70,75,80,85]

x1=[2,3,5,6,2,3,6,7,3]
y1=[85,29,35,72,28,50,65,65,35]
plt.title("Scatter Plot")
plt.scatter(x,y,color="tomato", # color
            alpha=0.5,  # transperancy
            s=200,   # size of each dot
            label="Class A"
            )
plt.scatter(x1,y1,color="green",
            alpha=0.5,
            s=200,
            label="Class B"
            )
plt.legend()
plt.xlabel("Hours Studied")
plt.ylabel("Grades")
plt.show()
