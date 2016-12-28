import math
f1=open("p099_base_exp.txt")
stringa="**"
lista=[]
while stringa!="":
	stringa=f1.readline()
	lista.append(stringa[0:len(stringa)-1])
fattore=1
listanumber=[]
listaespo=[]



for el in lista:
	number=""
	espo=''
	switch=0
	for elem in el:
		
		if elem!=',':
			if (switch==0):
				number=number+str(elem)
			if (switch==1):
				espo=espo+str(elem)

		if elem==',':
			switch=1;
						
	listanumber.append(number)
	listaespo.append(espo)
	
print listanumber[10]				
print listaespo[10]
max=0
val=0
linea=0
for i in range(len(listanumber)-1):
	#print float(listanumber[i])
	val=math.log(float(listanumber[i]))*float(listaespo[i])
	print val
	if val>max:
		max=val
		linea=i+1
	
print linea		