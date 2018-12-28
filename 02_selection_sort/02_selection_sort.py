# 将数组元素按照从小到大排序

# Finds the smallest value in an array
def findSmallest(arr):
    '''
    存储最小元素的值和索引
    遍历列表
    :param arr:
    :return: 索引
    '''
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index
# Sort array
def selectionSort(arr):
    '''
    对数组进行排序
    使用上面定义的函数找出数组中最小的元素并添加到新数组中，从而实现排序
    :param arr:
    :return: 新数组
    '''
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
