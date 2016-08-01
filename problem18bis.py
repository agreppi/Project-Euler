import time
import pdb

def main():
    start = time.time()
    f = open('p018_triangle.txt', 'r')
    raw = f.readlines()
    triangle = []
    for linea in raw:
        triangle.append( [int(n) for n in linea[:-1].split(' ')] )
    f.close()
    fila = 0
    columna = 0

    suma = triangle[fila][columna]
    triangulo_de_sumas = [[suma]]
    print([suma])
    # for fila in range(1,len(triangle)):
    for fila in range(1,len(triangle)):
        lista_parcial = []
        lista_parcial.append(triangulo_de_sumas[fila-1][0]+triangle[fila][0])
        for columna in range(1,fila+1):
            lista_parcial.append(triangulo_de_sumas[fila-1][columna-1]+triangle[fila][columna])           
            
        triangulo_de_sumas.append(lista_parcial)    
        print(lista_parcial)

    suma = sorted(triangulo_de_sumas[-1])[-1]

    elapsed = (time.time() - start)
    print("%s found in %s seconds" % (suma,elapsed))


if __name__ == '__main__':
    main()
