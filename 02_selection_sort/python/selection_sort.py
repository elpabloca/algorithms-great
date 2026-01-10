def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

def reverseArray(arr):
    arr.reverse()
    return arr



my_list = [40, 7, 30, 8, 20, 9]

print(my_list, 'original array')
print(selectionSort(my_list), 'array sorted')
print(reverseArray(selectionSort(my_list)), 'reverse the array')