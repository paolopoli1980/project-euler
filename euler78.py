import math
p=[]
l=102
for k in range(l):
	p.append(0)

p[1]=1
p[2]=0
cont=0
pr=1
som=p[1]
for i in range(1,l):
	
	for k in range(int((1-(math.sqrt(1+24*i))/6-1)),int((1+(math.sqrt(1+24*i))/6)+1)):
		if ((i-k*(3*k-1)/2)>=0 and (i-k*(3*k-1)/2)<i and (k!=0)):
			#print k
			p[i]=p[i]+((-1)**(k-1))*p[int(i-k*(3*k-1)/2)]
                som=p[i]                 
		k-=1
	resto=p[i]%l
#	p[i]=p[i]%l
        if pr==1:
           print p[i]        

	if resto==0:
		print i
		print p[i]
   
		break
				


 