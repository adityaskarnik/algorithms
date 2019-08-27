#### Linear Search is used to find an Item in a list, where the list need not be in order. To find an item in the list, start by looping in the list from the beginning and continue till the end.

### Algorithm

```
position -> 0
found -> False
while position < length(List) and item no found:
    if List[position] = item:
        found <- True
    position <- position + 1
return List
```
