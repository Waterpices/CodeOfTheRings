from loopDetection import count_biggest_substring_replication
from loopDetection import longest_substring_replication_chain
from colorama import Fore, Back, Style
from functools import wraps
from time import time

testAll = True
testSetNum = 1
'''
Format:
List of test set which are composed of
a tuple composed of the name of the function tested and the related tests which consist in
a list of tuple structured as followed
(input_given, wanted_output)
'''
testSets = [
    (count_biggest_substring_replication,[
        ("AABBAABB",(2,0,"AABB")),
        ("azeAABBAABB",(2,3,"AABB")),
        ("AABBAABBAABBAABB",(2,0,"AABBAABB")),
        ("trysisAABBAABBAABBAABB",(2,6,"AABBAABB")),
        ("trysAABBAABBAABBqspdry",(3,4,"AABB"))
    ]),
    (count_biggest_substring_replication,[
        ("E2E2aFe1aFe1",(2,4,"aFe1")),
        ("E2E2aFe1aFe1qmùodsurjf",(2,4,"aFe1")),
        ("ds5qùb6ofilb6ofils4dlf5jio4sq",(2,5,"b6ofil")),
        ("ertyDERFDERFDERFpodsu",(3,4,"DERF")),
        ("aaabbgghhbbgghh__bbgghhbbgghh__",(2,3,"bbgghhbbgghh__"))
    ]),
    (longest_substring_replication_chain,[
        ("AABBAABB",(2,0,"AABB")),
        ("azeAABBAABB",(2,3,"AABB")),
        ("AABBAABBAABBAABB",(4,0,"AABB")),
        ("trysisAABBAABBAABBAABB",(4,6,"AABB")),
        ("trysAABBAABBAABBqspdry",(3,4,"AABB"))
    ]),
    (longest_substring_replication_chain,[
        ("AABBAABBAABBOUAABBOU",(3,0,"AABB")),
        ("AABBAABBAABBOUBAABBOU",(2,7,"BAABBOU")),
        ("AAAAAAAAAAAAB",(12,0,"A")),
        ("BBBAAAAAAAAAAAABAAAAAAAAAAAAB",(2,2,"BAAAAAAAAAAAA")),
        ("ABCDEFGHFIFOFIFOFIFO UFEOFUFIFO",(3,8,"FIFO")),
        ("before_test123456789123456789123456789123456789123456789123456789___azertyuiopazertyuiopazertyuiopazertyuiop",(6,11,"123456789")),
    ])
]

def timer(func):
        @wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time()
            res = func(*args, **kwargs)
            end_time = time()
            total_time = end_time - start_time
            print(f" in {total_time*1000:.1f} ms \n")
            return res
        return wrapper_timer

def getTestSet(num=0):
    return testSets[num]

@timer
def launchTests(funct,tests):
    validated = 0
    error = 0
    indexError = []
    resultError = []
    for i in range(len(tests)):
        res = funct(tests[i][0])
        if(res == tests[i][1]):
            validated += 1
        else:
            error += 1
            indexError.append(i)
            resultError.append(res)

    print((Fore.GREEN if error == 0 else Fore.RED) + str(validated) + "/" + str(validated+error) +" SUCCESS",end="")
    if(error != 0):
        for i in range(len(indexError)):
            print("\nTest "+ str(indexError[i]) +": "+ str(tests[indexError[i]]) + " FAILED " + "\nReturned: "+ str(resultError[i]),end="")
    print(Style.RESET_ALL, end="")


if __name__ == '__main__':
    if(testAll):
        for i in range(len(testSets)):
            testSet = getTestSet(i)
            print("[Test set " + str(i)+"] " + str(testSet[0].__name__), end='\n')
            launchTests(testSet[0],testSet[1])
    else:
        testSet = getTestSet(testSetNum)
        print("[Test set " + str(testSetNum)+"]" + str(testSet[0].__name__), end='\n')
        launchTests(testSet[0],testSet[1])