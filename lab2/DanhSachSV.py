from datetime import datetime
from lab2.SinhVien import SinhVien
from lab2.SinhVienChinhQuy import SinhVienChinhQuy
from lab2.SinhVienPhiChinhQuy import SinhVienPhiChinhQuy
  
  
class DanhSachSV:
    def __init__(self):
        self.ds = []
    
    def themSV(self, sv:SinhVien):
        self.ds.append(sv)
    
    def timSVTheoMaSo(self, mssv:int):
        for sv in self.ds:
            if sv.mssv == mssv:
                return sv
        return None
    
    def timVTSVTheoMaSo(self, mssv:int):
        for i in range(len(self.ds)):
            if self.ds[i].mssv == mssv:
                return i
        return -1
    
    def xoaSVTheoMaSo(self, mssv:int):
        vt = self.timVTSVTheoMaSo(mssv)
        if vt != -1:
            self.ds.pop(vt)
        return vt
    
    def timSVTheoTen(self, hoten:str):
        return [sv for sv in self.ds if hoten in sv.hoten]
    
   
    
    def __str__(self) -> str:
        s = ""
        for sv in self.ds:
            s += sv.__str__() + "\n"
        return s  

    def themTuFileTXT(self, filename:str):
        with open(filename, "r",encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                parts = line.split(",")
                if len(parts) == 3:
                    mssv, hoten, ngaysinh = parts
                mssv = int(mssv)
                ngaysinh = datetime.strptime(ngaysinh, "%d/%m/%Y")
                sv = SinhVien(mssv, hoten, ngaysinh)
                self.themSV(sv)

    def SapXepTangTheoTen(self):
        self.ds.sort(key = lambda sv: sv.hoten)

    def SApXepGiamTheoTen(self):
        self.ds.sort(key = lambda sv: sv.hoten, reverse = True)
    
    def TimSinhVienTheoLoai(self, loai:str):
        return [sv for sv in self.ds if isinstance(sv, loai)]