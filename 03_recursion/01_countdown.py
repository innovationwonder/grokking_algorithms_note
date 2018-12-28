def countdown(i):
    print(i)
    # 基线条件
    if i <= 1:
        return
    # 递归条件
    else:
        countdown(i-1)

countdown(10)