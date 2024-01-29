import math

# Get a string and return the largest substring that's countained multiple time in a row
# @Return count, start_index, substring
def count_biggest_substring_replication(string):
    count = 0
    loopFound = False
    substring = ""
    
    '''
    Length of the substring in decreasing order to find the biggest first
    '''
    for length in range(math.floor(len(string)/2),0,-1):
        '''
        Starting index of the substring. Moving window trying each substring
        End when the substring can't be contained at least twice
        '''
        for offset in range(len(string)-length*2+1): 
            substring = string[offset:length+offset]
            #print('searching for: ' + substring)
            count = 0
            '''
            Loop a maximal number of time a substring can be countained +1
            +1 allows to make another run and return the result
            If the substring is found, the loop continue
            '''
            for j in range(1,math.ceil((len(string)-offset)/length)+1): 
                #print("offset="+str(offset)+",j="+str(j))
                #print(str(length+offset+j*length) + "<" + str(len(string)+1) + " ?")
                #print(substring + " == " + string[offset+j*length:length+offset+j*length] +" ?")
                '''
                If the substring isn't found, we stop the loop
                The Substring is returned if a replication was found otherwise the offset is changed
                '''
                if(length+offset+j*length < len(string)+1 and string[offset+j*length:length+offset+j*length] == substring): #TODO
                    count += 1
                    loopFound = True
                else:
                    if(loopFound):
                        return count+1, offset, substring # The count +1 take into account the original substring
                    else:
                        break
    return 0, 0, ""; #no loop found in the string

# Identifies and returns the repeating substring forming the longest consecutive chain of characters within the given input string
# @Return count, start_index, substring
def longest_substring_replication_chain(string):
    count = 0
    loopFound = False
    substring = ""
    maxChainLength = 0
    res = (0,0,"") # Default return if no loops are found
    iteration = 0
    
    '''
    Length of the substring in increasing order to find the smallest first
    '''
    for length in range(1,math.floor(len(string)/2)+1,1):
        '''
        Starting index of the substring. Moving window trying each substring
        End when the substring can't be contained at least twice
        '''
        for offset in range(len(string)-length*2+1):
            substring = string[offset:length+offset]
            #print('searching for: ' + substring)
            count = 0
            loopFound = False
            '''
            Loop a maximal number of time a substring can be countained +1
            +1 allows to make another run and return the result
            If the substring is found, the loop continue
            '''
            for j in range(1,math.ceil((len(string)-offset)/length)+1): 
                '''
                If the substring isn't found, we stop the loop
                The Substring is returned if a replication was found otherwise the offset is changed
                '''
                iteration += 1
                if(length+offset+j*length < len(string)+1 and string[offset+j*length:length+offset+j*length] == substring): #TODO
                    #print(string[offset+j*length:length+offset+j*length] + "==" + substring)
                    count += 1
                    loopFound = True
                else:
                    if(loopFound):
                        if((count+1)*len(substring)>maxChainLength): # If the chain is longer than the longest found for now
                            res = (count+1, offset, substring) # The count +1 take into account the original substring
                            maxChainLength = (count+1)*len(substring) # save the chain
                            break
                    else:
                        break
    #print("Iteration: " + str(iteration) + "\nmaxChainLength: " + str(maxChainLength))
    return res

if __name__ == '__main__':
    var = "ABCDEFGHFIFOFIFOFIFO UFEOFUFIFO"
    #print("length=" + str(len(var)))
    #count, start_index, substring = count_biggest_substring_replication(var)
    #print(count, start_index, substring)
    count, start_index, substring = longest_substring_replication_chain(var)
    print(count, start_index, substring)