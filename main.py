"""
	main.py
	
	M. Reza Mozaffari
	Physics Group, University of Qom
"""

from Vector2D import *

if __name__ == "__main__":

	V1 = Vector2D()
	print("V1 = ", V1)

	V2 = Vector2D(1.0, 2.0)
	print("V2 = ", V2)

	V3 = Vector2D(2.0, 1.0)
	print("V3 = ", V3)
	
	V1 = V2
	print("V1 = ", V1)
	
	print("V2 + V3 = ", V2 + V3)
	
	print("V2 - V3 = ", V2 - V3)
	
	print("3.0*V1/2.0 = ", 3.0*V1/2.0)
	
	print("|V2| = ", abs(V2)) 
	print("|V2| = ", length(V2)) 
	
	print("hat{V2} = ", V2.hat()) 
	print("hat{V2} = ", hat(V2))  
	
	print("V2 . V3 = ", V2.dot(V3))
	print("V2 . V3 = ", dot(V2, V3))
	
	print("V2 x V3 = ", V2.cross(V3))
	print("V2 x V3 = ", cross(V2, V3))
