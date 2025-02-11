num_list = list(map(int, input("Enter the numbers: ").split()))
unique_sorted_list = sorted(set(num_list))
print("Sorted Unique List:", unique_sorted_list)