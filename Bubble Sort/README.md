#### Bubble Sort

This technique is used to compare and swap the elements with each other in ascending order. This requires an unsorted technique. Multiple iterations are required to achieve the proper order.

### Algorithm

```
Repeat
    X ← StartofArray
    Flag ← False
    Repeat
        If Number(X) > Number (X+ 1) Then
            Temp ← Number(X)
            Number (X) ← Number (X+ 1)
            Number(X+I) ← Temp
            Flag ← True
        End If
        X ← X+1
    Until EndofArray
Until Flag = False
```