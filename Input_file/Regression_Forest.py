
import numpy as np
from scipy.stats.stats import pearsonr

# with open('F:\kaggle\Final Project\\Book.txt', 'r') as file:
#     rows = file.readlines()
#
# print(rows)
#
#
# #
# # #Dividing the dataset into single rows of string
# my_data = []  # is the List of List
# #count1 = 0
# for singlerow in rows:
#     columns = singlerow.split(",")  # I have taken the rows as a string and then splitting them
#     finalcolumnList = []  # storing each element to finalList
#     type(columns)
#     for column in columns:
#         if '\n' in column:
#             column = column.rstrip('\n')  # stripping the \n component
#         finalcolumnList.append(column)
#     my_data.append(finalcolumnList)
# print ("my_data",my_data)
# dataset = np.array(my_data)
# bag5 = []
# for i in range(1):
#     bag5.append(dataset[np.random.choice(dataset.shape[0], 50)])
#
# my_final_data = bag5[0]
# print(my_final_data)
#     # print(bag[i])
height = 0
i = 1

####### ************** Calculating Variance ***********************######
#### online algorithm is used to calculate the Variance of the given Data *******######

def onlinevariance(data):
    if len(data) == 0 or len(data) == 1:
        return 0
    n = 0
    mean = 0.0
    M2 = 0.0

    for x in data:
        n += 1
        delta = float(x[0]) - mean
        mean += delta / n
        M2 += delta * (float(x[0]) - mean)

    if n < 2:
        return float('nan')
    else:
        return M2 / (n - 1)


#*********************************Calculate Average value of a set ********************************#

def Cal_avg(rows):
    avg = 0
    sum = 0.0
    for row in rows:
        sum = sum + float(row[0])
    avg = sum / len(rows)
    return avg
#*********************************************************** **************************************#
#                       Code for partioning the set                                                #
#**************************************************************************************************#


def partition_set(rows, column, value):
    #print(rows)
    #print("value in partition", type(value))
    # Make a function that tells us if a row is in the first group (true) or the second group (false)
    split_function = None
    # try:
    z = float(value)
    #print("value in partition", type(z))
    # split_function = lambda row: int(row[column]) >= int(value)
    if isinstance(z, int) or isinstance(z, float):  # check if the value is a number i.e int or float
        #print("Check if its entering here")
        split_function = lambda row: row[column] >= value
    # except ValueError:
    else:
        split_function = lambda row: row[column] == value

        # Divide the rows into two sets and return them
    set1 = [row for row in rows if split_function(row)]
    set2 = [row for row in rows if not split_function(row)]
    #if len(set1) == 0 or len(set2) == 0:
        #print ("Null set")
        #print(set1)
        #print("now the set 2 will start")
        # print(set2)
    return (set1, set2)

#*****************************************************************************************************#
#                                   Defining Class Node                                               #
#*****************************************************************************************************#


class NodeAnalysis:
    def __init__(self, col=-1, value=None, lb=None, rb=None, results=None, ent=None):
        self.col = col
        self.value = value
        self.lb = lb
        self.rb = rb
        self.results = results
        self.ent = ent
        # print(self.results)


#*****************************************************************************************************#
#                                   Code for building the tree                                        #
#*****************************************************************************************************#


def build_tree(records, depth, Feature):
    global height
    global i
    #print(Feature)
    if len(records) == 0: return NodeAnalysis()
    column_count = len(records[0])
    #print('column_count', column_count)
    min_SOS = 9999999999.99
    #parent_gain = Calculate_entropy(records)
    #print('parent_gain', parent_gain)
    best_feature = None
    best_sets = None
    #print('test_entry')
    # parent_gain = Calculate_entropy(records)
    # print(records[0])
    # print(column_count)
    count1 = 0
    #count = 0
    for col in Feature:
        # print(range(1,column_count)
        # Generate the list of all possible different values in the considered column
        global column_values  # Added for debugging
        column_values = {}
        count = 0
        # print(column_values)
        #for row in records:
        # if count == 0:
        #     continue
        # else:
        #print(row)
        # print(row[col])
        for row in records:
            column_values[row[col]] = 1

        #print('DiscPrint', column_values.keys())
        # print(column_values)
        #print('Disc Print',column_values[row[col]])
        #count = count + 1            #This count variable is just for the testing purose#
        # Now try dividing the rows up for each value in this column
        for value in column_values.keys():  # the 'values' here are the keys of the dictionnary
            #if col == 1:
               #print('Final Column value',value)
            #print(col)
            #count1 = count1 + 1
            #print('Every Col and value',col,value)
            (set1, set2) = partition_set(records, col,value)  # define set1 and set2 as the 2 children set of a division
            #print ('length of set1', len(set1))
            #print ('length of set2', len(set2))


            # ******************* Caculating the Information gain for the two set generated ********************#
            #if (i <= 1):
                #print(set1, set2)
                #i += 1
            #p = float(len(set1) / len(records))
            # q = float(1 - p)
            #gain = parent_gain - p * Calculate_entropy(set1) - (1 - p) * Calculate_entropy(set2)
            TotSOS = onlinevariance(set1) + onlinevariance(set2)
            #print('tot SOS', TotSOS)

            # print('parent_gain', parent_gain)
            #print('gain : ', gain)
            if TotSOS <= min_SOS and len(set1) > 0 and len(set2) > 0 and TotSOS != 'nan':
                min_SOS = TotSOS
                #print('min_SOS', min_SOS)
                best_feature = (col, value)
                #print(best_feature[0],best_feature[1])
                best_sets = [set1, set2]
                #print(best_feature)
   # print ('The best Set',best_sets)
        # ************Based on the optimum information gain calculated partioning the tree ********************
    #print('test')
    #print("len(set1) Len(set2)", len(set1), len(set2))
    #print("height", height)
    if (min_SOS > 0 and height < depth) and (set1) != 0 and len(set2) != 0 : #*and height < depth*#)
        #print("check this loop")
        #print(len(set1))
        #print('best_sets[1]', best_sets[1])
        #print('max_gain: ', max_gain)
        height += 1
        #print("height", height)
        #print('height: ', height)
        if (len(set1) == 0 and len(set2)!=0):
            RightBranch = build_tree(best_sets[1], depth , Feature)
            return NodeAnalysis(col=best_feature[0], value=best_feature[1],
                             rb=RightBranch)
        #if len(best_sets[0]) == 0:
            #print(best_sets[0])
        if (len(set2) == 0 and len(set1)!=0):
            LeftBranch = build_tree(best_sets[0], depth , Feature)
            return NodeAnalysis(col=best_feature[0], value=best_feature[1],
                            lb=LeftBranch)
        if (len(set1)!= 0 and len(set2)!=0):

            LeftBranch = build_tree(best_sets[0], depth , Feature)
            RightBranch = build_tree(best_sets[1], depth, Feature)
            return NodeAnalysis(col=best_feature[0], value=best_feature[1],
                            lb=LeftBranch, rb = RightBranch)

    else:
        #height=0
        #print(height)
        return NodeAnalysis(results = Cal_avg(records))#ent=Calculate_entropy(records))

