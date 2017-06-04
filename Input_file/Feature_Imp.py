import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesRegressor
import collections

f = open('F:\kaggle\Final Project\\Book.txt')
# f.readline()  # skip the header
dataset = np.loadtxt(fname=f, delimiter=',')
# dataset = datasets.load_iris()
# fit an Extra Trees model to the data
# print(dataset)
mapElement = {}
X = dataset[:, 1:31]
Y = dataset[:, 0]
num_trees = 10
max_feature = 7
model = ExtraTreesRegressor(n_estimators=num_trees, max_features=max_feature)
model.fit(X, Y)
z = model.feature_importances_
print("first",z.item(0))

for i in range(len(z)):
    mapElement[z.item(i)] = (i+1)
#od = collections.OrderedDict(sorted(mapElement.items()))
p = sorted(mapElement)
print(p)
result = []
for i in range(len(p)):
    result.append(mapElement.get(p[(len(p) - 1)- i ]))

print(result)
#print(type(od))
print(mapElement)
#print(od)
# model.fit(dataset.data, dataset.target)
# display the relative importance of each attribute
print(model.feature_importances_)
