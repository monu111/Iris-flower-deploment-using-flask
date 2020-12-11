import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('iris.data')


# dependent and independent variables
X = df.iloc[:,0:4].values
y = df.iloc[:,4].values

# applying Labelenocding to dependent variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)


# Splitting the data into train and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


#Applying SVC
from sklearn.svm import SVC
svc = SVC(kernel = 'linear').fit(X_train,y_train)


# saving the model in disk
pickle.dump(svc, open('iris.pkl', 'wb'))




