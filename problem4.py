from isPalindrome import isPalindrome


def main():
    result = 1
    for i in range(1000):
        for j in range(1000):
            multi = i*j
            if isPalindrome(multi) and multi > result:
                result = multi
    print(result)

if __name__ == '__main__':
    main()