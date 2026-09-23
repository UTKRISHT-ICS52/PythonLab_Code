# write a program to count the frequency of each element in list using dictionary
# list = [2,3,2,5,3,2,7,5,3]
list = [2,3,2,5,3,2,7,5,3]
frequency = {}
for item in list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
    print (frequency)
    
    
        