#******************************************************************************************************#
#                           Print the forest                                                           #
#******************************************************************************************************#
def getwidth(tree):
    if tree.lb == None and tree.rb == None: return 1
    return getwidth(tree.lb) + getwidth(tree.rb)
def getdepth(tree):
    if tree.lb == None and tree.rb == None: return 0
    return max(getdepth(tree.lb), getdepth(tree.rb)) + 1

from PIL import Image, ImageDraw


def drawtree(tree, jpeg='tree.jpg'):
    w = getwidth(tree) * 200
    h = getdepth(tree) * 200 + 120

    img = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    drawnode(draw, tree, w / 2, 20)
    img.save(jpeg, 'JPEG')

def drawnode(draw, tree, x, y):
    if tree.results == None:
        # Get the width of each branch
        w1 = getwidth(tree.rb) * 100
        w2 = getwidth(tree.lb) * 100

        # Determine the total space required by this node
        left = x - (w1 + w2) / 2
        right = x + (w1 + w2) / 2

        # Draw the condition string
        draw.text((x - 20, y - 10), 'feature:' + str(tree.col) + ',' + 'value:' + str(tree.value), (0, 0, 0))

        # Draw links to the branches
        draw.line((x, y, left + w1 / 2, y + 100), fill=(255, 0, 0))
        draw.line((x, y, right - w2 / 2, y + 100), fill=(255, 0, 0))

# Draw the branch nodes
        drawnode(draw, tree.lb, left + w1 / 2, y + 100)
        drawnode(draw, tree.rb, right - w2 / 2, y + 100)
    else:
        txt = ' \n'.join([str(tree.results)])  # + str(tree.ent)""]#)
        draw.text((x - 20, y), txt, (0, 0, 0))

# depth = input("enter the depth of the tree")
# Desctree = build_tree(my_final_data,int(depth))
# drawtree(Desctree, jpeg='TreeView.jpg')
def FlowTestData(observation, tree):
    if tree.results != None:
        return tree.results
    else:
        #print(observation)
        #print (observation[tree.col])
        v = float(observation[tree.col])

        #print("Type of V",type(v))
        #print('check the type of V' , v)
        branch = None
        if isinstance(v, int) or isinstance(v, float):
            #print('check if the control goes here')
            if v >= float(tree.value):
                branch = tree.lb
            else:
                branch = tree.rb
        else:
            if v == float(tree.value):
                branch = tree.lb
            else:
                branch = tree.rb
        return FlowTestData(observation, branch)


def PrintClass(test_data,Desctree):
    no1 = 0
    no0 = 0
    predict_out = []
    for testrec in test_data:
        Expresults = FlowTestData(testrec, Desctree)
        #if (Expresults[0] > Expresults[1]):
        predict_out.append(Expresults)
    #print("Predict_output",predict_out)
    #         no1 += 1
    #         #print("1")
    #
    #     else:
    #         predict_out.append(0)
    #         #print("0")
    #         no0 += 1
    # #print(predict_out)
    # #print(no1, no0)
    # #print(len(predict_out))
    return predict_out

def Compare_results(test_data,Desctree):
    predict = []
    predict = PrintClass(test_data,Desctree)
    test = []
    # i = 0
    # TruePositive = 0
    # TrueNegative = 0
    # FalsePositive = 0
    # FalseNegative = 0
    #print("check")
    for testrec in test_data:
        test.append(float(testrec[0]))
    #print("test",test)
    R2 = pearsonr(predict,test)


    #     if testrec[0] == predict[i]:
    #         if predict[i] == 1:
    #             TruePositive += 1
    #         else:
    #             TrueNegative += 1
    #     else:
    #         if predict[i] == 1:
    #             FalsePositive += 1
    #         else:
    #             FalseNegative += 1
    #             # Falsecount +=1
    #     i = i + 1
    # Accuracy = float((TruePositive + TrueNegative)/ (TruePositive+FalsePositive + TrueNegative + FalseNegative))
    return(R2)


