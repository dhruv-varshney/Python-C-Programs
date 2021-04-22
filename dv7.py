
def power(exp,pow):
    
    
    if(pow==1):
       return exp
       
    else:
       
           ans = exp*power(exp,pow-1)
           return ans  
exp = int(input("enter a no."))
pow = int(input("enter a power "))            
a  = power(exp,pow) 
print("{} raise to {} is:{}".format(pow,exp,a))      
