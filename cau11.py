t=float(input("lãi sát tiết kiệm là:"))
n=int(input("nhập số tiền vốn ban đầu:"))
k=int(input("nhập số thnags gửi:"))


def benefit(t,n,k):
    tienlai=n*(t/100)*k
    print("so tien lai la:",tienlai)
    tong=n+tienlai
    print("tong so tien lai la:",tong)
benefit(t,n,k)

