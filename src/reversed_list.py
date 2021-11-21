"""
The goal from this algorithm is to reverse a list
"""

array = [2, 1, 43, 23, 8, 5] 

# You can do it like this

reversed_list = [array[-i] for i in range(1, len(array) + 1)]

# And also like that

reversed_list = list()
for i in range(1, len(array) + 1): 
    reversed_list.append(array[-i]) 

# Printing the result

print(reversed_list)

# Result -> [5, 8, 23, 43, 1, 2]