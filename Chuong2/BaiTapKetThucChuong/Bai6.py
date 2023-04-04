hoten=input("Ho ten: ")
songaycong=int(input("So ngay cong: "))
dongiangaycong=int(input("Don gia ngay cong: "))
hesophucap=float(input("He so phu cap: "))
tamung=int(input("Tam ung: "))
luong=dongiangaycong*songaycong*hesophucap
thuclinh=luong-tamung
print("Nhan vien",hoten,end="")
print(", Co tien Luong=",luong,end="")
print(", Tam ung=",tamung,end="")
print(" va Thuc linh=",thuclinh)