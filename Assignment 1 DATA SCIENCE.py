#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# In[3]:


import sys


# In[4]:


print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[5]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[6]:



from math import pi
 

r = float(input ("Input the radius of the circle : "))
 

calculateArea = str(pi * r**2);
 

print ("The area of the circle with radius " + str(r) + " is: " + calculateArea)


# In[7]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[8]:



num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

sum = float(num1) + float(num2)


print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[ ]:




