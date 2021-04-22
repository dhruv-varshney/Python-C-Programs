n = int(input("enter a no."))
tot = 0
if(n==0):
   tot =0
while(n>0):
   dig = n%10
   tot =tot+dig
   n= n//10
print("the sum of a digits of a no. is"+str(tot))      
