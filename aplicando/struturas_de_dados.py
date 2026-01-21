#    numerics = int, float e complex
inteiro = 23
decimais = 24.8
complexos = 3 + 4j
print('os numeros são {}, {}, {}'.format(inteiro,decimais, complexos ))

#   text = str
string = "lindo"
print(string)

#   collection = list, tuple, range, set e dict
list_frutas = ["maçã", "banana", "laranja"]
tuple_coordenadas = (10, 20)

'''range sintax
Apenas o fim 1 numero n de elementos(começa do 0 e vai até o n)
Início n e fim m (de n até m)
n, m e passo: p (de n até m, pulando de p em p)
E para armazenar o conteudo nessa estrutura de dados tem que acom-panhar ela do list()'''

range_lista = list(range(1,8))
set_numeros_primos = {2, 3, 5, 7, 11, 13}
dict_pessoa = {"nome": "Ana", "idade": 30, "profissao": "Engenheira"}
print('As listas são {}, {}, {}, {} e {}'.format(list_frutas, tuple_coordenadas,range_lista,set_numeros_primos, dict_pessoa) )


#   boolean = bool
boolean_false = False
boolean_true = True

print('os numeros são {} e {}'.format(boolean_false,boolean_true))

#   none = noneType
none = None

print(f'esse é o vazio {none}' )