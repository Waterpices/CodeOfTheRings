NUMBER_OF_RUNE_STATE = 27
numberOfIterationWithOffSet = []
for i in range(NUMBER_OF_RUNE_STATE):
    numberOfIterationWithOffSet.append([])
weight = []
for i in range(NUMBER_OF_RUNE_STATE):
    weight.append([])
hasEnded = False;

def mapNoOffSet():
    numberOfiIeration= {}
    currentletter = -1 #Z i.e. 26
    for i in range(1,28):
        for j in range(1,500):
            currentletter -= i
            if(currentletter < 0):
                currentletter += 27
            if(currentletter == 0):
                numberOfiIeration[str(i)] = str(j);
                break
        currentletter = -1;
            
    print(numberOfiIeration["1"])
    for key in numberOfiIeration:
        print("Number of iteration for " + key + " '-': " + numberOfiIeration[key])

def matricewithOffSet():
    for offSet in range(NUMBER_OF_RUNE_STATE): #offSet before the loop
        currentletter = offSet
        for i in range(NUMBER_OF_RUNE_STATE): # i = number of + in the loop
            for j in range(1,200): # number of iteration before the loop stops
                currentletter -= i
                if(currentletter < 0):
                    currentletter += NUMBER_OF_RUNE_STATE
                if(currentletter == 0):
                    numberOfIterationWithOffSet[offSet].append(j)
                    hasEnded = True
                    break
            if not(hasEnded):
                numberOfIterationWithOffSet[offSet].append(0)
            hasEnded = False
            currentletter = offSet;

def print2DArray( array ):
    string = ""
    for i in range(len(array)):
        string+="["
        for j in range(len(array[i])):
            string+= str(array[i][j]) + ","
        string = string[0:-1] + "]"
        print(string)
        string = ""

def weightMatrice(array):
    size = len(array)
    for i in range(size):
        for j in range(size):
            array[i].append(min(i+j,abs(i-size)+j,i+abs(j-size),abs(i-size)+abs(j-size)))
    return array

def findBestStringForNIteration(array,weight,n):
    size = len(array)
    min = 26 #max possible value
    offsetSequence = ""
    loopSequence = ""
    for i in range(size):
        for j in range(size):
            if array[i][j] == n and weight[i][j] < min:
                min = weight[i][j]
                if i<size/2 :
                    offsetSequence = "+"*i
                else:
                    offsetSequence = "-"*(abs(i-size))
                if j<size/2 :
                    loopSequence = "-"*j
                else:
                    loopSequence = "+"*(abs(j-size))
    return [min,offsetSequence,loopSequence];

#mapNoOffSet()
matricewithOffSet()
print("---------iterations---------")
#print2DArray(numberOfIterationWithOffSet)
weight = weightMatrice(weight)
print("-----------weight-----------")
#print2DArray(weight)
print("----iterations sequences----")
for i in range(1,28):
    print(str(i) + ": " + str(findBestStringForNIteration(numberOfIterationWithOffSet,weight,i)))