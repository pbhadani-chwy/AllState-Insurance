
# Feature Importance
import Regression_Forest as RF
from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesRegressor
from sklearn import cross_validation

import sys
import numpy as np

global depth


def featureImp(dataset1):
    import numpy as np
    from sklearn import datasets
    from sklearn import metrics
    from sklearn.ensemble import ExtraTreesRegressor
    import collections

    #f = open('F:\kaggle\Final Project\\Book.txt')
    # f.readline()  # skip the header
    #dataset = np.loadtxt(fname=f, delimiter=',')
    # dataset = datasets.load_iris()
    # fit an Extra Trees model to the data
    # print(dataset)
    mapElement = {}
    X = dataset1[:, 1:406]
    Y = dataset1[:, 0]
    num_trees = 10
    max_feature = 7
    model = ExtraTreesRegressor(n_estimators=num_trees, max_features=max_feature)
    model.fit(X, Y)
    z = model.feature_importances_
    #print("first", z.item(0))

    for i in range(len(z)):
        mapElement[z.item(i)] = (i + 1)
    # od = collections.OrderedDict(sorted(mapElement.items()))
    p = sorted(mapElement)
    #print(p)
    result = []
    for i in range(len(p)):
        result.append(mapElement.get(p[(len(p) - 1) - i]))

    return (result)
    #print(result)
    # print(type(od))
    #print(mapElement)
    # print(od)
    # model.fit(dataset.data, dataset.target)
    # display the relative importance of each attribute
    #print(model.feature_importances_)


def Bagging(depth,numtree,datapath1,datapath2):

    from numpy import random
    rows = []
    # number of rows in the file
    #datapath="..\PA_2\mushrooms\\agaricuslepiotatrain1_updated1.txt"
    with open(datapath1) as file:

        rows=file.readlines()

    #
    # #Dividing the dataset into single rows of string
    my_data=[]  # is the List of List
    for singlerow in rows:
        columns=singlerow.split(",") #  I have taken the rows as a string and then splitting them
        finalcolumnList=[] #storing each element to finalList
        type(columns)
        for column in columns:
            if '\n' in column:
                column=column.rstrip('\n') # stripping the \n component
            finalcolumnList.append(column)
        my_data.append(finalcolumnList)

    dataset = np.array(my_data)
    bag = []
    ForestTree = []
    #imp_feature = []
    num_fold = 10
    num_instance = len(my_data)
    seed = 0
    bagsize = int(len(my_data)/numtree)
    print(bagsize)
    #kfold =  cross_validation.KFold(n= num_instance, n_folds= num_fold, random_state= seed)
    for k in range(numtree):

        bag.append(dataset[np.random.choice(dataset.shape[0], bagsize)])
        #print("Bag Details\n",bag[i])
        imp_feature = featureImp(bag[k])
        Final_feature= imp_feature[0:200]
        #print('important feature',Final_feature)
        RF.height = 0
        ForestTree.append(RF.build_tree(bag[k], int(depth), Final_feature))
    RF.drawtree(ForestTree[0], jpeg='FinalTreeView1.jpg')
    #RF.height = 0
    RF.drawtree(ForestTree[1], jpeg='FinalTreeView2.jpg')
    # #RF.height = 0
    RF.drawtree(ForestTree[2], jpeg='FinalTreeView3.jpg')
    # #RF.height = 0
    RF.drawtree(ForestTree[3], jpeg='FinalTreeView4.jpg')



    #****************************** Testing the Tree Phase **********************************************#
    with open(datapath2) as file:

        rows=file.readlines()

    #
    # #Dividing the dataset into single rows of string
    test_result = []
    test_data=[]  # is the List of List
    for singlerow in rows:
        columns=singlerow.split(",") #  I have taken the rows as a string and then splitting them
        finalcolumnList=[] #storing each element to finalList
        type(columns)
        for column in columns:
            if '\n' in column:
                column=column.rstrip('\n') # stripping the \n component
            finalcolumnList.append(column)
        test_data.append(finalcolumnList)

    for p in range(numtree):
        test_result.append(RF.Compare_results(test_data,ForestTree[p]))

    #print(test_result)
    sum = 0
    for i in range(len(test_result)):
        if (str(test_result[i][0]) != 'nan'):
            sum = sum + (test_result[i][0])
    AvgR2 = sum/len(test_result)
    print("Average R2", AvgR2 )
#datapath1 = 'C:\\Users\\pbhadani\\Python_code\\Input_file\\TrainDatset-Final_V2.1.txt'
#datapath2 = 'C:\\Users\\pbhadani\\Python_code\\Input_file\\TrainDatset-Final_V2.1.txt'
datapath1 = 'C:\\Users\\pbhadani\\Python_code\\Input_file\\Book.txt'
datapath2 = 'C:\\Users\\pbhadani\\Python_code\\Input_file\\Book.txt'

#Bagging(3,5,datapath1,datapath2)

if __name__ == "__main__":
    # The arguments to your file will be of the following form:
    # <ensemble_type> <tree_depth> <num_bags/trees> <data_set_path>
    # Ex. bag 3 10 mushrooms
    # Ex. boost 1 10 mushrooms

    # Get the ensemble type
    tdepth = sys.argv[1];
    # Get the depth of the trees
    tnumtree = int(sys.argv[2]);
    # Get the number of bags or trees
    train_dataPath = sys.argv[3];
    # Get the location of the data set
    test_dataPath = sys.argv[4];
    # Get the location of the data set
    #testdatapath = sys.argv[5];

Bagging(tdepth,tnumtree,train_dataPath,test_dataPath)

