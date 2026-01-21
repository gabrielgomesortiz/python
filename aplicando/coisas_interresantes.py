'''praticar um prouco de formatação de print nesse arquivo além de 
pequenos teste de funções que estão no livro Automatize Tarefas 
Maçantes com Python (Al Sweigart)'''

# Método .index() (busca de índice)
spam = [1,2,3,4]
posicao = spam.index(1)
print('teste de index bem legal {} e esse é o item que esta nesse indix {}'.format(posicao, spam[posicao] ))

#metdo append e insert

teste = ["q","q","f","9","p"]

#append adiciona direto
teste.append('ele')

teste.insert(0,'lindo')

print(f'olha só que legal {teste}')

# remove

teste.remove("lindo")
print(f"agora com remove olha só que massa {teste}")

# função de ordenamento rapido sort
#só para testar coloquei um numero complexo mas não funciona python não deixa 1 + 4j
numeros = [1,8,3,90,34,78,1,0,0.9]

numeros.sort()

print('olha só que bacna esse metodo: %s'%numeros)

# testei tuple e list que eles são conversores. tupla(imutavel) converte lista em
# tupla e list coverte tupla em lista(mutavel)

tupla = ("olha só","vai que dá", "então")
lista = [1,2,3,434,5,6566,7]

print(f"antes lista agpra tupa {tuple(lista)} e antes tupla e agora lista {list(tupla)} bem legal")

