import math

lista=[2,3,4]
solution=[]

def diophantine_solutions(n):
	for i in range(n+1):
		for j in range(n+1):
			for k in range(n+1):
				if lista[0]*i+lista[1]*j+lista[2]*k<=n:
					solution.append([i,j,k])
					

n=5
diophantine_solutions(n)
del solution[0]
listnew=[]
print solution


def comb_calc():
	som=0
	c1=0
	c2=0
	c3=0
	c0=0
	print listnew
	som=0
	listsom=[]
	for j in listnew:
		c1=0
		c2=0
		c3=0
		c0=0

		for i in j:
			if i=='1':
				c0+=1
			if i=='2':
				c1+=1
			if i=='3':
				c2+=1
			if i=='4':
				c3+=1
			x=1
			#print j
			x=math.factorial(len(j))
			som=x/(math.factorial(c1)*math.factorial(c2)*math.factorial(c3)*math.factorial(c0))
		listsom.append(som)
	
		
		print som
	som=0
	
	for el in listsom:
		som=som+el
	print som+1
						

	#print som+1

			
		
		
		
		
	
for el in solution:
	stringa=""
	t=n
	for i in range(el[0]):
		stringa+=str(lista[0])
		t=t-lista[0]
	for i in range(el[1]):
		stringa+=str(lista[1])
		t=t-lista[1]
	for i in range(el[2]):
		stringa+=str(lista[2])
		t=t-lista[2]			
	print stringa
	for i in range(t):
		stringa+=str('1')
	listnew.append(stringa)
print listnew
comb_calc()


