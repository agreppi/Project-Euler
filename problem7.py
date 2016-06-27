from isPrime import is_prime

def main():
    counter = 1
    for i in range(3,1000000,2):
        if is_prime(i):
            counter = counter + 1
            if counter == 10001:
                break
    print(i)


if __name__ == '__main__':
    main()