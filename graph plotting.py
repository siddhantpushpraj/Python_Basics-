import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
'''
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)
plt.xlabel('x-a axis')
plt.ylabel('y-axis')
plt.title('my first graph plotting')
plt._show()
'''
'''
x1=[1,2,3,4,5,6]
y1=[2,4,1,6,9,10]
plt.plot(x1,y1,label="line1")
x2=[1,2,3,5,6,5]
y2=[4,1,3,6,2,8]
plt.plot(x2,y2,label="line2")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("drawing lines")
plt.legend()
plt.show()
'''
'''
x=[1,2,3,4,5,6]
y=[2,4,1,5,2,6]
plt.plot(x,y,color='green',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='blue',markersize='12')
plt.xlim(1,8)
plt.ylim(1,8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('customization')
plt.show()
'''
'''
left=[1,2,3,4,5]
height=[10,24,36,40,50]
tick_label=['one','two','three','four','five']
plt.bar(left,height,tick_label=tick_label,width=0.8,color=['red','green'])
plt.xlabel('left')
plt.ylabel('height')
plt.title('Bar graph')
plt.show()
'''
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')