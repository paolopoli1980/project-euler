somma=0
for i in range(1000000):
	a=bin(i)
	a=a[2:]
	reversbin=int(str(a)[::-1])
	revers=int(str(i)[::-1])
	#1print revers
	#print reversbin
	
	if ((int(reversbin)==int(a)) and (int(revers)==i)):
		somma=somma+int(i)
		#print somma
	#print reversbin
	#print a[2:]	
print somma