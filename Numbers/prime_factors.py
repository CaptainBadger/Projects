# Prime Divisors
# Calculates the prime factors of a given natural number n
def prime_fac(n):
	primes = []
	prime_factors = []
	if n == 1:
		print prime_factors
	if n == 2:
		prime_factors.append[2]
		print prime_factors
	else:
		for x in xrange[1,n]:
			for y in xrange[1,x]:
				if y != 1 and y != x and x % y == 0:
					break
				if y=x:
					primes.append[x]
		for p in primes:
			if n % p == 0:
				prime_factors.append[p]
		print prime_factors