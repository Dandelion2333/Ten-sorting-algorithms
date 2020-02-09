import random 
import time 
import datetime

Qucomparision = 0
Quexchange = 0

########################################################################
# Get an array whose elements are unordered integers
def RandomInitList(start, end, length):
    randomList = []
    for i in range(length):
        randomList.append(random.randint(start, end))
    
    #print("The automatically generated unordered array data is:")
    print(randomList)
    
    return randomList

########################################################################
# Choose a sorting method
def SelectionSort(SeMatrix):
    timeStart = time.time()
    comparision = 0
    exchange = 0
    exNum = 0
    inNum = 0

    while exNum < len(SeMatrix):
        minValue = SeMatrix[exNum]
        inNum = exNum

        while inNum < len(SeMatrix):
            if minValue > SeMatrix[inNum]:
                comparision = comparision + 1
                exchange = exchange + 1
                minTemp = minValue
                minValue = SeMatrix[inNum]
                SeMatrix[inNum] = minTemp
            inNum = inNum + 1

    
        exchange = exchange + 1
        SeMatrix[exNum] = minValue
        exNum = exNum + 1

    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart

    #print("The result of selecting sort is:")
    #print(SeMatrix)
    print("Select comparision number:%d" % comparision)
    print("Select exchange number:%d" % exchange)
    print("timeGap:%d" % timeGap)

    return SeMatrix

########################################################################
# Quickly sorted method calls
def QuickSortMathod(left, right, QuMatrix):
    global Qucomparision
    global Quexchange
    comparision = 0
    exchange = 0
    begin = left
    end = right

    if left > right:
        return

    while left != right:
        Qucomparision = Qucomparision + 1
        if QuMatrix[right] <= QuMatrix[begin]:
            Qucomparision = Qucomparision + 1
            if QuMatrix[left] > QuMatrix[begin]:
                Qucomparision = Qucomparision + 1
                Quexchange = Quexchange + 1
                quickTemp = QuMatrix[left]
                QuMatrix[left] = QuMatrix[right]
                QuMatrix[right] = quickTemp

                right = right - 1
            else:
                left = left + 1
        else:
            right = right - 1
    
    Quexchange = Quexchange + 1
    quickTemp = QuMatrix[begin]
    QuMatrix[begin] = QuMatrix[right]
    QuMatrix[right] = quickTemp

    QuickSortMathod(begin, (left - 1), QuMatrix)
    QuickSortMathod((right + 1), end, QuMatrix)

# Quickly sorted method
def QuickSort(QuMatrix):
    timeStart = time.time()

    global Qucomparision
    global Quexchange
    QuickSortMathod(0, (len(QuMatrix) - 1), QuMatrix)
        
    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    #print("The result of quick sort is:")
    #print(QuMatrix)
    print("Quick comparision number:%d" % Qucomparision)
    print("Quick exchange number:%d" % Quexchange)
    print("timeGap:%d" % timeGap)

    return QuMatrix

########################################################################
def InsertSort(InMatrix):
    timeStart = time.time()
    comparision = 0
    exchange = 0
    rightCnt = 1
    while rightCnt < len(InMatrix):
        comparision = comparision + 1
        if InMatrix[rightCnt] < InMatrix[rightCnt-1]:
            comparision = comparision + 1
            insertValue = InMatrix[rightCnt]
            leftCnt = rightCnt - 1
            while leftCnt > -1 and insertValue < InMatrix[leftCnt]:
                comparision = comparision + 1
                exchange = exchange + 1
                InMatrix[leftCnt+1] = InMatrix[leftCnt] 
                leftCnt = leftCnt - 1
            exchange = exchange + 1
            InMatrix[leftCnt+1] = insertValue

        rightCnt = rightCnt + 1
    
    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    #print("The result of insert sort is:")
    #print(InMatrix)
    print("Insert comparision number:%d" % comparision)
    print("Insert exchange number:%d" % exchange)
    print("timeGap:%d" % timeGap)

    return InMatrix

########################################################################
def ShellSort(ShMatrix):
    timeStart = time.time()

    comparision = 0
    exchange = 0
    gap = int((len(ShMatrix) / 2))
    
    while gap > 0:
        begin = 0
        # Set each data loop
        while begin < gap:
            rightCnt = begin + gap

            # Sorting of each group of data after separation by gaps
            while rightCnt < len(ShMatrix):
                if ShMatrix[rightCnt] < ShMatrix[rightCnt - gap]:
                    comparision = comparision + 1
                    leftCnt = rightCnt - gap
                    insertValue = ShMatrix[rightCnt]
                    while leftCnt > (begin - gap) and ShMatrix[leftCnt] > insertValue:
                        comparision = comparision + 1
                        ShMatrix[leftCnt + gap] = ShMatrix[leftCnt]
                        exchange = exchange + 1
                        leftCnt = leftCnt - gap
                    ShMatrix[leftCnt + gap] = insertValue

                rightCnt = rightCnt + gap
            begin = begin + 1
        gap = int((gap / 2))

    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    #print("The result of shell sort is:")
    #print(ShMatrix)
    print("Shell comparision number:%d" % comparision)
    print("Shell exchange number:%d" % exchange)
    print("timeGap:%d" % timeGap)

    return ShMatrix

########################################################################
def BubbleSort(BuMatrix):
    timeStart = time.time()
    
    comparision = 0
    exchange = 0
    exCnt = 0
    while exCnt < len(BuMatrix):
        inCnt = 0
        while (inCnt + 1) < (len(BuMatrix) - exCnt):
            if BuMatrix[inCnt] > BuMatrix[inCnt+1]:
                exchange = exchange + 1
                BuTemp = BuMatrix[inCnt+1]
                BuMatrix[inCnt+1] = BuMatrix[inCnt]
                BuMatrix[inCnt] = BuTemp
            inCnt= inCnt + 1
            comparision = comparision + 1

        exCnt = exCnt + 1
    
    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    print("The result of bubble sort is:")
    print(BuMatrix)
    print("Shell comparision number:%d" % comparision)
    print("Shell exchange number:%d" % exchange)
    print("timeGap:%d" % timeGap)

########################################################################
if __name__ == "__main__":
    Matrix = []
    Matrix = RandomInitList(1, 200, 3)

    SeMatrix = Matrix.copy()
    QuMatrix = Matrix.copy()
    InMatrix = Matrix.copy()
    ShMatrix = Matrix.copy()
    BuMatrix = Matrix.copy()
    
    # Select Sort
    #SelectionSort(SeMatrix)

    # Quick Sort
    #QuickSort(QuMatrix)

    # Insert Sort
    #InsertSort(InMatrix)
    
    # Shell Sort
    #ShellSort(ShMatrix)

    # Bubble Sort
    BubbleSort(BuMatrix)

