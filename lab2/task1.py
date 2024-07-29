n = int(input())
array = list(map(int, input().split()))
close = 10000000
m = int(input())
iter = 0
for i in array:
    if abs(i-m)<close:
        close = abs(i-m)
        index = iter
    iter+=1
print(index)