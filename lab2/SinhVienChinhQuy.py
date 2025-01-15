from lab2.SinhVien import SinhVien
from datetime import datetime
class SinhVienChinhQuy(SinhVien):
    def __init__(self, mssv:int, hoten:str, ngaysinh:datetime, diemRL:int)->None:
        super().__init__(mssv, hoten, ngaysinh)
        self.diemRL = diemRL
    

    def __str__(self)->str:
        return super().__str__() + f", Điểm rèn luyện: {self.__diemRL}"