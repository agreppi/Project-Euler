import time
# import pdb

def main():
    start = time.time()
    one = 3
    two = 3
    three = 5
    four = 4
    five = 4
    six = 3
    seven = 5
    eight = 5
    nine = 4
    ten = 3
    eleven = 6
    twelve = 6
    thirteen = 8
    fourteen = 8
    fifteen = 7
    sixteen = 7
    seventeen = 9
    eighteen = 8
    nineteen = 8
    twenty = 6
    thirty = 6
    forty = 5
    fifty = 5
    sixty = 5
    seventy = 7
    eighty = 6
    ninety = 6
    hundred = 7
    nand = 3
    thousand = 8
    # pdb.set_trace()
    suma_de_1_a_9 = one + two + three + four + five + six + seven + eight + nine
    suma_de_1_a_19 = suma_de_1_a_9 + ten + eleven + twelve + thirteen + fourteen + fifteen + sixteen + seventeen + eighteen + nineteen
    suma_de_20_a_99 = 10 * (twenty + thirty + forty + fifty + sixty + seventy + eighty + ninety) + 8 * suma_de_1_a_9
    suma_de_1_a_99 = suma_de_1_a_19 + suma_de_20_a_99
    suma_de_100_a_999 = 100 * (suma_de_1_a_9) + 9 * (100 * hundred + 99 * nand) + 9 * suma_de_1_a_99
    suma = suma_de_1_a_99 + suma_de_100_a_999 + one + thousand

        

    elapsed = (time.time() - start)
    print("Cantidad de letras: %s. El proceso tardó %s" % (suma, elapsed))


if __name__ == '__main__':
    main()
