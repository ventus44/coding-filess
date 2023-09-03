import matplotlib.pyplot as plt
#those two lists hold the cordinates for the left side of the bar 
left = [1, 2, 3, 4, 5]
height = [10, 11, 23, 36, 4]
#this list holds the label for every bar that is going to be displayed on the x axis
tick_label = ["one", "two", "three", "four", "five"]
#this line sets the height width and color of the bar
plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ["blue", "orange"])
#the two next lines label the y and y axels
plt.xlabel("X Axel")

plt.ylabel("Y Axel")

#this line adds the demograph bar chart to the chart
plt.title("Demo Graph - Bar Chart")


#this line displays the figure until the function is called 
plt.show()