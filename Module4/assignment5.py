import numpy as np
import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')

# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
colors = []
samples = [] 
files = np.arange(356)
files = files[::5]



#r = 0    
#img = misc.imread('/Users/zmandell/Downloads/DAT210x-master/Module4/Datasets/ALOI/32/32_r'+str(r)+'.png')
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#


for fname in files:
    img = misc.imread('/Users/zmandell/Downloads/DAT210x-master/Module4/Datasets/ALOI/32/32_r'+str(fname)+'.png')
    samples.append(  (img[::2, ::2] / 255.0).reshape(-1)  )
    colors.append('b')


#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
"""files2 = np.arange(221)
files2 = files2[110:221:10]
for fname in files2:
    img = misc.imread('/Users/zmandell/Downloads/DAT210x-master/Module4/Datasets/ALOI/32i/32_i'+str(fname)+'.png')
    samples.append(  (img[::2, ::2] / 255.0).reshape(-1)  )
    colors.append('r')
"""
#
# TODO: Convert the list to a dataframe
#
df = pd.DataFrame(samples)



#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
from sklearn import manifold
iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
manifold = iso.transform(df)





#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Isomap')
ax.scatter(manifold[:,0], manifold[:,1], c=colors, marker='.', alpha=0.75)




#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.set_xlabel('0')
#ax.set_ylabel('Perimeter')
#ax.set_zlabel('Asymmetry')

ax.scatter(manifold[:,0], manifold[:,1], manifold[:,2], c=colors, marker='.')


plt.show()

