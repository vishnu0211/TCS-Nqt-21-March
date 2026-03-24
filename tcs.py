n = int(input())
r = int(input())
start = "1"
end = input()

lst = []
if len(lst) == 0:
    for i in range(1 , r+1):
        if i == 1:
            continue
        else:
            lst.append(str(i))


ls = []
sam = []
for i in range(n-3):
    ls = []
    for x in lst:
        for j in range(r):
            if str(j+1) != x[-1]:
                ls.append(x+str(j+1))
                sam.append(x[i-1])
    lst = ls

print(ls)
print(sam)

l = []
for i in range(len(ls)):
    if ls[i][-1] != end:
        l.append(ls[i])

print(l)
print(len(l))

for i in range(5):
    for j in range(i):
        print(i, end = " ")
    print("")






            
