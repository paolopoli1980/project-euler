'''
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
'''

x=[]
y=[]
for i in range(2,100):
	for j in range(i,100):
		x.append([i,j])
		
t=-1
#x=[[3,4]]
somma=0
err=1000000000000
for i in range(len(x)):
	
	t=-1
	somma=0
	#print x[i][1]
	while t<x[i][0]:
		t+=1
		k=0
		while (k<x[i][1]):
			k+=1
			somma=(x[i][1]-k+1)*(x[i][0]-t)+somma
	
			#print somma
	#print somma
	if ((2000000-somma)>0 and err>(2000000-somma)):
		err=2000000-somma
		print (x[i]) 	
