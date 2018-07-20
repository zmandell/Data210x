import pandas as pd
# TODO: Load up the 'tutorial.csv' dataset
#
# .. your code here ..
df = pd.read_csv('/Users/zmandell/Downloads/DAT210x-master/Module2/Datasets/tutorial.csv')


# TODO: Print the results of the .describe() method
#
print(df.describe())
print('\n')
print(df)
print('\n')


# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
print(df.loc[2:4,'col3'])
# .. your code here ..

