import matplotlib.pyplot as plt
import numpy as np

#Histogram
plt.title("Histogram-Title")
scores=np.random.normal(loc=80,scale=10,size=100)
scores=np.clip(scores,0,100)
plt.hist(scores,bins=10,
         color="tomato",
         edgecolor="black"
        )
plt.xlabel("Scores")
plt.ylabel("No. of Students")
plt.show()
