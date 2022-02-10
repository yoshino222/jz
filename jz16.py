def p(x,n):
    sums=1
    if n>0:
        for _ in range(n):
            sums=sums*x
        return sums
    if n==0:
        return 1
    if n<0:
        x=1/x
        for _ in range(abs(n)):
            sums=sums*x
        return sums
print(p(2.10000,3))
a=pow(2,3)

def mypow(x,n):#利用位运算 二分法 减少时间
    res=1
    if x==0:
        return 0
    if n<0:x,n=1/x,-n
    while n:
        if n&1:res=res*x#n&1 判断奇偶
        x*=x
        n>>=1
    return res
