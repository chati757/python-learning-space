import numpy as np
import pandas as pd
import os


#load data to dataframe
def load_iris_dataset(split_train_test=None):
    iris = pd.read_csv('iris.data',header=None)
    x = iris.iloc[:,:4].values
    '''
    #x
    [
        [5.1 3.5 1.4 0.2],
        ...
        [5.9 3.  5.1 1.8]
    ]
    '''
    y = iris.iloc[:,-1].values
    '''
    #y
    [
        [Iris-setosa],
        ...
        [Iris-virginica]
    ]
    '''
    if split_train_test:
        classes = np.unique(y)
        itrain = np.empty((0,),dtype=np.int)
        itest = np.empty((0,),dtype=np.int)
        for i in classes:
            idx = np.where(y==i)[0]
            split = int(len(idx) * split_train_test)
            itrain = np.concatenate((itrain,idx[:split]))
            itest = np.concatenate((itest,idx[split:]))
        return x[itrain],y[itrain],x[itest],y[itest]
    return x,y
    
#basic knn
def knn(x_train,y_train,x_test,k):
    y_test = []

    for x in x_test:
        d = np.sqrt(np.sum((x_train-x)**2,axis=1))
        idx = np.argsort(d)
        (values,counts) = np.unique(y_train[idx[:k]],return_counts=True)
        ind = np.argmax(counts)
        ytest.append(values[ind])

    return ytest

if __name__=='__main__':
    load_iris_dataset(split_train_test=0.5)