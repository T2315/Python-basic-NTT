def InsertionSort(A):
    n = len(A)
    for i in range(1, n):
        value = A[i]
        j = i-1
        while j >= 0 and A[j] < value:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = value
def SelectionSort(A):
    n = len(A)
    for i in range(n):
        iMin = i
        for j in range(i+1, n):
            if A[j] > A[iMin]: iMin = j
        A[i], A[iMin] = A[iMin], A[i]
def BubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] < A[j+1]: A[j], A[j+1] = A[j+1], A[j]

fi = open("data.inp", "r", encoding = "utf-8")
n = int(fi.readline())
st = fi.readline().split()
a = []
for x in st:
    a.append(int(x))

fo = open("data.out", "w", encoding = "utf-8")

tong=0
for x in a: tong = tong + x
fo.write(str(tong) + '\n')

for x in a:
    if x%3 == 0: fo.write(str(x) + " ")
fo.write('\n')

BubbleSort(a)
for x in a: fo.write(str(x) + " ")

fo.close()
fi.close()
