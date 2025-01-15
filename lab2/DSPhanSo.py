from lab2.PhanSo import PhanSo

class DSPhanSo:
    def __init__(self):
        self.ds = []
    def themPS(self, ps:PhanSo):
        self.ds.append(ps)
    def __str__(self) -> str:
        s = ""
        for ps in self.ds:
            s += ps.__str__() + "\n"
        return s
    def DemPhanSoAmTrongDS(self):
        return len([ps for ps in self.ds if ps.tu * ps.mau < 0])
    def TimPhanSoDuongNhoNhat(self):
        return min([ps for ps in self.ds if ps.tu * ps.mau > 0], key = lambda ps: ps.tu/ps.mau)
    def TimDSViTriCuaPhanSoX(self, x:PhanSo):
        return [i for i in range(len(self.ds)) if self.ds[i].tu/self.ds[i].mau == x.tu/x.mau]
    def TongPhanSoAm(self):
        return sum([ps for ps in self.ds if ps.tu * ps.mau < 0])
    def XoaPhanSoX(self, x:PhanSo):
        self.ds = [ps for ps in self.ds if ps.tu/ps.mau != x.tu/x.mau]
    def XoaTatCaPhanSoCoMauX(self, x:int):
        self.ds = [ps for ps in self.ds if ps.mau != x]
    def SapXepGiamDan(self):
        self.ds.sort(key = lambda ps: ps.tu/ps.mau, reverse = True)
    def SapXepTangDan(self):
        self.ds.sort(key = lambda ps: ps.tu/ps.mau)
    def SapXepTangDanTheoTu(self):
        self.ds.sort(key = lambda ps: ps.tu)
    def SapXepGiamDanTheoTu(self):
        self.ds.sort(key = lambda ps: ps.tu, reverse = True)
    def SapXepTangDanTheoMau(self):
        self.ds.sort(key = lambda ps: ps.mau)
    def SapXepGiamDanTheoMau(self):
        self.ds.sort(key = lambda ps: ps.mau, reverse = True)    