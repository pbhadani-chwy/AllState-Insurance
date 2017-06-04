# rows = []
# # number of rows in the file
# datapath="sqlfile.txt"
# with open(datapath) as file:
#
#     rows=file.readlines()
#
# #
# # #Dividing the dataset into single rows of string
# my_data=[]  # is the List of List
# for singlerow in rows:
#     columns=singlerow.split(" ") #  I have taken the rows as a string and then splitting them
#     finalcolumnList=[] #storing each element to finalList
#     type(columns)
#     for column in columns:
#         if '\n' in column:
#             column=column.rstrip('\n') # stripping the \n component
#         finalcolumnList.append((column))
#     my_data.append(finalcolumnList)
#
# print(my_data)

import os
import glob

def read_files():
    my_data = []
    list_of_files = glob.glob('*.txt')
    #print(list_of_files)
    open_File = open ("C:\\Users\pbhadani\Python_code\Output_file.txt", 'a')
    deleteContent(open_File)

    for fileName in list_of_files:
        #print(fileName)
        fin = open(fileName , "r")
        my_data = read_words(fin)
        out_file = fetch_attribute(my_data)
        Write_data(out_file,open_File)

def read_words(FileName):
    #open_file = open(FileName, 'r')
    words_list =[]
    contents = FileName.readlines()
    #print(contents)
    for i in range(len(contents)):
        words_list.extend(contents[i].split())
    return words_list
    open_file.close()

#my_data=read_words()
#print(my_data)

def fetch_attribute(my_data):

    string_data = []
    for i in range(len(my_data) - 1):
        data = []
        while (str(my_data[i]) != 'FROM'):
            print(my_data[i])
            list_data = []
            #print(i)
            list_data = list(my_data[i])

            for j in range(len(list_data) - 1):
                #print('check')
                if ( list_data[j] == '.'):
                    data.append(my_data[i])
                    break
                    #print (j)
                    #print('check1')
                else:
                    continue
            #     else:
            #         j = j + 1
            #         #print('check2')
            #         for k in range(j,len(list_data)):
            #             data.append(list_data[k])
            #         #j = 0
            #         #k = 0
            #         p = len(data) - 1
            #         if(data[p]) != ',':
            #             data.append(',')
            #         break
            #             #j = j + 1
            #     #break
            # #print(data)
            # my_result = []
            # my_join = ''.join(map(str,data))
            # my_result.append(my_join)
            #if (len(string_data) == 2):
            #    print("My desired data" + string_data[1])
            i = i + 1
        else:
            #print("My_result",my_result)
            return(data)
            break



#out_file = fetch_attribute(my_data)
#print(out_file)
def Write_data(out_file,open_File):

    #open_File = open ("C:\\Users\pbhadani\Python_code\Output_file.txt", 'a')
    open_File.write("%s\n" % out_file)

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

read_files()
# PRSN_UNIV_ID
# PRSN_PRM_LAST_NM
# PRSN_PRM_1ST_NM
# ACAD_PRM_PGM_CD
# ACAD_PRM_PLAN_1_DESC
# STU_GRP_CD
# STU_GRP_DESC












