import math
math.pi

r=float(input('nhap vao ban kinh:'))
if r<0:
    print('khong hop le')


def tinh(r):


    cv=2*3.14*r
    print('cv=',cv)
    dt=3.14*(r**2)
    print('dt=',dt)
tinh(r)
print(tinh(r))

