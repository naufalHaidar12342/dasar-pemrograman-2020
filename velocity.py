#calculate average velocity from input given by user
import math
#dictionary
#d1, d2, t1, t2:real
#distance measured in meter
#time measured in seconds
#velocity measured  in m/s

d1=int(input(" type d1 : "))
d2=int(input(" type d2 : "))
t1=int(input(" type t1 : "))
t2=int(input(" type t2 : "))

velocity=(d2-d1)/(t2-t1)
v=velocity
print('v=',v,'m/s') 