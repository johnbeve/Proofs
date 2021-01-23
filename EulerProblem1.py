#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, #5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
	
#n=1000
#total=0
#while n%3==0 or n%5==0:
#	total=total+n 
#	print(total)
#	n=n-1
	
n=1000
total=0
while True:
	if n%3==0 or n%5==0:
		total=total+n
		n=n-1
		continue
	if n>0:
		n=n-1
	if n==0:
		break
print(total-1000)
		


