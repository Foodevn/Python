from lab2.DanhSachSV import DanhSachSV
from PhanSo import PhanSo

DanhSachSV1 = DanhSachSV()
DanhSachSV1.themTuFileTXT("D:\\Bai_Thuc_Hanh\\python\\lab2\\dssv.txt")
print(DanhSachSV1   )

DanhSachSV1.SapXepTangTheoTen()
print(DanhSachSV1)

DanhSachSV1.SApXepGiamTheoTen()
print(DanhSachSV1)

PhanSo1 = PhanSo(37, 18)
PhanSo1.rutGon()
print(PhanSo1)

PhanSo2 = PhanSo(3, 4)
print(PhanSo2)
PhanSo3 = PhanSo1 + PhanSo2
PhanSo3.rutGon()
print(PhanSo3)
