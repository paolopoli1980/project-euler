'''
A row of five grey square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

png116_1.png
If green tiles are chosen there are three ways.

png116_2.png
And if blue tiles are chosen there are two ways.

png116_3.png
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the grey tiles in a row measuring five units in length.

How many different ways can the grey tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?

'''
cont=0
cont2=0
number=50
somma=0

lista=[2,3,4]

def binom(n,k):
	fat1=1
	for i in range(1,n+1):
		fat1=fat1*i
	fat2=1
	for i in range(1,k+1):
		fat2=fat2*i
		
	fat3=1
	for i in range(1,(n-k)+1):
		fat3=fat3*i
	return fat1/(fat2*fat3)
for el in lista:
	cont=0
	while (number-cont*lista[cont2])>0:
		cont=cont+1
		n=number-lista[cont2]*cont+cont	
		k=cont
		print (binom(n,k))
		somma=somma+binom(n,k)
	cont2+=1
print (somma)
