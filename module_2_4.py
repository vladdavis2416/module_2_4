numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_prime=[]
is_prime = True
for i in numbers:
    for j in range(2,i):
        if i % j == 0:
            is_prime = True
            break
        else:
            is_prime = False
    if is_prime == True:
        primes.append(i)
    else:
        not_prime.append(i)
    if i == 1:
        not_prime.append(i)
        primes.remove(i)



print(primes)
print(not_prime)

