def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res = (fibo(n-2)) + (fibo(n-1))
        return res

n=int(input("Digite um valor: "))
print(fibo(n))

for l in range (fibo(n)):
    print(l, end=" - ")
