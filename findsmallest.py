def find(arr):
    smalest = arr[0]
    smalest_index = 0

    for i in range(len(arr)):
        if smalest > arr[i]:
            smalest = arr[i]
            smalest_index = i
    return smalest_index

def sort(arr):
    newArr= []
    for i in range(len(arr)):
        smalest = find(arr)
        newArr.append(arr.pop(smalest))
    return newArr

print(sort([7456,234,176,32,1,3784]))