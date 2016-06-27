from isPrime import is_prime

def main():
    
    suma = 0
    for b in range(2,10):
        if is_prime(b):
            suma += b

    print(suma)


if __name__ == '__main__':
    main()