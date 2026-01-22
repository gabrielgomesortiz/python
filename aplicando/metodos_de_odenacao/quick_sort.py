'''Implemente o algoritmo de ordenação quick sort em Python. O algoritmo deve ordenar uma lista de números em ordem crescente, utilizando a técnica de divisão e conquista. A implementação deve 
ser feita de forma recursiva, realizando a partição da lista a partir de um elemento pivô e 
reorganizando os elementos menores à esquerda e os maiores à direita. Ao final da execução, a 
lista original deve estar ordenada.'''


def controle_fluxo():
    lista = [5, 3,1,1,2,3,4,0.5,999999, 8,5,5,5, 4, 2, 80,1.5,987,3,0.5]
    ordenado = quick_sort(lista)
    return ordenado

#aqui é o coração do algoritmo. aqui fiz 3 partições da lista: > , < e =
def quick_sort(lista):
    length = len(lista)
    if length <= 1:
        return lista
    pivo = lista[0]
    maiores =[]
    iguais = [pivo]
    menores = []
    i = 1
    while i < length:

        if lista[i] < pivo:
            menores.append(lista[i])
        elif lista[i] > pivo:
            maiores.append(lista[i])
        else:
            iguais.append(lista[i])
        i+=1

    return quick_sort(menores) + iguais + quick_sort(maiores)

print(controle_fluxo())
