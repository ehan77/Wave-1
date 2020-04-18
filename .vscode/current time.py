# Inputs

import time

t = time.asctime()

a = t.split(' ')

print("The current time is: " , a[3] , "and the date is: " , a[1] , a[2] , "," , a[4])
