try:
   my_list =[]
   while True:
        my_list.append(float(input()))
        
except:
        
    k = my_list
    print() 
for x in k:
    if (x < 0):
       print("invalid")
       exit(0)

k.remove(max(k))
m = max(k)
k.remove(max(k))
n = max(k)
k.remove(max(k))
p = max(k)
t =[m,n,p]
print(t)       
          
       
