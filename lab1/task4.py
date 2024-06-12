s = input()
a = list(s.split("s"))
s = ''
for i in a:
    s+=i
if s == s[::-1]:
    print("YES")
else:
    print("NO")

