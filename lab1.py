import math
import sys


# 1. Formatted Twinkle Poem
def twinkle_poem():
    print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are")


# 2. Python Version Checker
def python_version():
    import sys
    print("     Python Version")
    print(sys.version)
    print("     Version Info")
    print(sys.version_info)


# 3. Current Date and Time
def current_date_time():
    import datetime
    now = datetime.datetime.now()
    print("Current Date and Time: ")
    print(now)

# 4. Area of Circle
def area_of_circle(radius):

    area = math.pi * radius ** 2
    print("Area of Circle with r = ", radius, " => area = ", area)
# area_of_circle(1)

# 5. Reverse Full Name
def reverse_full_name(first_name, last_name):
    print(last_name, first_name)
# reverse_full_name("John", "Doe")

#6. List and Tuple Generator
def list_tuple_generator():
    values = input("Input some comma separated numbers: ")
    list = values.split(",")
    tuple1 = tuple(list)
    print("List: ", list)
    print("Tuple: ", tuple1)
# list_tuple_generator()

# 7. File Extension Extractor
def file_extension_extractor():
    filename = input("Input the Filename: ")
    extension = filename.split(".")
    print("The extension of the file is: ", extension[-1])
# 8. First and Last Colors
def first_last_colors():
    color_list = ["Red", "Green", "White", "Black"]
    print("First Color: ", color_list[0])
    print("Last Color: ", color_list[-1])
# 9. Exam Schedule Formatter
def exam_schedule_formatter():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from: %i/%i/%i" % exam_st_date)
# 10. Number Expansion Calculator
def number_expansion_calculator():
    number = int(input("Input a number: "))
    n1 = int("%s" % number)
    n2 = int("%s%s" % (number, number))
    n3 = int("%s%s%s" % (number, number, number))
    print("Result: ", n1+n2+n3)
# 11. Function Documentation Printer
def function_documentation_printer():
    print(abs.__doc__)
    print(int.__doc__)
    print(input.__doc__)
# 12. Monthly Calendar Display
def monthly_calendar_display():
    import calendar
    y = int(input("Input the year: "))
    m = int(input("Input the month: "))
    print(calendar.month(y, m))
# 13. Multi-line Here Document
def multi_line_here_document():
    print("""
    a string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example
    """)
# 14. Days Between Dates
def days_between_dates():
    from datetime import date
    f_date = date(2014, 7, 2)
    l_date = date(2014, 7, 11)
    delta = l_date - f_date
    print("Days between dates: ", delta.days)
# 15. Sphere Volume Calculator
def sphere_volume_calculator():
    r = float(input("Input the radius of the sphere: "))
    V = 4.0/3.0 * math.pi * r**3
    print("The volume of the sphere with radius ", r, " is: ", V)
# 16. Difference from 17
def difference_from_17(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2
# 17. Number Range Tester
def number_range_tester():
    n = int(input("Input a number: "))
    if n in range(10, 20):
        print("Number is in the range")
    else:
        print("Number is not in the range")
# 18. Triple Sum Calculator
def triple_sum_calculator(x, y, z):
    if x == y == z:
        return (x + y + z) * 3
    else:
        return x + y + z
# 19. Prefix "Is" String Modifier
def prefix_is_string_modifier():
    s = input("Input a string: ")
    if s[:2] == "Is":
        print(s)
    else:
        print("Is" + s)
# 20. String Copy Generator
def string_copy_generator():
    s = input("Input a string: ")
    n = int(input("Input a number: "))
    result = ""
    for i in range(n):
        result += s
    print(result)
# 21. Odd Even Number Checker
def odd_even_number_checker():
    n = int(input("Input a number: "))
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
# 22. Count 4 in List
def count_4_in_list():
    l = [1, 2, 3, 4, 5, 4, 4]
    print(l.count(4))
# 23. String Prefix Copies
def string_prefix_copies():
    s = input("Input a string: ")
    if len(s) < 2:
        print(s)
    else:
        print(s[:2] + s[:2] + s[:2] + s[:2])
# 24. Vowel Tester
def vowel_tester():
    s = input("Input a character: ")
    if s in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonant")
# 25. Value in Group Tester
def value_in_group_tester():
    l = [1, 5, 8, 3]
    n = int(input("Input a number: "))
    if n in l:
        print("Value is in the group")
    else:
        print("Value is not in the group")

    

#                              Bài 2: Viết hàm thực hiện các chức năng sau: 
# 1. Tính:
def add(a, b):
    return a+b

def chia(a, b):
    return a/b

def mu(a, b):
    return a**b

# 2. Tính diện tích hình chữ nhật khi biết bán kính
def dien_tich_hinh_chu_nhat(a, b):
    return a*b

def dien_tinh_hinh_tron(r):
    return 3.14*r*r

# 3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước
def Array_prime(n):
    if n < 2:
        return []
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num)):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
   
# print(Array_prime(100))

# 4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
def KtraFibonacci(n):
    a=0
    b=1
    while(b<n):
        (a,b)=(b,a+b)
        if(b==n):
            return True
    return False

# print(KtraFibonacci(9))

# 5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
def tim_so_fibonacci_thu_n(n):
    if n <= 0:    
        return 0
    elif n == 1:
        return 1
    else:
        return tim_so_fibonacci_thu_n(n - 1) + tim_so_fibonacci_thu_n(n - 2)  


def tim_so_fibonacci_thu_n_khong_de_quy(n):
    a=0
    b=1
   
    for i in range(2,n+1):
        a,b=b,a+b
        
    return b

