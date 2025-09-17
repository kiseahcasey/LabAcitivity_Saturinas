my_list = input("Enter numbers separated by spaces: ").split()
my_list = list(map(int, my_list))   
my_list.sort()
print('Sorted list:', my_list)  # Output: [1, 3, 4, 5] (original list modified