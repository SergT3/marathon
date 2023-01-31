# if i know the number is from 0 to N Eratosphenes method would be good)
N = 1000
prime_numbers = []
for i in range(N):
    prime_numbers.append(i)
i = 2
while i * i < 1000:
    for j in prime_numbers:
        if j == i:
            continue
        if j % i == 0:
            prime_numbers.remove(j)
    i += 1


def is_prime(n):
    if n in prime_numbers:
        return True
    return False
