k = input("Why you are applying for financial aid\n")
print("\n")
t = k.split()
if(len(t) >= 150):
  print(k)
else:
  print("The length of k should be more than 150")  
