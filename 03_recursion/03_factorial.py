from functools import reduce


def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

def xunhuan(x):
    a = 1

    for i in range(1,x+1):
        a = a*i
    return a

# 使用 reduce()
n = 5
a = reduce(lambda x,y: x*y, range(1, n+1))
print(a)

print(fact(5))

print(xunhuan(5))