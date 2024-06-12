a = [False]*100001
a[1] = True
for i in range(2, 100001):
    if a[i]==False:
        for j in range(2*i, 100001, i):
            a[j]=True


n = int(input())
if a[n]==False:
    print("YES")
else:
    print("NO")