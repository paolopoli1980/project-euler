from scipy.integrate import quad
import numpy as np

def integrand(teta,a,b,r):
	return np.sqrt((a**2*r**2*np.sin(2*teta)-b**2*r**2*np.sin(2*teta))**2/(4*(a**2*r**2*np.sin(teta)**2+b**2*r**2*np.cos(teta)**2))+a**2*r**2*np.sin(teta)**2+b**2*r**2*np.cos(teta)**2)

a=1
b=4
r=1
c=2*np.pi
d=0
I1= quad(integrand,d,c,args=(a,b,r))
a=3
b=4
I2= quad(integrand,d,c,args=(a,b,r))

print I1[0]
print I2[0]
print I1[0]+I2[0]

