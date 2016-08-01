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
    ultima_fila = triangle[len(triangle)-1]
    largo_ultima_fila = len(ultima_fila)
    max = 0
    for i in range(largo_ultima_fila):
        if ultima_fila[i] >= max:
            max = ultima_fila[i]
            indice_del_mayor = i
    suma = max

    for fila in range(len(triangle)-1, -1, -1):
        # pdb.set_trace()
        print(fila, indice_del_mayor)
        if indice_del_mayor == fila + 1:
            sumando = triangle[fila][indice_del_mayor - 1]
            indice_del_mayor = indice_del_mayor - 1
        elif triangle[fila][indice_del_mayor] > triangle[fila][indice_del_mayor-1]:
            sumando = triangle[fila][indice_del_mayor]
        else:
            sumando = triangle[fila][indice_del_mayor-1]
            indice_del_mayor = indice_del_mayor - 1
        print(suma, sumando)
        suma = suma + sumando
    print(fila)
    elapsed = (time.time() - start)
    print("%s found in %s seconds" % (suma,elapsed))


if __name__ == '__main__':
    main()
