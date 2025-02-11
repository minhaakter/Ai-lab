list1 = set(map(int, input("Enter first list of numbers: ").split()))
list2 = set(map(int, input("Enter second list of numbers: ").split()))
common_elements = list1.intersection(list2)
print("Common Elements:", common_elements)