#Sequencia de Fibonacci
inicio = int(input("Digite um número inicial para sequência de Fibonacci : "))
antes = 1
depois = 1

for i in range(0, inicio,):
    print(antes)
    soma = antes + depois
    antes = depois
    depois = soma

if inicio <= 0:
    print("Sequência Invalida")