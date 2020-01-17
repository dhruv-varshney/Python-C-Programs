import random
import re
import sys

num = random.randint(1,100)

if (not((num%2)==0) and num < 20):
   print("Weird")
elif((num%2)==0 and 2<=num<=5):
   print("Not Weird")
elif((num%2)==0 and 6<=num<=20):
   print("Weird")
elif((num%2)==0 and num>20 and num<=100):
   print("Not Weird")
print(num)
