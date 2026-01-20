'''Se number for par, collatz() deverá exibir n = n / 2 e retornar esse valor.
Se number for ímpar, collatz() deverá exibir e retornar n = 3*n + 1'''

while True:
    #basico:
    number = int(input("digite seu numero (aqui é so o while): "))

    def collatz(number):
        sequence = [number]
        numero_comparacao = number
        while numero_comparacao!=1:
            if numero_comparacao % 2 == 0:
                numero_comparacao = numero_comparacao // 2
                sequence.append(numero_comparacao)
            elif numero_comparacao % 2 == 1:
                numero_comparacao = 3*numero_comparacao + 1
                sequence.append(numero_comparacao)
        
        print(sequence)

    collatz(number)


    #vamos complicar um pouco
    n = int(input("digite seu numero (aqui é só uma função recursiva): "))
    sequence = [n]
    def collatz(n):
            if n!=1:
                if n % 2 == 0:
                    n = n // 2
                    sequence.append(n)
                    return collatz(n)
                elif n % 2 == 1:
                    n = 3*n + 1
                    sequence.append(n)
                    return collatz(n)
            else:
                return sequence
            
    print(collatz(n))
