#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [x for x in original_array if x >= 5]
add_new_array = [x + 2 for x in new_array]
print (original_array)
print (add_new_array)
