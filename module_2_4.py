numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
for number in numbers:
    is_prime = True
    if number == 1:
        continue
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')