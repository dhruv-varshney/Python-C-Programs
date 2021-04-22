m1 = {}
m2 = {}
m3 = {}
print("********ENTER INTERNAL1 MARKS OF VARIOUS SUBJECTS********") 
m1["me"] = int(input("enter the management internal1 marks"))
m1["cns"] = int(input("enter the cns internal1 marks"))
m1["atci"] = int(input("enter the atci internal1 marks"))
m1["dbms"] = int(input("enter the dbms internal1 marks"))
m1["unix"] = int(input("enter the unix internal1 marks"))
m1["python"] = int(input("enter the python internal1 marks"))
print("\n")
print("**********DISPLAY INTERNAL1 MARKS*********")
for keys,values in m1.items():
    print("{} = {}".format(keys,values))
print("\n")
t1 = sum(m1.values())
avg1 = t1/6
print("Total marks scored in internal1 is {} and the average is {}".format(t1,avg1))
print("\n")
print("********ENTER INTERNAL2 MARKS OF VARIOUS SUBJECTS********") 
m2["me"] = int(input("enter the management internal2 marks"))
m2["cns"] = int(input("enter the cns internal2 marks"))
m2["atci"] = int(input("enter the atci internal2 marks"))
m2["dbms"] = int(input("enter the dbms internal2 marks"))
m2["unix"] = int(input("enter the unix internal2 marks"))
m2["python"] = int(input("enter the python internal2 marks"))
print("\n")
print("**********DISPLAY INTERNAL2 MARKS*********")
for keys,values in m2.items():
    print("{} = {}".format(keys,values))
print("\n")
t2 = sum(m2.values())
avg2 = t2/6
print("Total marks scored in internal2 is {} and the average is {}".format(t2,avg2))
print("\n")
print("********ENTER INTERNAL3 MARKS OF VARIOUS SUBJECTS********") 
m3["me"] = int(input("enter the management internal3 marks"))
m3["cns"] = int(input("enter the cns internal3 marks"))
m3["atci"] = int(input("enter the atci internal3 marks"))
m3["dbms"] = int(input("enter the dbms internal3 marks"))
m3["unix"] = int(input("enter the unix internal3 marks"))
m3["python"] = int(input("enter the python internal3 marks"))
print("\n")
print("**********DISPLAY INTERNAL3 MARKS*********")
for keys,values in m3.items():
    print("{} = {}".format(keys,values))
print("\n")
t3 = sum(m3.values())
avg3 = t3/6
print("Total marks scored in internal3 is {} and the average is {}".format(t3,avg3))
print("\n")
total = {}
print("*******Final Marks to be put in report Card *******")
print("\n")
total["me"] = (m1["me"]+m2["me"]+m3["me"])/3
total["cns"] = (m1["cns"]+m2["cns"]+m3["cns"])/3
total["atci"] = (m1["atci"]+m2["atci"]+m3["atci"])/3
total["dbms"] = (m1["dbms"]+m2["dbms"]+m3["dbms"])/3
total["unix"] = (m1["unix"]+m2["unix"]+m3["unix"])/3
total["python"] = (m1["python"]+m2["python"]+m3["python"])/3
for keys,values in total.items():
    print("{} = {}".format(keys,values))
    

