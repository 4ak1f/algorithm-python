def merge_and_sort(list1, list2):
    # Merging the two lists
    merged_list = list1 + list2
    # Sorting the merged list
    merged_list.sort() 
    return merged_list

list1 = [int(x) for x in input("Enter elements of the first list separated by space: ").split()]
list2 = [int(x) for x in input("Enter elements of the second list separated by space: ").split()]

sorted_merged_list = merge_and_sort(list1, list2)

print("The merged and sorted list is:", sorted_merged_list)
