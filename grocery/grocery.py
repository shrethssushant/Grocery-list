grocery_list = []

try:
    while True:
        item = input().strip().title()
        grocery_list.append(item)
except EOFError:
    pass

#Counting the number of item in grocery list
count_dict = {}
for item in grocery_list:
    count_dict[item] = count_dict.get(item, 0) + 1

#Sort the product
sorted_items = sorted(count_dict.items(), key=lambda x: x[0])

# Print the grocery list
for item, count in sorted_items:
    print(f"{count} {item.upper()}")




