def bubbleSort(itemList):
    moreSwaps = True
    counter = 0
    while moreSwaps:
        counter = counter + 1
        print("Iteration number",counter)
        moreSwaps = False
        for element in range(len(itemList)-1):
            if itemList[element] > itemList[element+1]:
                moreSwaps = True
                temp = itemList[element]
                itemList[element] = itemList[element+1]
                itemList[element+1] = temp
    return itemList

def testBubbleSort():
    itemList = [5,2,7,1,9,3,6]
    print("Input given", itemList)
    sortedList = bubbleSort(itemList)
    print(sortedList)

testBubbleSort()