"""
The goal from this algorithm is to filter a list from duplicates
"""

array = [1, 2, 2, 3, 4, 4, 4] 

# You can do it like this

filtered_list = list()

for e in array:
    if e not in filtered_list:
        filtered_list.append(e)

# Printing the result
        
print(filtered_list)

# Result -> [1, 2, 3, 4]