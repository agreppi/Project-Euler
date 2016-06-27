def main():
	result = 2
	f = 0
	f0 = 1
	f1 = 2
	while f0 + f1 < 4000000:
	    f = f0 + f1
	    if f % 2 == 0: result = result + f
	    f0 = f1
	    f1 = f
	print(result)
    
if __name__ == '__main__':
	main()