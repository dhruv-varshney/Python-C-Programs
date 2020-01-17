my_function = lambda a, b, c : (a/b)
m = int(input("enter the value of a"))
n = int(input("enter the value of b"))
p = int(input("enter the value of c"))
try:
    d = my_function(m,n,p)
    print(round (d))

except :
    print("invalid")
