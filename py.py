# tính tiền hôm nay cần phải tiết kiệm trong năm -- ngược

def LayNgayTrongThang (thang, nam):
        match(thang):
                case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                        return 31
                case 4 | 6 | 9 | 11:
                       return 30
                case 2:
                        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
                                return 29
                        else:
                                return 28 
                case default:
                        return 0

def TinhNgayTrongNam (ngay, thang, nam):
        ngaytrongnam = 0
        for i in range(1, thang):
                ngaytrongnam += LayNgayTrongThang(i, nam)
        ngaytrongnam += ngay
        return ngaytrongnam


def TinhTienPhaiTietKiem (n):
        sotien=365
        tong=0
        n=366-n
        for i in range(n, 366):
                tong+=sotien
                sotien-=1  
        return tong

        # return n * (n + 1) // 2

def Main():
        print("nhập ngày hôm nay của bạn:")
        ngay = int(input())
        thang = int(input())
        nam = int(input())
        print( TinhTienPhaiTietKiem(TinhNgayTrongNam(ngay, thang, nam)))

Main()
# n = 364
# tong = n * (n + 1) // 2
# print(tong)
