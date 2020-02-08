import random 

minTemp = 0
quickTemp = 0

########################################################################
# Get an array whose elements are unordered integers
def RandomInitList(start, end, length):
    randomList = []
    for i in range(length):
        randomList.append(random.randint(start, end))
    
    print("The automatically generated unordered array data is:")
    print(randomList)
    
    return randomList

########################################################################
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

########################################################################
# Quickly sorted method calls
def QuickSortMathod(left, right, QuMatrix):
    begin = left
    end = right

    if left > right:
        return

    while left != right:
        if QuMatrix[right] <= QuMatrix[begin]:
            if QuMatrix[left] > QuMatrix[begin]:
                quickTemp = QuMatrix[left]
                QuMatrix[left] = QuMatrix[right]
                QuMatrix[right] = quickTemp

                right = right - 1
            else:
                left = left + 1
        else:
            right = right - 1
    
    quickTemp = QuMatrix[begin]
    QuMatrix[begin] = QuMatrix[right]
    QuMatrix[right] = quickTemp

    QuickSortMathod(begin, (left - 1), QuMatrix)
    QuickSortMathod((right + 1), end, QuMatrix)

# Quickly sorted method
def QuickSort(QuMatrix):
    QuickSortMathod(0, (len(QuMatrix) - 1), QuMatrix)
    
    print("The result of quick sort is:")
    print(QuMatrix)
    return QuMatrix

########################################################################
def InsertSort(InMatrix):
    rightCnt = 1
    while rightCnt < len(InMatrix):
        if InMatrix[rightCnt] < InMatrix[rightCnt-1]:
            insertValue = InMatrix[rightCnt]
            leftCnt = rightCnt - 1
            while insertValue < InMatrix[leftCnt] and leftCnt > -1:
                InMatrix[leftCnt+1] = InMatrix[leftCnt] 
                leftCnt = leftCnt - 1
            InMatrix[leftCnt+1] = insertValue
        else:
            rightCnt = rightCnt + 1
    
    print("The result of insert sort is:")
    print(InMatrix)
    return InMatrix


########################################################################
if __name__ == "__main__":
    Matrix = []
    Matrix = RandomInitList(1, 200, 100)
    
    # Select Sort
    #SelectionSort(Matrix)

    # Qucik Sort
    #QuickSort(Matrix)

    # Insert Sort
    InsertSort(Matrix)
    




