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
            idx = np.where(y==i)[0] #get rows index
            #rint('idx:')
            #print(idx)
            split = int(len(idx) * split_train_test)
            #print('split:',split)
            itrain = np.concatenate((itrain,idx[:split]))
            #print('itrain')
            #print(itrain)
            itest = np.concatenate((itest,idx[split:]))
            #print('itest')
            #print(itest)
        return x[itrain],y[itrain],x[itest],y[itest]
    return x,y
    
#basic knn
def knn(x_train,y_train,x_test,k):
    ytest = []

    for x in x_test:
        d = np.sqrt(np.sum((x_train-x)**2,axis=1))
        print('np.sqrt(np.sum((x_train-x)**2,axis=1)):')
        print(d)
        idx = np.argsort(d)
        print('\nidx = np.argsort(d)')
        print(f'idx:{idx}')
        (values,counts) = np.unique(y_train[idx[:k]],return_counts=True)
        print('\n(values,counts) = np.unique(y_train[idx[:k]],return_counts=True)')
        print(f'k:{k}')
        print(f'idx[:k]:{idx[:k]}')
        print(f'y_train[idx[:k]]:{y_train[idx[:k]]}')
        print(f'values:{values}')
        print(f'counts:{counts}')
        ind = np.argmax(counts)
        print('\nind = np.argmax(counts)')
        print(f'ind:{ind}')
        print(f'values[ind]:{values[ind]}')
        ytest.append(values[ind])
        exit()

    return ytest

if __name__=='__main__':
    xtrain , ytrain , xtest , ytest = load_iris_dataset(split_train_test=0.25)
    #print(xtrain) #Ex.[[4.8 3.  1.4 0.1]..]
    #print(ytrain) #Ex.['Iris-setosa',..]
    #print(xtest) #Ex.[[4.8 3.  1.4 0.1]..]
    #print(ytest) ##Ex.['Iris-setosa',..]

    print('prepare data')
    print(xtrain[:2])
    print(ytrain[:2])
    print(xtest[:1])
    print('\nin knn')
    
    x_train_data = [[1,2],[3,4]]
    y_train_data = ['a','b']
    x_testing_data = [[3,3]]
    knn(np.array(x_train_data),np.array(y_train_data),np.array(x_testing_data),1)