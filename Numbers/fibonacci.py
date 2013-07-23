# Fibonacci Sequence
# Function returns the Fibonacci sequence to the nth degree, where n is given
def fibbo(n):
	a = 1
	b = 1
	i = 3
	fibbo = [1, 1]
	while i <= n:
		c = a + b
		fibbo.append(c)
		a, b = b, c
		i += 1
	
	print fibbo
