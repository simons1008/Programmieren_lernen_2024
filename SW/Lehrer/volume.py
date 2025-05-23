## volume.py  volume calculations
## https://cs.uky.edu/~keen/help/debug-tutorial/volume.py
# Author:
# Date:
# There are libraries of common functions, for example a math library
# that has functions such as sine, cosine, logs, etc.
# There ARE syntax and semantic errors in this program as given!
from math import pi   # use the value of pi defined in the math library
def main():
      radius = input("Enter the radius: ")
      height = input("Enter the height: ")
      conevol = 1/3*pi*radius**2*height   # cone volume
      cylvol = pi*radius**2*height        # cylinder volume
      spherevol = 4/3*Pi*r**3        # sphere volume
      print ('The volume of a cone: ',conevol)
      print ("The volume of a cylinder: ",cylvol)
      print ("The volume of a sphere: ",spherevol)

main()
