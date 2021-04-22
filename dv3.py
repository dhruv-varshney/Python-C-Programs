num = int(input("Enter the number:"))
for i in range(2, int(num / 2)):
    if num % i == 0:
        print("Not a Prime Number")
        break
else:
    print("It is a Prime Number")
