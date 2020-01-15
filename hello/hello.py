# import matplotlib.pyplot as plt
# import numpy as np
import random

# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot

# this is a comment line
# msg_long_long_varabile = "hello world!"
# print(msg_long_long_varabile)

# myname = "Alfred ...xxx"
# if myname == "Alfred":
#   print("Hi Alfred!")
# else:
#   print("You are not Alfred")

counter = 0

for mynum in [1, 2, 3, 4, 5]:
  # print("Hello", mynum)
  # print "Hello:", mynum
  # counter += 1
  counter = counter + 1

# print "*** count:", counter


mycount = 0

while (mycount < 100):
  # print ':', mycount
  mycount += 1

# print "*** mycount: ", mycount

# **********************************
# ******* I'm learning new stuff ***
# **********************************

# this is a function, simple 
def say_hello(name):
      print('Hi', name)

# say_hello("robin")


def plus(a, b):
  print(a+b)

# plus(1,1)

print(random.randint(1,100))





