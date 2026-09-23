# Write a program to remove duplicates elements from a list without changing it's order 
# list = [10,20,10,30,20,40,30,50]
list = [10,20,10,30,20,40,30,50]
unique_list = []
for item in list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

