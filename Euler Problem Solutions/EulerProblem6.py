summed=25502500
total=0
n=100

while True:
    if n>0:
        total=total+(n*n)
        n=n-1 
        continue
    if n==0:
        break
print(total)
new = summed-total
print(new)
