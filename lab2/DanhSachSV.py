from datetime import datetime
from SinhVien import SinhVien
from SinhVienChinhQuy import SinhVienChinhQuy
from SinhVienPhiChinhQuy import SinhVienPhiChinhQuy
  
  
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
                mssv = int(parts[0])
                hoten = parts[1]
                ngaysinh = datetime.strptime(parts[2], "%d/%m/%Y")
                 
                if len(parts) == 4:
                    diemRL = int(parts[3])
                    sv = SinhVienChinhQuy(mssv, hoten, ngaysinh, diemRL)

                else:
                    trinhdo = parts[3]
                    thoiGianDaoTao = int(parts[4])
                    sv = SinhVienPhiChinhQuy(mssv, hoten, ngaysinh, trinhdo, thoiGianDaoTao)
                
            
                # sv = SinhVien(mssv, hoten, ngaysinh)
                self.themSV(sv)

    def SapXepTangTheoTen(self):
        self.ds.sort(key = lambda sv: sv.hoten.split()[-1])

    def SApXepGiamTheoTen(self):
        self.ds.sort(key = lambda sv: sv.hoten.split()[-1], reverse = True)
    
    def TimSinhVienTheoLoai(self, loai:str):
        if loai in "sinh vien chinh quy":
            return [sv for sv in self.ds if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.ds if isinstance(sv, SinhVienPhiChinhQuy)]
    
    def SinhVienCoDiemRLXTroLen(self,x:int):
        return[sv is SinhVienChinhQuy for sv in self.ds if isinstance(sv, SinhVienChinhQuy) and sv.diemRL>50  ]
        