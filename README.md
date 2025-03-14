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


## 📫 Bài tập mới
#### Đề bài
THI GIỮA KỲ II

Cho tệp dữ liệu data.inp gồm:

Dòng đầu tiên, chứa số nguyên n là số lượng học sinh của lớp.
n dòng tiếp theo, mỗi dòng chứa dữ liệu thông tin gồm:
Họ và tên đầy đủ của học sinh.
Điểm trung bình (có 2 chữ số thập phân).
Viết chương trình đọc dữ liệu từ tệp data.inp và ghi vào tệp data.out gồm:

Dòng đầu tiên ghi họ và tên của bạn có điểm trung bình cao nhất.
Sắp xếp lại danh sách học sinh kèm điểm trung bình theo thứ tự tên tăng dần.


#### Code
```python
# Do mỗi phần tử trong mảng là một mảng con của 2 phần tử [họ tên, điểm]
# Nên để sắp xếp theo tên thì ta phải lấy ra phần tử đầu tiên là họ tên
# Dùng split() để tách họ tên thành mảng gồm : họ, tên lót, tên
# sau đó thêm [-1] đằng sau để lấy ra tên làm tiêu trí so sánh để sắp xếp
# Nên ta mới có điều kiện : A[j][0].split()[-1] > A[j+1][0].split()[-1]
def BubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j][0].split()[-1] > A[j+1][0].split()[-1]: A[j], A[j+1] = A[j+1], A[j]
            
fi = open("data.inp", "r", encoding = "utf-8")
 
# Đọc số nguyên n
n = int(fi.readline())
 
# Mảng chứa danh sách học sinh của lớp
dshs = []

for i in range(n):
    # Đọc sanh sách học sinh của lớp, chia thông tin mỗi học sinh ra thành mảng theo khoảng trẳng
    # Ví dụ: "Nguyen Van A 7.88" => ["Nguyen", "Van", "A", "7.88"]
    hs = fi.readline().split()
    
    # hs[:-1] = lấy từ mảng trên từ đầu đến phần tử kế cuối, bỏ phần tử cuối do nó là điểm
    # Ví dụ kết quả hs[:-1] => ["Nguyen", "Van", "A"]
    
    # join để kết hợp mảng thành chuỗi bằng dấu sách
    # Ví dụ ["Nguyen", "Van", "A"] (sau khi " ".join() ta sẽ được) "Nguyen Van A" 
    ten = " ".join(hs[:-1])
    
    # hs[-1] lấy ra phần tử cuối cùng là điểm 
    diem = float(hs[-1])
    
    # chúng vào mảng dshs, mỗi phần tử là một mảng có 2 thông tin tách biệt [tên, điểm] 
    dshs.append([ten, diem])

fo = open("data.out", "w", encoding="utf-8")

# Tìm họ và tên bạn có điểm trung bình cao nhất 
max = 0 # Biến để lưu lại điểm trung bình cao nhất
ten = "" # Biến lưu lại tên của học sinh có điểm trung bình cao nhất

# Lặp qua dshs sau đó ở mỗi phần tử lấy ra điểm để so sánh nếu điểm đó lớn hơn max thì thay max bằng điểm của học sinh đó và gán lại tên
for i in range(n):
    if dshs[i][1] > max:
        max = dshs[i][1]
        ten = dshs[i][0]
        
fo.write(ten +"\n")

# Gọi hàm sắp xếp tăng dần theo điểm 
BubbleSort(dshs)
# In ra danh sách học sinh đã sắp xếp 
for i in range(n):
    fo.write(str(dshs[i][0]) + " " + str(dshs[i][1]) + "\n")


fi.close()
fo.close()
```
