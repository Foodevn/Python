from SinhVien import SinhVien
from datetime import datetime
class SinhVienPhiChinhQuy(SinhVien):
    def __init__(self, mssv:int, hoten:str, ngaysinh:datetime, trinhdo:str, ThoiGianDaoTao:int)->None:
        super().__init__(mssv, hoten, ngaysinh)
        self.thoiGianDaoTao = ThoiGianDaoTao
        self.trinhdo = trinhdo
    

    def __str__(self)->str:
        return super().__str__() + f", Trình độ: {self.trinhdo}, Thời gian đào tạo: {self.thoiGianDaoTao} năm"
    