import time
# import pdb

def main():
    start = time.time()
    eslabon_max = 0
    for i in range(1000000):
        n = i
        eslabon = 1
        while n > 1:
            eslabon += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3*n + 1
        if eslabon > eslabon_max:
            num_con_cadena_mas_larga = i
            eslabon_max = eslabon
            # print("El número %s es el que tiene más eslabones (%s)." % (num_con_cadena_mas_larga,eslabon_max))
        

    elapsed = (time.time() - start)
    print("El número %s es el que tiene más eslabones (%s). El proceso tardó %s" % (num_con_cadena_mas_larga,eslabon_max, elapsed))


if __name__ == '__main__':
    main()
