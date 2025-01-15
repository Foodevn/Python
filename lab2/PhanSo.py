


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
    def rutGon(self):
        ucln = self.UCLN(self.tu, self.mau)
        self.tu = self.tu // ucln
        self.mau = self.mau // ucln

    def UCLN(self, a, b):
        if b == 0:
            return a
        return self.UCLN(b, a % b)
    
    def __add__(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)
    
    def __sub__(self, other):
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)
    
    def __mul__(self, other):
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)
    
    def __truediv__(self, other):
        tu = self.tu * other.mau
        mau = self.mau * other.tu
        return PhanSo(tu, mau)
