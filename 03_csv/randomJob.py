#code by team AntKirby for Mykolyk Softdev Pd2, written by Tyler Huang and Hannah Fried

import random
diction = {}
def convertToDict():
    ary = []
    file = open('occupations.csv', 'r')
    file.readline()
    for line in file:
        if '"' in line:
            #print(line.split('"')[1:])
            ary.append(line.split('"')[1:])
        #print(line.split(',')[0])
        else:
            ary.append(line.split(','))
    ary = ary[:-1]
    for arr in ary:
        if ',' in arr[1]:
            arr[1] = arr[1][1:]
        #print(arr[1])
        arr[1] = arr[1].replace('\n', '')
        #print(arr)
        diction.update({arr[0]:float(arr[1])})
    #print(diction)

def randomJob():
    weightedList = []
    for job in diction:
        weight = int(float(diction[job]) * 10)
        #print(weight)
        while weight > 0:
            weightedList.append(job)
            #print(weightedList)
            weight = weight - 1
    #print(weightedList)
    print(weightedList[random.randint(0, len(weightedList) - 1)])

convertToDict()
randomJob()

