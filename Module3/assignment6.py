import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv('/Users/zmandell/Downloads/DAT210x-master/Module3/Datasets/wheat.data')

#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# 
df.drop(['id'], axis=1, inplace=True)


#
# TODO: Compute the correlation matrix of your dataframe
# 
#df = df.corr()


#
# TODO: Graph the correlation matrix using imshow or matshow
# 

plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
tick_marks = [i for i in range(len(df.columns)-1)]
plt.xticks(tick_marks,df.columns,rotation='vertical')
plt.yticks(tick_marks,df.columns)
plt.colorbar()
plt.show()


