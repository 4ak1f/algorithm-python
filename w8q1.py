print("To sort the elements of the list according to their length.")
lst = input("Enter elements separated by space: ").split()
lst.sort(key=len)
print(lst)
