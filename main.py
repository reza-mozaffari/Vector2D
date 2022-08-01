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

	V1 = V2
	print("V1 = ", V1)

	print("3.0*V1/2.0 = ", 3.0*V1/2.0)
