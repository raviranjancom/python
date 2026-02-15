import matplotlib.pyplot as plt

# Pie chart
categories=["Freshmen", "Sophomores", "Juniors", "Seniors"]
values=[300,250,275,225]
colors=["red","blue","brown","orange"]

plt.pie(values, # values for segmenting each piece
        labels=categories, # label names
        autopct="%1.1f%%", # to give % values values after %age sign gives number of decimal precision values 
        colors=colors,  # for coloring each segment
        explode=[0,0,0,0.1],    # to pop-out or highlight segment
        shadow=True,    # shadow
        startangle=90   # rotating takes deg
        )
plt.title("Bro Code")
plt.show()
