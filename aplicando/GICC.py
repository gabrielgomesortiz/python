'''
Grade para imagem composta de caracteres
Suponha que você tenha uma lista de listas em que cada valor das listas
internas seja uma string de um caractere como:

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

Podemos pensar em grid[x][y] como sendo o caractere nas coordenadas x e
y de uma “imagem” desenhada com caracteres textuais. A origem (0, 0) estará
no canto superior esquerdo, as coordenadas x aumentam para a direita e as
coordenadas y aumentam para baixo.
Copie o valor da grade anterior e crie um código que a utilize para exibir a
imagem:
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
'''


def printar_array_formatado():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    nova_matriz = manipular_Grid(grid)
    lenght_geral = len(nova_matriz)
    lenght_linha = len(nova_matriz[0])
    matriz = ""
    i = 0
    while i < lenght_geral:
        j =0
        while j < lenght_linha:
            matriz += nova_matriz[i][j]
            j += 1
        matriz+='\n'
        i += 1
    return matriz

def manipular_Grid(grid):
    nova_matriz = [[],[],[],[],[],[]]
    length = len(grid)
    length_linha = len(grid[0])

    i = 0
    while i < length_linha:
        j=0
        while j < length:
            nova_matriz[i].append(grid[j][i])
            j +=1
        i+=1


    return nova_matriz

print(printar_array_formatado())