#K-Means algorithm with cost calculation
import numpy as np

#A=np.array([3,15,4,78,41,13,77,89,5,10])
A1=np.array([30,71,32,4,6,7,15,21,43,79])
k=2
m1new=15
m2new=43
for j in range(4):
	m1=m1new
	m2=m2new
	c1=[]
	c2=[]

	cost=0


	for i in range(10):
	
		if abs(A1[i]-m1)<=abs(A1[i]-m2):
			c1.append(A1[i])
			cost=cost+np.power(A1[i]-m1,2)
		if abs(A1[i]-m1)>abs(A1[i]-m2):
			c2.append(A1[i])
			cost=cost+np.power(A1[i]-m2,2)
	m1new=np.mean(c1)
	m2new=np.mean(c2)
	
cost=cost/10
print("After ", j+1 ,"th iteration  :" )
print("A1 :",A1)
print("C1 :",c1)
print("C2 :",c2)

print(m1, m1new)
print(m2, m2new)
print(cost)
		
	

	

