"""
	Vector2D.py
	
	M. Reza Mozaffari
	Physics Group, University of Qom
"""

from math import *

class Vector2D ():
	def __init__ (self, x=0.0, y=0.0):
		self.x = float(x)
		self.y = float(y)
	
	def __str__ (self):
		return "({:.8f}, {:.8f})".format(self.x, self.y)
			
	def __add__ (self, other):
		return Vector2D (self.x + other.x, self.y + other.y)
		
	def __sub__ (self, other):
		return Vector2D (self.x - other.x, self.y - other.y)	
	
	def __mul__ (self, scalar):
		return 	Vector2D (self.x*scalar, self.y*scalar)
	
	def __rmul__ (self, scalar):
		return 	self.__mul__(scalar)
	
	def __div__ (self, scalar):
		return Vector2D (self.x/float(scalar), self.y/float(scalar))
	
	def __truediv__ (self, scalar):
		return self.__div__(scalar)
				
	def __abs__ (self):
		return sqrt(self.x**2 + self.y**2)	

	def dot (self, other):
		return self.x*other.x + self.y*other.y

	def cross (self, other):
		return self.x*other.y - self.y*other.x

	def hat (self):
		r = self.__abs__()
		return Vector2D (self.x/r, self.y/r)

def dot (Vec1, Vec2):
	return Vec1.dot(Vec2)

def length (Vec):
	return sqrt(Vec.dot(Vec))
	
def cross (Vec1, Vec2):
	return Vec1.cross(Vec2)

def hat (Vec):
	return Vec.hat()
