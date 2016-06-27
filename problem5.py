def main():
    result = 21
    meeting = 1
    while meeting:
        result = result + 1
        meeting = result % 20 or result % 19 or result % 18 or result % 17 or result % 16 or result % 15 or result % 14 or result % 13 or result % 12 or result % 11
    print(result)

if __name__ == '__main__':
    main()