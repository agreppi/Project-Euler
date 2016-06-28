def main():
    matrix = []
    f = open('problem11.txt', 'r')

    raw = f.readlines()

    matrix = []

    for linea in raw:
        matrix.append( [int(n) for n in linea[:-1].split(' ')] )

    f.close()

    resultados = []

    #import pdb
    #pdb.set_trace()


    # De izquierda a derecha, hacia abajo, es el triangulo superior
    prod_triangulo1 = 0
    for fila in range(17):
        for columna in range(fila,17):
            prod = matrix[fila][columna] * matrix[fila+1][columna+1] * matrix[fila+2][columna+2] * matrix[fila+3][columna+3]
            print('Fila: {}, columna: {}, {} * {} * {} * {} = {}'.format(fila, columna, matrix[fila][columna], matrix[fila+1][columna+1], matrix[fila+2][columna+2], matrix[fila+3][columna+3], prod))
            if prod > prod_triangulo1:
                prod_triangulo1 = prod

    # De izquierda a derecha, hacia abajo, es el triangulo inferior
    prod_triangulo2 = 0
    for fila in range(1,17):
        for columna in range(fila):
            prod = matrix[fila][columna] * matrix[fila+1][columna+1] * matrix[fila+2][columna+2] * matrix[fila+3][columna+3]
            print('Fila: {}, columna: {}, {} * {} * {} * {} = {}'.format(fila, columna, matrix[fila][columna], matrix[fila+1][columna+1], matrix[fila+2][columna+2], matrix[fila+3][columna+3], prod))
            if prod > prod_triangulo2:
                prod_triangulo2 = prod

    # De derecha a izquiera, hacia arriba, es el triangulo inferior
    prod_triangulo3 = 0
    for fila in range(19,2,-1):
        for columna in range(fila,2,-1):
            prod = matrix[fila][columna] * matrix[fila-1][columna-1] * matrix[fila-2][columna-2] * matrix[fila-3][columna-3]
            print('Fila: {}, columna: {}, {} * {} * {} * {} = {}'.format(fila, columna, matrix[fila][columna], matrix[fila-1][columna-1], matrix[fila-2][columna-2], matrix[fila-3][columna-3], prod))
            if prod > prod_triangulo3:
                prod_triangulo3 = prod

    # De derecha a izquierda, hacia arriba, es el triangulo superior
    prod_triangulo4 = 0
    for fila in range(18,2,-1):
        for columna in range(19,fila,-1):
            prod = matrix[fila][columna] * matrix[fila-1][columna-1] * matrix[fila-2][columna-2] * matrix[fila-3][columna-3]
            print('Fila: {}, columna: {}, {} * {} * {} * {} = {}'.format(fila, columna, matrix[fila][columna], matrix[fila-1][columna-1], matrix[fila-2][columna-2], matrix[fila-3][columna-3], prod))
            if prod > prod_triangulo4:
                prod_triangulo4 = prod

    prod_horizontal = max_prod_horizontal(matrix)
    prod_vertical = max_prod_vertical(matrix)

    resultados.append(prod_triangulo1)
    resultados.append(prod_triangulo2)
    resultados.append(prod_triangulo3)
    resultados.append(prod_triangulo4)
    resultados.append(prod_horizontal)
    resultados.append(prod_vertical)

    print(prod_triangulo1)
    print(prod_triangulo2)
    print(prod_triangulo3)
    print(prod_triangulo4)
    print(prod_horizontal)
    print(prod_vertical)    

    resultados.sort()
    
    print(resultados)


def max_prod_vertical(matrix):
    prod_vertical = 0
    for fila in range(17):
        for columna in range(20):
            prod = matrix[fila][columna] * matrix[fila+1][columna] * matrix[fila+2][columna] * matrix[fila+3][columna]
            print('Fila: {}, columna: {}, {} * {} * {} * {} = {}'.format(fila, columna, matrix[fila][columna], matrix[fila+1][columna], matrix[fila+2][columna], matrix[fila+3][columna], prod))
            if prod > prod_vertical:
                prod_vertical = prod 
    return prod_vertical

def max_prod_horizontal(matrix):
    prod_horizontal = 0
    for columna in range(17):
        for fila in range(20):
            prod = matrix[fila][columna] * matrix[fila][columna+1] * matrix[fila][columna+2] * matrix[fila][columna+3]
            print('Fila: {}, columna: {}, {} * {} * {} * {} = {}'.format(fila, columna, matrix[fila][columna], matrix[fila][columna+1], matrix[fila][columna+2], matrix[fila][columna+3], prod))            
            if prod > prod_horizontal:
                prod_horizontal = prod 
    return prod_horizontal



if __name__ == '__main__':
    main()
