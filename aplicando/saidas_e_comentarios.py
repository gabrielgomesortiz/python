

A = 'maravilhoso'
n = 1233

# com cocatenação e soma
print("HELLO WORLD" + A)
print(n + 2)

# com virgula ','
print("HELLO WORLD", A)
print("HELLO WORLD", n)

# com %s
print("HELLO WORLD %s" %A)
print("HELLO WORLD %s" %n)

# com format
print("HELLO WORLD {}".format(A))
print("HELLO WORLD {}".format(n))

# com f e {}
print(f"HELLO WORLD {A}")
print(f"HELLO WORLD {n}")

#sep e end
    #sep:
print("HELLO WORLD", A, sep = '   L  ')
    #end
print("HELLO WORLD", A, end = ' ')
    #end + sep
print("HELLO WORLD", A, sep = '   L  ', end = '\n')


''' Na questão dos comentários é bem simples. Basta usar as aspas triplas (como neste texto que você está lendo) para selecionar mais de uma linha. Se preferir, use apenas o sinal de # para comentar apenas uma linha por vez. É isso, bem direto. ''' 



'''Pedi para a IA me mostrar um exemplo de flush. O flush é um argumento que define se os dados exibidos pelo print serão mostrados imediatamente na tela ou se serão guardados em um 'reservatório' (buffer) para serem mostrados todos de uma vez, que é o comportamento padrão do Python. É um recurso bem interessante!

Exemplo abaixo.

para testar o flush faça isso em arquivo separado, pois os prints esta todos configurados em false.
'''

import time

print("Contagem regressiva: ", end="")
for i in range(5, 0, -1):
    print(i, end=" ", flush=True) 
print("Fogo! 🚀")