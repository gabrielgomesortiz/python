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

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def manipular_Grid(grid):
    coordenadas = []
    length = len(grid)
    length_linha = len(grid[0])

    i = 0
    while i < length_linha:
        j=0
        while j < length:
            coordenadas.append(grid[j][i])
            j +=1
        i+=1


    return coordenadas

print(manipular_Grid(grid))