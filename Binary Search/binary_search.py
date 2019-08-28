def binarySearch(item, itemList):
    found = False
    bottom = 0
    top = len(itemList) - 1
    counter = 0
    while bottom<=top and not found:
        counter = counter + 1
        middle = (bottom+top)//2
        if itemList[middle] == item:
            found = True
        elif itemList[middle] < item:
            bottom = middle + 1
        else:
            top = middle - 1
    print(counter)
    return found

if __name__ == "__main__":
    numberList = [1,4,6,8,12,15,18,19,24,27,31,42,43,58]
    item = int(input("Enter the item to be found: "))
    isFound = binarySearch(item, numberList)
    if (isFound):
        print("Item is in the list")
    else:
        print("Item is not in the list")