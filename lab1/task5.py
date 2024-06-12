coloda = '1234567890'
borya = list(map(str, input().split()))
nurs = list(map(str, input().split()))
sum_bor = 0
sum_nur = 0
for i in range(5):
    if coloda.index(borya[i])==coloda.index(nurs[i]):
        sum_bor+=1
        sum_nur+=1
    elif coloda.index(borya[i])>coloda.index(nurs[i]):
        sum_bor+=1
    else:
        sum_nur+=1

if sum_bor == sum_nur:
    print("blin nichiya")
elif sum_bor>sum_nur:
    print(f"Boris {sum_bor}")
else:
    print(f"Nursik {sum_nur}")