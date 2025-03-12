# Thuật toán sắp xếp chèn
def InsertionSort(A):
    n = len(A)
    for i in range(1, n):
        value = A[i]
        j = i-1
        while j >= 0 and A[j] < value:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = value
# Thuật toán sắp xếp chọn
def SelectionSort(A):
    n = len(A)
    for i in range(n):
        iMin = i
        for j in range(i+1, n):
            if A[j] > A[iMin]: iMin = j
        A[i], A[iMin] = A[iMin], A[i]
# Thuật toán sắp xếp nổi bọt
def BubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] < A[j+1]: A[j], A[j+1] = A[j+1], A[j]

# Mở file đọc dữ liệu
fi = open("data.inp", "r", encoding = "utf-8")
# Đọc số n
n = int(fi.readline())
# Đọc chuỗi chứa n số tách chuỗi thành mảng của số ví dụ "1 2 3" -> ["1", "2", "3"]
st = fi.readline().split()
# Mảng lưu dánh sách các số 
a = []
for x in st:
    a.append(int(x))

# Mở file in kết quả 
fo = open("data.out", "w", encoding = "utf-8")

# Tính tổng của mảng (lặp qua mảng mỗi lần lặp cộng từ phần từ đó vs biến "tong")
tong=0
for x in a: tong = tong + x
fo.write(str(tong) + '\n')

# In ra các số chia hết cho 3 ( lặp qua mảng mỗi lần lặp kiểm tra xem số đó có chia hết cho 3 không nếu có thì in nó ra)
for x in a:
    if x%3 == 0: fo.write(str(x) + " ")
fo.write('\n')

# Sắp xếp lại mang theo thứ tự giảm dần ( Gọi hàm BubbleSort(a) đã viết ở trên đầu trước đó để sắp xếp, sau đó lặp qua mảng in từng phần tử ra)
BubbleSort(a)
for x in a: fo.write(str(x) + " ")

fo.close()
fi.close()