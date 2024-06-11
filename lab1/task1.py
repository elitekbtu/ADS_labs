n = int(input())
while n!=0:
    
    a = int(input())
    sandar = []
    for i in range(a,0,-1):
        sandar.insert(0,i)
        for j in range(0,i,1):
            num = sandar[len(sandar)-1]
            sandar.pop(len(sandar)-1)
            sandar.insert(0, num)
    print(*sandar)
    n-=1
    
