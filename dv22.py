S1 = " " 
S2 = " " 
for I in range (6): 
  J = 1 
  while (J <= I): 
    if J + I % 2 == 0 or J + I % 3 == 0 : 
      S1 = S1 + '++' 
    else: 
      S2 = S1 + '**'
    J += 1
  print (S1) 
  print (S2) 
