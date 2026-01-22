'''Implemente o algoritmo de ordenação Merge Sort em Python.
O algoritmo deve ordenar uma lista de números em ordem crescente utilizando a técnica de divisão e conquista.
A implementação deve ser feita de forma recursiva, dividindo a lista em duas sublistas aproximadamente iguais até que cada sublista contenha apenas um elemento.
Em seguida, as sublistas devem ser intercaladas (merge) de forma ordenada, produzindo listas cada vez maiores até que a lista original esteja completamente ordenada.
Ao final da execução, a lista original deve estar ordenada em ordem crescente.'''


def controle_fluxo():    
    lista = [5, 3,1,3,6,9,0]
    ordenado = dividir_array(lista)
    return ordenado

def dividir_array(lista):
    if len(lista)<=1:   
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
    return dividir_array(esquerda), dividir_array(direita)

    


print(controle_fluxo())