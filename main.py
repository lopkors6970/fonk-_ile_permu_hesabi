def permu(n,r): 
    i =1
    toplamn= 1
    toplamr= 1 
    k = 1
    p = 0
    while i<=n:
        toplamn*=i
        i+=1
    while k<=n-r:
        toplamr*=k
        k+=1
    p = toplamn/toplamr
    return p

a = int(input("Permütasyon 1.değerini giriniz:"))
b = int(input("Permütasyon 2.değerini giriniz:"))
result = permu(a,b)
print(result)


