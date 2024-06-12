a = [False]*100001
for i in range(2, 100001):
    if a[i]==False:
        for j in range(2*i, 100001, i):
            a[j]=True
prime=[]
for i in range(2, 100001):
    if a[i]==False:
        prime.append(i)

a = [False]*len(a)
for i in range(2, len(a)):
    if a[i]==False:
        for j in range(2*i, len(a), i):
            a[j]=True

n = int(input())
sum = 0
for i in range(2, len(a)):
    if a[i]==False:
        sum+=1
    if sum==n:
        print(prime[i-1])
        break
    

