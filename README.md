# Python-basic-NTT

### 📫 Bài tập tách họ tên. Đếm số học sinh có họ nguyễn và trần, danh sách học sinh có tên Anh

#### Code
```python
# Hàm dùng để tách Họ vs Tên (ví dụ "Huỳnh Đăng Khanh" => Sẽ lấy ra họ là Huỳnh, và tên là Khanh)
# split() để chia chuỗi thành 
def tachHoTen(st):
    t = st.split()
    return t[0], t[len(t)-1]

# Mở file để đọc dữ liệu
fi = open("data.inp", 'r', encoding = 'utf-8')

# Đọc dòng đầu tiên trong file data.inp
st = fi.readline()

# Mảng chứa danh sách học sinh 
dshs = []

# Đọc tiếp các dòng tiếp theo trong data.inp đến khi không còn dòng nào nữa thì dừng,
# Mỗi lần đọc thì sẽ thêm học sinh đó vào mảng dshs
while st != '':
    dshs.append(st)
    st = fi.readline()
 
# Lưu số lượng học sinh vào n 
n = len(dshs)

demTran = 0
demNguyen = 0
dsTenAnh = []

# Lặp qua tất cả học sinh trong dshs
for hs in dshs:
    # Tách tên học sinh thành : ho vs ten (bằng cách gọi hàm tachHoTen(st) đã viết ở trên)
    ho, ten = tachHoTen(hs) 
    if ho == "Trần": demTran = demTran+1
    if ho == "Nguyễn": demNguyen = demNguyen+1
    # Nếu tên là học sinh đó là Anh thì lưu nó vào mang dsTenAnh
    if ten == "Anh": dsTenAnh.append(hs)
    
# In kết quả ra file data.out
fo = open("data.out", 'w', encoding = 'utf-8')

# In ra số lượng học sinh có Họ là Trần và số lượng học sinh có họ là Nguyễn
fo.write(str(demTran) + " " + str(demNguyen) + "\n")

# In ra ds các học sinh có tên Anh
for t in dsTenAnh:
    fo.write(t)
    
# Đóng các file đã mở    
fo.close()
fi.close()
```

#### file data.inp
```bash
Nguyễn Hoa
Trần Thanh Tâm
Nguyễn Nhật Anh
Trần Thanh Nhàn
Huỳnh Đăng Anh
Trần Hồng Mai
```
### Sau khi chạy code trên thì sẽ được kết quả trong file data.out như bên dưới:

#### file data.out 
```bash
3 2
Nguyễn Nhật Anh
Huỳnh Đăng Anh
```





# 📫 Bài tập tính tổng dãy số, tìm số chia hết cho 3, và sắp xếp giảm dần 

#### Code
```python
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
```

#### file data.inp
```bash
5
2 4 3 6 1
```
### Sau khi chạy code trên thì sẽ được kết quả trong file như bên dưới:

#### file data.out 
```bash
16
3 6 
6 4 3 2 1 
```
