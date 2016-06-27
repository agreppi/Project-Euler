def main():
    sum_squares = 0
    suma = 0
    for i in range(1,101):
        sum_squares = sum_squares + i**2
        suma = suma + i

    square_sum = suma**2

    print(square_sum - sum_squares)


if __name__ == '__main__':
    main()