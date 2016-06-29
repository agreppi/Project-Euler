from factors import factors
import time

def main():
    start = time.time()
    factores = set()
    orden = 1
    num_triang = 0
    while len(factores) < 500:
        num_triang = orden + num_triang
        factores = factors(num_triang)
        orden = orden + 1

    elapsed = (time.time() - start)
    print("%s found in %s seconds" % (num_triang,elapsed))

if __name__ == '__main__':
    main()