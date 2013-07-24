# Prime Divisors
# Calculates the prime factors of a given natural number n
def prime_fac(n):
	primes = []
	prime_factors = []
	if n == 1:
		prime_factors = []
	if n == 2:
		prime_factors.append(2)
	else:
		for x in xrange(1,n):
			for y in xrange(2,x+1):
				if y != x and x % y == 0:
					break
				if y==x:
					primes.append(y)
		for p in primes:
			if n % p == 0:
				prime_factors.append(p)
	print primes
	print prime_factors
