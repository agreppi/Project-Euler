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
    # pdb.set_trace()
    for fila in range(1,len(triangle)):
        if triangle[fila][columna] > triangle[fila][columna+1]:
            sumando = triangle[fila][columna]
        else:
            sumando = triangle[fila][columna+1]
            columna += 1
        print(suma, sumando)
        suma = suma + sumando

    elapsed = (time.time() - start)
    print("%s found in %s seconds" % (suma,elapsed))


if __name__ == '__main__':
    main()
