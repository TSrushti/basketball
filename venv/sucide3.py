import matplotlib.pyplot as plt
#X- Cordinates of left side of bars
left = [1, 2, 3, 4, 5]

#heights of bars
height = [10, 20, 30, 20, 5]

#labels for bars
label = ['one', 'two', 'three','four', 'five']

#plotting a bar chart
plt.bar(left, height, label = label, width =0.8, color = ['red' , 'green'])

#naming the x-axis
plt.xlabel('x - axis')

#naming the y axis
plt.ylabel('y - axis')

#plot title
plt.title('My bar chart!')

#function to show the plot
plt.show()