from math import sqrt

def main():
    
    for b in range(2,1000):
        for a in range(1,b+1):
            c = sqrt (a**2 + b**2)
            if a+b+c == 1000:
                print(a,b,c, a*b*c)
                break


if __name__ == '__main__':
    main()