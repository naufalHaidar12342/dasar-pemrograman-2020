#calculate average acceleration from input given by user
import math
#dictionary
#t1, t2, v1, v2:real
#time measured in seconds
#velocity measured in m/s

v1=int(input(" type v1 : "))
v2=int(input(" type v2 : "))
t1=int(input(" type t1 : "))
t2=int(input(" type t2 : "))

acceleration=(v2-v1)/(t2-t1)
a=acceleration
print('a=',a,'m/s2')
