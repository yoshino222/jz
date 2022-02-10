#n场

def fuc(n):
    k=[]
    ans=1
    i=0
    if n<=2:
        return 1
    if 2<n<5:
        return n-1
    while n>=5:
            k.append(3)
            ans=ans*3
            n=n-3
    print(k)
    return ans*n

print(fuc(2))


