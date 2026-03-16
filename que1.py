myList = [5,3,6,9,4,2,0]
#search for element 
def searchTarget(target):
    for i in range(len(myList)):
        if target == myList[i]:
            return i
    return -1
result = searchTarget(9)

if(result!=-1):
    print("Element found at ", result)
else:
    print("Element not found")