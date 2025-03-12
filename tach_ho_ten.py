def tachHoTen(st):
    t = st.split()
    return t[0], t[len(t)-1]

fi = open("data.inp", 'r', encoding = 'utf-8')
st = fi.readline()
dshs = []

while st != '':
    dshs.append(st)
    st = fi.readline()
    
n = len(dshs)
demTran = 0
demNguyen = 0
dsTenAnh = []

for hs in dshs:
    ho, ten = tachHoTen(hs) 
    if ho == "Trần": demTran = demTran+1
    if ho == "Nguyễn": demNguyen = demNguyen+1
    if ten == "Anh": dsTenAnh.append(hs)
    
fo = open("data.out", 'w', encoding = 'utf-8')

fo.write(str(demTran) + " " + str(demNguyen) + "\n")

for t in dsTenAnh:
    fo.write(t)
    
fo.close()
fi.close()
