n = int(input())
a = [False]*100001
for i in range(2, 100001):
    if a[i]==False:
        for j in range(2*i, 100001, i):
            a[j]=True
sum = 0
for i in range(2, 100001):
    if a[i]==False:
        sum+=1
    if sum==n:
        print(i)
        break

