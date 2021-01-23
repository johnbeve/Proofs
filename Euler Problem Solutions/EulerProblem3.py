#The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?

#Greatest prime factor of any n is less than the square root of n. The square root of our target is 775147 (rounded up). 
	
def prime_factorization(n):
	list = []
	i = 2
	while i*i <=n:     #equivalent to i<=sqrt(n)
		while n%i == 0:
			list.append(i)
			n=n/i      #e.g. i=2 and n=6, then n=3
		i=i+1
	if n>1:            #catches 2 and 3 since they won't satisfy while condition
		list.append(n)
	return list


