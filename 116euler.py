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
		print binom(n,k)
		somma=somma+binom(n,k)
	cont2+=1
print somma