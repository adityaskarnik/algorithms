def linearSearch(myList, myItem):
        found = False
        position = 0
        while position < len(myList) and not found:
            if myList[position] == myItem:
                found = True
            postion = position + 1
        return found

if if __name__ == "__main__":
    passopping = ["apples", "banana", "chocolate", "pasta"]
    item = input("What item you want to find? " )
    isFound = linearSearch(item, shopping)
    if (isFound):
        print("Item is found")
    else:
        print("Item not found")