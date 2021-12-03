class ClassName(object):
	"""docstring for ClassName"""
	# Constructor
	def __init__(self):
		print("This is Program for Overloading in python")
	def show(self,a=None,b=None,c=None):
		if a!=None and b!=None and c!=None:
			s=a+b+c
		elif a!=None and b!=None:
			s=a+b
		elif a!=None:
			s=a
		else:
			s= "You don't Enter any number please enter"
		return s
#Craeet the class object
obj = ClassName()
# Called by one arguments 
obj.show(12)
# Called by two arguments
obj.show(12,13)
# Called by three arguments
obj.show(12,13,15)

# By making is this Abrar
		
		