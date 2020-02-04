import random 

minTemp = 0

# Get an array whose elements are unordered integers
def RandomInitList(start, end, length):
    randomList = []
    for i in range(length):
        randomList.append(random.randint(start, end))
    
    print("The automatically generated unordered array data is:")
    print(randomList)
    
    return randomList

# Choose a sorting method
def SelectionSort(SeMatrix):
    exNum = 0
    inNum = 0

    while exNum < len(SeMatrix):
        minValue = SeMatrix[exNum]
        inNum = exNum

        while inNum < len(SeMatrix):
            if minValue > SeMatrix[inNum]:
                minTemp = minValue
                minValue = SeMatrix[inNum]
                SeMatrix[inNum] = minTemp
            inNum = inNum + 1

        SeMatrix[exNum] = minValue
        exNum = exNum + 1
    print("The result of selecting sort is:")
    print(SeMatrix)

    return SeMatrix

if __name__ == "__main__":
    Matrix = []
    Matrix = RandomInitList(1, 100, 50)
    
    # Select Sort
    SelectionSort(Matrix)
    




