lList = list(input("Enter first list: ").split(" "))
rList = list(input("Enter second list: ").split(" "))


sameList = set(lList) & set(rList)

print("General list: ", sameList)