from datetime import datetime


class SinhVien:
    truong="Đại Học Đà Lạt"
    def __init__(self, mssv:int , hoten:str, ngaysinh:datetime):
        self.__mssv = mssv
        self.__hoten = hoten
        self.__ngaysinh = ngaysinh

    @property
    def mssv(self):
        return self.__mssv
    @property
    def hoten(self):
        return self.__hoten
    @property
    def ngaysinh(self):
        return self.__ngaysinh
    
    @mssv.setter
    def mssv(self, mssv):
        if self.laMaSoHopLe(mssv):
            self.__mssv = mssv

    @hoten.setter
    def hoten(self, hoten):
        self.__hoten = hoten

    @ngaysinh.setter
    def ngaysinh(self, ngaysinh):
        self.__ngaysinh = ngaysinh
    
    @staticmethod
    def laMaSoHopLe(mssv:int):
        return len(str(mssv))==7
    
    @staticmethod
    def doiTenTruong(self,truong:str):
        self.truong = truong

    def __str__(self) -> str:
        return f"MSSV: {self.mssv}, Họ tên: {self.hoten}, Ngày sinh: {self.ngaysinh}, Trường: {self.truong}"