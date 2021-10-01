#Starting from xp,yp positions finds the number of bounces in an elipse before to exit
#in -0.01<x<0.01  and y=0

'''
In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam. The beam enters the cell, bounces around on the mirrors, and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation 4x2 + y2 = 100

The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing the light to enter and exit through the hole.


The light beam in this problem starts at the point (0.0,10.1) just outside the white cell, and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual law of reflection "angle of incidence equals angle of reflection." That is, both the incident and reflected beams make the same angle with the normal line at the point of incidence.

In the figure on the left, the red line shows the first two points of contact between the laser beam and the wall of the white cell; the blue line shows the line tangent to the ellipse at the point of incidence of the first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is: m = −4x/y

The normal line is perpendicular to this tangent line at the point of incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before exiting?
'''
import math
import numpy
import matplotlib.pyplot as plt



xp=0
yp=10.1
puntix=[0]
puntiy=[10.1]
x0=1.4
y0=-9.6
#xnew=0
#ynew=0
puntix=[]
puntiy=[]

conta=0
xd=x0
yd=y0
t=0
tol=0.000001
conta=0
bounce=0

def disegna():
	plt.rc('xtick', labelsize=8)
	plt.rc('ytick', labelsize=8)
 
	# creazione canvas (le misure sono in pollici))
	plt.figure(figsize=(4, 8))
 
	# disegno grafico
	plt.plot(puntix, puntiy)
 
	# titolo grafico
	plt.title("test")
 
	# salvataggio su file
	plt.savefig("example.png")	
	plt.show()
	print xd
	print yd
	



 




def calcolo(x0,y0,xp,yp):
	global xnew
	global ynew
	uxperpend=-x0/(math.sqrt(x0**2+y0**2/16))
	uyperpend=-0.25*y0/math.sqrt((x0**2+y0**2/16))

	teta=math.pi


	uincx=(xp-x0)/math.sqrt((xp-x0)**2+(yp-y0)**2)
	uincy=(yp-y0)/math.sqrt((xp-x0)**2+(yp-y0)**2)
	matrixrot=[uxperpend**2+(1-uxperpend**2)*math.cos(teta), (1-math.cos(teta))*uxperpend*uyperpend,0],[(1-math.cos(teta))*uyperpend*uxperpend,uyperpend**2+(1-uyperpend**2)*math.cos(teta),0]
	xnew=matrixrot[0][0]*uincx+matrixrot[0][1]*uincy
	ynew=matrixrot[1][0]*uincx+matrixrot[1][1]*uincy
		 
 

while 1==1:
	calcolo(x0,y0,xp,yp)
 	conta+=1	
	if (conta%1==0):
		puntix.append(xd)
		puntiy.append(yd)
		#print "ok"	
	t=(-(8*xnew*x0+2*ynew*y0)+math.sqrt((8*xnew*x0+2*y0*ynew)**2-4*(4*xnew**2+ynew**2)*(4*x0**2-100+y0**2)))/(2*(4*xnew**2+ynew**2))
 	xd=x0+t*xnew
	yd=y0+ynew*t	

 	#if ((100-tol<=(4*xd**2+yd**2)<=100+tol)):
 	bounce+=1
 	xp=x0
	yp=y0
	x0=xd
	y0=yd
 		
 		
	if (-0.01<=xd<=0.01 and math.sqrt(100-4*xd**2)<=yd<=math.sqrt(100+4*xd**2)):
		disegna()
		print bounce
		break
		
					
 
