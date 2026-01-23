'''Implemente o algoritmo de ordenação Merge Sort em Python.
O algoritmo deve ordenar uma lista de números em ordem crescente utilizando a técnica de divisão e conquista.
A implementação deve ser feita de forma recursiva, dividindo a lista em duas sublistas aproximadamente iguais até que cada sublista contenha apenas um elemento.
Em seguida, as sublistas devem ser intercaladas (merge) de forma ordenada, produzindo listas cada vez maiores até que a lista original esteja completamente ordenada.
Ao final da execução, a lista original deve estar ordenada em ordem crescente.'''


def controle_fluxo():    
    lista = [5, 3,1,3,6,9,0,98,2,4,5,7,8,2,323,1,4,6,0,7]
    ordenado = dividir_array(lista)
    return ordenado

def dividir_array(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista)//2
    esquerda = []
    direita = []
    i = 0
    while i < len(lista):
        if i <= meio-1:
            esquerda.append(lista[i])
        else:
            direita.append(lista[i])
        i+= 1
    esquerda = dividir_array(esquerda)
    direita = dividir_array(direita)

    return merge(esquerda,direita)


def merge(esquerda,direita):
    resultado = []
    i = j= 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] >= direita[j]:
            resultado.append(direita[j])
            j+=1
        else:
            resultado.append(esquerda[i])
            i+= 1
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i+= 1
    while j < len(direita):
        resultado.append(direita[j])
        j+= 1
    return resultado

print(controle_fluxo())