
lista=[[1,2,3],[3,2,1],[2,3,1],[1,3,2],[3,1,2],[2,1,3]]

n=8

nin=2

listamem=[]
listcar=['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','z']
while nin!=n:
	nin+=1

	for i in range(len(lista)):
#		print lista
		car=nin+1
		if nin+1>9:
			
			car=listcar[nin-9]
		#	print car,nin
			lista[i].append(car)
		if nin+1<10:	
			lista[i].append(car)
	listamem=[]
	for i in range(len(lista)):

		for j in  range(nin,-1,-1):
			stringa=""

			mem=lista[i][j]
			lista[i][j]=lista[i][j-1]
			lista[i][j-1]=mem
			for k in range(len(lista[i])):
				stringa=str(stringa)+str(lista[i][k])
			listamem.append(stringa)
	
			
	lista=[]
	error=0

	for el in range(len(listamem)):
		lista.append([str(elx) for elx in listamem[el]])

#print (listamem)	
 
				
		
		



