#Euler Problem 15


def path(n,m):
	if n == 0:
		return 1
	elif m == 0:
		return 1
	else: 
		return path(n-1,m) + path(n,m-1)

		
def path_cache(f):
	cache = {}
	def memoized(n,m):
		if (n,m) not in cache:
			cache[(n,m)] = f(n,m)
		return cache[(n,m)]
	return memoized

path = path_cache(path)
		