# 6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy) 
def tim_tong_fibonacci_thu_n_khong_de_quy(n):
    a=0
    b=1
    tong =1
    for i in range(1,n):
        a,b=b,a+b
        tong+=b
    return tong


def tong_fibonacci_de_quy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return tim_so_fibonacci_thu_n(n) + tong_fibonacci_de_quy(n - 1)

# 7. Tính tổng căn bậc 2 của n số nguyên đầu tiên
def tong_can_bac_2(n):
    tong = 0
    for i in range(1,n+1):
        tong+=i**0.5
    return tong

# print(tong_can_bac_2(5))

# 8. Giải phương trình bậc 2: ax2 + bx + c=0 
def giai_phuong_trinh_bac_2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b/(2*a)
        return "Phương trình có nghiệm kép x = ", x
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        return "Phương trình có 2 nghiệm phân biệt x1 = ", x1, " và x2 = ", x2

# print(giai_phuong_trinh_bac_2(3, 4, 1))

# 9. Tính n! 
def tinh_giai_thua(n):
    if n == 0:
        return 1
    return n*tinh_giai_thua(n-1)

# 10. In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)
def in_hinh_tam_giac(n):
    for i in range(1,n):
        for j in range(1,i+1):
            if j == 1 or j == i:
                print("* ", end="")
            else:
                print("  ", end="")     
        print()
    print("* "*n) 

# print(in_hinh_tam_giac(10))

# 11.   Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây. 
# Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ: soGiay = 3770 thì xuất 
# ra màn hình 1:2:50. 

def doi_gio_phut_giay(so_giay):
    gio = so_giay//3600
    phut = (so_giay%3600)//60
    giay = (so_giay%60)
    return str(gio)+":"+str(phut)+":"+str(giay)
# print(doi_gio_phut_giay(3770))

# 12. Cho một mảng số nguyên: 
array = [1, 2, 3, 9, 4, 11, 6, 2, 8, 10,1,2,1,4,1,2]
print(array)
# a) Xuât tất cả các số lẻ không chia hết cho 5 
def so_le_khong_chia_het_cho_5(array):
    ket_qua = []
    for i in array:
        if i%2 != 0 and i%5 != 0:
            ket_qua.append(i)
    return ket_qua
# print(so_le_khong_chia_het_cho_5(array))

# b) Xuất tất cả các số Fibonacci 
def so_fibonacci(array):
    ket_qua = []
    for i in array:
        if KtraFibonacci(i):
            ket_qua.append(i)
    return ket_qua
# print(so_fibonacci(array))

# c) Tìm số nguyên tố lớn nhất 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def so_nguyen_to_lon_nhat(array):
    max =  -sys.maxsize
    
    for i in array:
        if is_prime(i) and (i > max):
            max = i
    return max
# print(so_nguyen_to_lon_nhat(array))

# d) Tìm số Fibonacci bé nhất 
def so_fibonacci_be_nhat(array):
    min = sys.maxsize
    for i in array:
        if KtraFibonacci(i) and i< min:
            min = i
    return min
# print(so_fibonacci_be_nhat(array))


# e) Tính trung bình các số lẻ 
def trung_binh_so_le(array):
    tong = 0
    dem = 0
    for i in array:
        if i%2 != 0:
            tong+=i
            dem+=1
    return tong/dem
print(trung_binh_so_le(array))

# f) Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng 
def tich_so_le_ko_chia_het_cho_3(array):
    tich = 1
    for i in array:
        if i%2 != 0 and i%3 != 0:
            tich*=i
    return tich

# g) Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ 
def doi_cho_2_phan_tu(array, i, j):
    array[i], array[j] = array[j], array[i]

# h) Đảo ngược trật tự các phần tử của danh sách
def dao_nguoc(array):
    l=0
    r=len(array)-1
    while l<r:
        array[l],array[r]=array[r],array[l]
        l+=1
        r-=1
    return array

def dao_nguoc_v2(array):
    return array[::-1]

# i) Xuất tất cả các số lớn thứ nhì của danh sách
def so_lon_thu_2(array):
    max1 = max2 = -sys.maxsize
    for i in array:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i < max1:
            max2 = i
    return max2

# print (so_lon_thu_2(array))

# j) Tính tổng các chữ số của tất cả các số trong danh sách 
def tong_chu_so(array):
    tong = 0
    for i in array:
        for j in str(i):
            tong+=int(j)
    return tong

# k) Đếm số lần xuất hiện của một số trong danh sách
def dem_so_lan_xuat_hien_cua_1_so(array,n):
    dem=0
    for i in array:
        if i == n:
            dem+=1
    return dem

# print(dem_so_lan_xuat_hien_cua_1_so(array, 2))
# l) Xuất các số xuất hiện n lần trong danh sách 
def so_xuat_hien_n_lan(array,n):
    ket_qua=[]
    for i in array:
        if dem_so_lan_xuat_hien_cua_1_so(array,i) == n:
            if(i not in ket_qua):
                ket_qua.append(i)
    return ket_qua

# print(so_xuat_hien_n_lan(array, 2))

# m) Xuất các số xuất hiện nhiều lần nhất trong danh sách
def so_xuat_hien_n_lan(array,n):
    ket_qua=[]
    max=-sys.maxsize
    for i in array:
        if dem_so_lan_xuat_hien_cua_1_so(array,i) > max:
            max = dem_so_lan_xuat_hien_cua_1_so(array,i)
    for i in array:
        if dem_so_lan_xuat_hien_cua_1_so(array,i) == max:
            if(i not in ket_qua):
                ket_qua.append(i)
    return ket_qua

print(so_xuat_hien_n_lan(array, 2))


        
    
            











