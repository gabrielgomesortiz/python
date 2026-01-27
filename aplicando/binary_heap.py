'''teste de manipular e criar binary heap'''

#1 retornar os pais 

def controle_fluxo():
    array = [4,2,8,7,1,5,3,6,10]
    lenght = len(array)
    gerar_binary_heap = gerar_heap(lenght,array)
    return gerar_binary_heap
def gerar_heap(length,array):
    pais = []
    i = 0
    while i <= length // 2 -1 :
        pais.append(array[i])
        i += 1
    return pais

print(controle_fluxo())