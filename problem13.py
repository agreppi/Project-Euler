import time
import pdb

def main():
    start = time.time()
    f = open('problem13.txt', 'r')
    raw = f.readlines()
    pdb.set_trace()
    lista = [int(n[:-1]) for n in raw]
    f.close()
    suma = sum(lista)


    elapsed = (time.time() - start)
    print("%s found in %s seconds" % (str(suma)[:10],elapsed))


if __name__ == '__main__':
    main()
