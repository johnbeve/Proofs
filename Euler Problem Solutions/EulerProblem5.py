#Euler Problem 5

def lcm(n,m):
	x = n 
	for x in range(n,n*m +1):
		if x%n==0 and x%m==0:
			return x 
			
def gcd(n,m):
	x = lcm(n,m)
	y = n*m 
	return y/x 

def check_prime(n):
	if n == 2:
		return n 
	i = 2
	for x in range(i,n):
		if n%x == 0:
			break
		else:
			x = x+1
		return n 	

def prime_list(n):
	list = []
	for x in range(1,n+1):
		if check_prime(x) > 0:
			list.append(x)
			x=x+1
		else:
			x=x+1
	return list
			
def prime_factorization(n):
	list = []
	i = 2
	while i*i <=n:
		while n%i == 0:
			list.append(i)
			n=n/i
		i=i+1
	if n>1:
		list.append(n)
	return list
		
def efficient_lcm(n,m):
	n_list = prime_factorization(n)
	m_list = prime_factorization(m)
	set_n = set(n_list)
	set_m = set(m_list)
	set_o = set_m - set_n 
	nm_list = n_list + list(set_o)
	total = 1
	for x in range(0,len(nm_list)):
		total = total*nm_list[x]
	print total
	

