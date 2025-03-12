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