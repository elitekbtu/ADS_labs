n = int(input())
a = list(map(int, input().split()))
a.insert(0,0)
for i in range(n):
    if i==0:
        print(-1, end=' ')
    elif a[i]<a[i+1]:
        print(a[i], end=" ")
    elif i==n-1:
        print(1, end=' ')
    else:
        print(-1, end=' ')



