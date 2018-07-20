#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


X = pd.read_csv('/Users/zach.mandell/Downloads/DAT210x-master/Module6/Datasets/parkinsons.data')
X.drop(['name'],inplace=True, axis=1)
y = X.status
X.drop(['status'],inplace=True, axis=1)



'''Normalizer(), The highest score obtained: 0.796610169492
C value: 0.05
gamma value: 0.001, 
MaxAbsScaler(), The highest score obtained: 0.881355932203
C value: 1.2
gamma value: 0.098
MinMaxScaler(), The highest score obtained: 0.881355932203
C value: 0.75
gamma value: 0.097
KernelCenterer(), The highest score obtained: 0.915254237288
C value: 1.7
gamma value: 0.006
StandardScaler(), The highest score obtained: 0.932203389831
C value: 1.55
gamma value: 0.097
'''

norm = preprocessing.StandardScaler().fit(X_train)
X_train_norm = norm.transform(X_train)
X_test_norm = norm.transform(X_test)


from sklearn.svm import SVC
svc = SVC()

'''
svc.fit(X_train, y_train) 
score = svc.score(X_test,y_test)
print(score)
'''


best_score = 0
from sklearn.manifold import Isomap

for k in range(2, 6):
    for l in range(4, 7):
        iso = Isomap(n_neighbors = k, n_components = l)
        X_iso = iso.fit_transform(T)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

        for C in np.arange(0.05,2,.05):
            for gamma in np.arange(.001,.1,.001):
                svc = SVC(C=C,gamma=gamma)
                svc.fit(X_train_norm, y_train) 
                score = svc.score(X_test_norm,y_test)
                if score > best_score:
                    best_score = score
                    best_c = svc.C
                    best_g = svc.gamma
            
print( "The highest score obtained:", best_score)
print( "C value:", best_c )
print( "gamma value:", best_g)
