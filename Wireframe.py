from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection = '3d')

#Generates random data
x,y,z = axes3d.get_test_data(0.05)
ax.plot_wireframe(x,y,z,rstride=10,cstride=10)

ax.set_title('Wireframe example',color='orange')
ax.set_ylabel('Y-axis',color ='pink')
ax.set_xlabel('X-axis',color ='red')
ax.set_zlabel('Z-axis',color='cyan')

plt.show()
