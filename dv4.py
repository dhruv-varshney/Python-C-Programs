store1=[1,2,3,4,5]
store2=[6,1,8,9,1]
cheapest = map(min,store1,store2)
highest = map(max,store1,store2)
print(cheapest)
print(highest)
for item in cheapest:
    print(item)
print("")
for item in highest:
    print(item)
