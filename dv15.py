n = int(input("enter the value of n\n"))
if not(n%2)==0:
   print("Weird")
elif ((n%2)==0 and 2<=n<=5):
    print("Not Weird")
elif((n%2)==0 and 6<=n<=20):
    print("Weird")
