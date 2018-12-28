def binary_search(list, item):
    start_point = 0 # 查找的起始索引
    end_point = len(list)-1 # 查找的结束索引，跟踪查找的数组部分

    # 只要范围没有缩小到只包含一个元素,即起始索引和结束索引即将重合
    while start_point <= end_point:

        # 每次都检查中间的元素
        mid = (start_point + end_point) // 2
        guess = list[mid]

        # 如果找到了元素,返回位置
        if guess == item:
            return mid
        # 如果猜的数字小了， start_point 后移
        if guess < item:
            start_point = mid + 1
        # 如果猜的数字大了，就相应修改 end_point 左移
        if guess > item:
            end_point = mid - 1

    # 列表中不含有指定元素
    return None

a = binary_search(range(1,100), 5)
print(a)
