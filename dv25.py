import random
k= random.randint(100,1000)
m = random.randint(100,1000)
n = random.randint(100,1000)
while((k%5 != 0) and (m%5 != 0) and (n%5 != 0) and (k != m) and (k != n) and (m !=n)):
  k = random.randint(100,1000)
  m = random.randint(100,1000)
  n = random.randint(100,1000)
  
print("three random number are:" +str(k) + "," + str(m) + "," + str(n))  
  
