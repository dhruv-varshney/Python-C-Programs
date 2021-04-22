val = int(input('enter the number: '))

x=0

y=0

for i in range(1,val+1):

     if(i%2!=0):

         x= x+7

     else:

         y = y+6

if(val%2!=0):

    print(' {} term in accordance to the program is {}'.format(val,x-7))

else:

    print('{} term in accordance to the program is {}'.format(val,y-6))
