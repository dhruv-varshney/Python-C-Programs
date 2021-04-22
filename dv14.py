import os
t = 0
for filename in os.listdir('/home/dhruv/Desktop'):
     t = t + os.path.getsize(os.path.join('/home/dhruv/Desktop',filename))
print(t)
