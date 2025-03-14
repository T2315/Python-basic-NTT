def BubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j][0].split()[-1] > A[j+1][0].split()[-1]: A[j], A[j+1] = A[j+1], A[j]
            
fi = open("data.inp", "r", encoding = "utf-8")
 
n = int(fi.readline())
 
dshs = []

for i in range(n):
    hs = fi.readline().split() 
    ten = " ".join(hs[:-1])
    
    diem = float(hs[-1])
    
    dshs.append([ten, diem])

fo = open("data.out", "w", encoding="utf-8")

max = 0 
ten = "" 

for i in range(n):
    if dshs[i][1] > max:
        max = dshs[i][1]
        ten = dshs[i][0]
        
fo.write(ten +"\n")

BubbleSort(dshs)
for i in range(n):
    fo.write(str(dshs[i][0]) + " " + str(dshs[i][1]) + "\n")


fi.close()
fo.close()