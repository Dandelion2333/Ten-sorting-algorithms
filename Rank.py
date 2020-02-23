import random 
import time 
import datetime

QuComparision = 0
QuExchange = 0

HeOneComparision = 0
HeOneExchange = 0

HeTwoComparision = 0
HeTwoExchange = 0

MeComparision = 0
MeExchage = 0

########################################################################
# Get an array whose elements are unordered integers
def RandomInitList(start, end, length):
    randomList = []
    for i in range(length):
        randomList.append(random.randint(start, end))
    
    # print("The automatically generated unordered array data is:")
    # print(randomList)
    
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
    print("timeGap:%dms" % timeGap)

    return SeMatrix

########################################################################
# Quickly sorted method calls
def QuickSortMathod(left, right, QuMatrix):
    global QuComparision
    global QuExchange
    comparision = 0
    exchange = 0
    begin = left
    end = right

    if left > right:
        return

    while left != right:
        QuComparision = QuComparision + 1
        if QuMatrix[right] <= QuMatrix[begin]:
            QuComparision = QuComparision + 1
            if QuMatrix[left] > QuMatrix[begin]:
                QuComparision = QuComparision + 1
                QuExchange = QuExchange + 1

                quickTemp = QuMatrix[left]
                QuMatrix[left] = QuMatrix[right]
                QuMatrix[right] = quickTemp

                right = right - 1
            else:
                left = left + 1
        else:
            right = right - 1

    QuExchange = QuExchange + 1
    
    quickTemp = QuMatrix[begin]
    QuMatrix[begin] = QuMatrix[right]
    QuMatrix[right] = quickTemp

    QuickSortMathod(begin, (left - 1), QuMatrix)
    QuickSortMathod((right + 1), end, QuMatrix)

# Quickly sorted method
def QuickSort(QuMatrix):
    timeStart = time.time()

    global QuComparision
    global QuExchange
    QuickSortMathod(0, (len(QuMatrix) - 1), QuMatrix)
        
    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    #print("The result of quick sort is:")
    #print(QuMatrix)
    # print("Quick comparision number:%d" % QuComparision)
    # print("Quick exchange number:%d" % QuExchange)
    print("Quick timeGap:%dms" % timeGap)

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
    print("timeGap:%dms" % timeGap)

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
    print("timeGap:%dms" % timeGap)

    return ShMatrix

########################################################################
def BubbleSort(BuMatrix):
    timeStart = time.time()
    comparision = 0
    exchange = 0

    stopFlag = True
    exCnt = 0
    while exCnt < len(BuMatrix):
        inCnt = 0
        while (inCnt + 1) < (len(BuMatrix) - exCnt):
            if BuMatrix[inCnt] > BuMatrix[inCnt+1]:
                stopFlag = False
                exchange = exchange + 1
                BuTemp = BuMatrix[inCnt+1]
                BuMatrix[inCnt+1] = BuMatrix[inCnt]
                BuMatrix[inCnt] = BuTemp
            inCnt= inCnt + 1
            comparision = comparision + 1
        if (stopFlag == True) and (exCnt == 0):
            break        
        exCnt = exCnt + 1
    
    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    #print("The result of bubble sort is:")
    print(BuMatrix)
    print("Bubble comparision number:%d" % comparision)
    print("Bubble exchange number:%d" % exchange)
    print("timeGap:%dms" % timeGap)

########################################################################
def HeapSortOne(HeMatrix):
    timeStart = time.time()
    global HeOneComparision
    global HeOneExchange
    constructionCnt = 0

    while constructionCnt < len(HeMatrix):
        # Get the first non-leaf node
        begin = (int((len(HeMatrix)-constructionCnt) / 2) - 1)
        HeMatrix = ConstructionHeap(HeMatrix, begin, constructionCnt)
        # Each time a large top pile is constructed, the number of participating structures is reduced next time
        constructionCnt = constructionCnt + 1
        
        HeMatrix = SwapValue(HeMatrix, 0, (len(HeMatrix) - constructionCnt))
    
    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    #print("The result of heap sort is:")
    #print(HeMatrix)
    print("Heap comparision number:%d" % HeOneComparision)
    print("Heap exchange number:%d" % HeOneExchange)
    print("timeGap:%dms" % timeGap)
    
    return HeMatrix

