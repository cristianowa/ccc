#Example file to use reflection in python.
#The inspect module helps in analysing classes methods
#using class.__dict__ make possible to add functions in each class struct
#the functions can be simple functions or methods bounded to other class instances
#bounding the a function to the current instance is still a TODO
import inspect
try :
#termcolor is avaibable at http://pypi.python.org/pypi/termcolor
	from termcolor import colored, cprint
except:
	def cprint(string,notused) :
		print(string)

class imported :
	def foo(self):
		print("foo")
	def foo2(self):
		print("foo2")
	def foo3(self):
		print("foo3")
class importer :
	def importClass(self,imported):
		#for i in imported
		name = imported.__class__.__name__
		self.__dict__[name] = {}
		membs = inspect.getmembers(imported)
		for m in membs :
			if(m[0].find("__") < 0):
				#this is not a hidden/private member
				self.__dict__[name][m[0]] = m[1]
def rprint(msg):
	cprint(msg,"red")


def run() :
	cprint("""
Example file to use reflection in python.
The inspect module helps in analysing classes methods
using class.__dict__ make possible to add functions in each class struct
the functions can be simple functions or methods bounded to other class instances
bounding the a function to the current instance is still a TODO""","blue")

	rprint("cl = imported()")
	cl = imported()
	rprint("im = importer()")
	im = importer()
	rprint("inspect.getmembers(cl)")
	print(inspect.getmembers(cl))
	rprint("inspect.getmembers(im)")
	print(inspect.getmembers(im))
	rprint("im.importClass(cl))")
	im.importClass(cl)
	rprint("inspect.getmembers(im)")
	print(inspect.getmembers(im))
	return cl,im
