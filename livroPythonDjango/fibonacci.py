def fibonacci(n):
    """Função recursiva para gerar os númeos da sequencia de Fibonacci"""
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
tamanho = int(input("Deseja gerar quantos termos da sequencia de Fibonacci? "))

if tamanho <= 0:
    print("Quantidade invalida!")
else:
    print("Sequencia de Fibonacci: ")
    for i in range(tamanho):
        print(fibonacci(i))
