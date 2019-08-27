def linearSearch(myList, myItem):
        found = False
        position = 0
        while position < len(myList) and not found:
            if myList[position] == myItem:
                found = True
            position = position + 1
        return found

if __name__ == "__main__":
    shopping = ["apples", "banana", "chocolate", "pasta"]
    item = input("What item you want to find? " )
    isFound = linearSearch(shopping, item)
    if (isFound):
        print("Item is found")
    else:
        print("Item not found")