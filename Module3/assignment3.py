import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv('/Users/zmandell/Downloads/DAT210x-master/Module3/Datasets/wheat.data')





#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Area')
ax.set_ylabel('Perimeter')
ax.set_zlabel('Asymmetry')

ax.scatter(df.area, df.perimeter, df.asymmetry, c='red', marker='.')


#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
fig = plt.figure()
ax2 = fig.add_subplot(111, projection='3d')
ax2.set_xlabel('Width')
ax2.set_ylabel('Groove')
ax2.set_zlabel('Length')

ax2.scatter(df.width, df.groove, df.length, c='green', marker='.')


plt.show()


