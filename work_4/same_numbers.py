def genPrime(maxNum):
    for num in range(2, maxNum + 1):
        prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)

m = int(input("enter max num"))
genPrime(m)