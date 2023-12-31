fruits = ('apple', 'banana', 'orange', 'grape', 'kiwi')
fruits_copy = tuple(fruits)
print("Original Tuple:", fruits)
print("Copied Tuple:", fruits_copy)
new_fruit = 'pear'
fruits_copy = fruits_copy + (new_fruit,)
print("Updated Copied Tuple:", fruits_copy)