# Constructing a Big Top Binary Tree
def ConstructionHeap(HeMatrix, begin, constructionCnt):
    global HeOneComparision
    global HeOneExchange
    # Get the starting non-leaf node
    noLeafNodeCnt = begin

    while noLeafNodeCnt >= 0:
        # Determine if there is a left child
        if (noLeafNodeCnt * 2 + 2) < (len(HeMatrix) - constructionCnt):
            if HeMatrix[noLeafNodeCnt*2+1] > HeMatrix[noLeafNodeCnt*2+2]:
                HeMatrix = SwapMax(HeMatrix, noLeafNodeCnt, noLeafNodeCnt*2 + 1)
            else:
                HeMatrix = SwapMax(HeMatrix, noLeafNodeCnt, noLeafNodeCnt*2 + 2)
        else:
            # Compare directly with right child
            HeMatrix = SwapMax(HeMatrix, noLeafNodeCnt, noLeafNodeCnt*2 + 1)
        
        HeOneComparision = HeOneComparision + 1
        HeOneExchange = HeOneExchange + 1

        noLeafNodeCnt = noLeafNodeCnt - 1

    return HeMatrix

def SwapMax(HeMatrix, large, small):
    if HeMatrix[large] < HeMatrix[small]:
        temp = HeMatrix[large]
        HeMatrix[large] = HeMatrix[small]
        HeMatrix[small] = temp
    return HeMatrix

def SwapValue(HeMatrix, left, right):
    temp = HeMatrix[left]
    HeMatrix[left] = HeMatrix[right]
    HeMatrix[right] = temp

    return HeMatrix

########################################################################
def HeapSortTwo(HeMatrix):
    timeStart = time.time()
    global HeTwoComparision
    global HeOneExchange

    sortCompleteCnt = 0

    # Get the first non-leaf node
    nodeNum = len(HeMatrix)-sortCompleteCnt
    noLeafNodeCnt = (int(nodeNum / 2) - 1)

    while noLeafNodeCnt >= 0:    
        HeapSortTwoSwap(HeMatrix, noLeafNodeCnt, nodeNum)
        noLeafNodeCnt = noLeafNodeCnt - 1

    sortCompleteCnt = sortCompleteCnt + 1
    SwapValue(HeMatrix, 0, (len(HeMatrix)-sortCompleteCnt))

    while len(HeMatrix) > sortCompleteCnt:
        nodeNum = len(HeMatrix)-sortCompleteCnt
        HeapSortTwoSwap(HeMatrix, 0, nodeNum)
        
        sortCompleteCnt = sortCompleteCnt + 1
        SwapValue(HeMatrix, 0, (len(HeMatrix)-sortCompleteCnt))
        
    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    #print("The result of heap sort is:")
    print(HeMatrix)
    print("Heap two comparision number:%d" % HeTwoComparision)
    print("Heap two exchange number:%d" % HeTwoExchange)
    print("timeGap:%dms" % timeGap)
    return 

def HeapSortTwoSwap(HeMatrix, nodeValue, nodeNum):
    global HeTwoComparision
    global HeTwoExchange

    leftChild = nodeValue * 2 + 1
    rightChild = nodeValue * 2 + 2

    # Determine if a node has children
    if leftChild < nodeNum:
        # Determine if a node has a right child
        if rightChild < nodeNum:
            # Take the older of the left and right children
            if HeMatrix[leftChild] > HeMatrix[rightChild]:
                HeMatrix = SwapMax(HeMatrix, nodeValue, leftChild)
                HeapSortTwoSwap(HeMatrix, leftChild, nodeNum)
            else:
                HeMatrix = SwapMax(HeMatrix, nodeValue, rightChild)
                HeapSortTwoSwap(HeMatrix, rightChild, nodeNum)
        else:
            # Compare directly with left child
            HeMatrix = SwapMax(HeMatrix, nodeValue, leftChild)
            HeapSortTwoSwap(HeMatrix, leftChild, nodeNum)
        HeTwoComparision = HeTwoComparision + 1
        HeTwoExchange = HeTwoExchange + 1
    else:
        return 

########################################################################
def MergeSort(MeMatrix):
    global MeComparision 
    global MeExchage
    timeStart = time.time()

    MergeSortMethod(MeMatrix, 0, (len(MeMatrix)-1))

    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    #print("The result of merge sort is:")
    #print(MeMatrix)
    print("Merge two comparision number:%d" % MeComparision)
    print("Merge two exchange number:%d" % MeExchage)
    print("timeGap:%dms" % timeGap)
    

