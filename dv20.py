def sum_divisors(n):
  k = 1
  sum = 0
  if(n == 0):
    return 0
  while(k <= n):
    if (n%k == 0):
      sum = sum +k
    k = k+1
  return(sum) 
  
print(sum_divisors(36))    
    
