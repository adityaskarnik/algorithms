#### Binary Search is used to find an item in an Ordered List

To search for an item, start search from the middle, if the item is in the middle, lower to the middle of the item or else above the middle item. If the item is in the middle of the list you have found the item. If the item is in at the higher then the middle item, set the bottom to one plus the middle position in the list. If the item is to the lower side, then set the higher position to the minus one of the middle position. 

### Algorithm:

```
Found -> False
while not Found and first <= last
    middle_point <- (first + last) DIV 2
    If List(middle_point) = Item Then
        Found <- True
    Else
        If List[middle_point] > Item Then
            Last <- middle_point - 1
        Else
            First <- middle_point + 1
        Endif
    Endif
```