def MergeSortMethod(MeMatix, start, end):
    if start < end:
        mid =  int((end+start)/2)
        MergeSortMethod(MeMatix, start, mid)
        MergeSortMethod(MeMatix, (mid+1), end)
        Merge(MeMatix, start, mid, end)

def Merge(MeMatrix, start, mid, end):
    global MeComparision 
    global MeExchage
    CoMeMatrix = MeMatrix.copy()
    midValue = mid
    cnt = start

    while start <= midValue and (mid+1) <= end:
        if CoMeMatrix[start] < CoMeMatrix[mid+1]:
            MeMatrix[cnt] = CoMeMatrix[start]
            start = start + 1
        else:
            MeMatrix[cnt] = CoMeMatrix[mid+1]
            mid = mid + 1
        cnt = cnt + 1
        MeComparision = MeComparision + 1
        MeExchage = MeExchage + 1
    
    while start <= midValue:
        MeMatrix[cnt] = CoMeMatrix[start]
        start = start + 1
        cnt = cnt + 1        
        MeExchage = MeExchage + 1

    while (mid+1) <= end:
        MeMatrix[cnt] = CoMeMatrix[mid+1]
        mid = mid + 1
        MeExchage = MeExchage + 1
        cnt = cnt + 1        
    
    return

########################################################################
def CountSort(CoMatrix, max):
    CoComparision = 0
    CoExchage = 0

    timeStart = time.time()
    list = [0]*(max+1)

    for cnt in range (len(CoMatrix)):
        CoExchage = CoExchage + 1
        list[CoMatrix[cnt]] = list[CoMatrix[cnt]] + 1

    CoMatrix = []

    for cnt in range(len(list)):
        CoComparision = CoComparision + 1
        if list[cnt] != 0:
            for count in range(list[cnt]):
                CoExchage = CoExchage + 1
                CoMatrix.append(cnt)
                count = count + 1
    
    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    # print("The result of count sort is:")
    # print(CoMatrix)
    print("CountSort comparision number:%d" % CoComparision)
    print("CountSort exchange number:%d" % CoExchage)
    print("CountSort timeGap:%dms" % timeGap)

########################################################################
def BucketSort(BucMatrix, min, max):
    timeStart = time.time()

    if min > max:
        return

    interval = int((max - min)/10) + 1
    list = [[],[], [],[], [],[], [],[], [],[]]
    for BuMaCnt in range (len(BucMatrix)):
        listCnt = 0
        while listCnt < 10:
            if BucMatrix[BuMaCnt] > interval*listCnt and BucMatrix[BuMaCnt] <= interval*(listCnt+1):
                list[listCnt].append(BucMatrix[BuMaCnt])
                break
            else:
                listCnt = listCnt + 1
    
    QuList = []
    for listCnt in range(len(list)):
        list[listCnt] = (QuickSort(list[listCnt]))
        for cnt in range (len(list[listCnt])):
            QuList.append(list[listCnt][cnt])
    
    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart

    print("Bucket Sort timeGap:%dms" % timeGap)

    # print(BucMatrix)
    # print(QuList) 



    return 

########################################################################
if __name__ == "__main__":
    Matrix = []
    min = 1
    max = 500000
    number = 300000
    Matrix = RandomInitList(min, max, number)

    SeMatrix = Matrix.copy()
    QuMatrix = Matrix.copy()
    InMatrix = Matrix.copy()
    ShMatrix = Matrix.copy()
    BuMatrix = Matrix.copy()
    HeOneMatrix = Matrix.copy()
    HeTwoMatrix = Matrix.copy()
    MeMatrix = Matrix.copy()
    CoMatrix = Matrix.copy()
    BucMatrix = Matrix.copy()
    
    # Select Sort
    #SelectionSort(SeMatrix)

    # Quick Sort
    QuickSort(QuMatrix)

    # Insert Sort
    #InsertSort(InMatrix)
    
    # Shell Sort
    # ShellSort(ShMatrix)

    # Bubble Sort
    #BubbleSort(BuMatrix)

    # Heap Sort
    #HeapSortOne(HeOneMatrix)
    #HeapSortTwo(HeTwoMatrix)

    # Merge Sort
    #MergeSort(MeMatrix)

    # Count Sort
    CountSort(CoMatrix, max)

    # Bucket Sort
    BucketSort(BucMatrix, min, max)
