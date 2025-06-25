#!/usr/bin/env python
enter_number = int(input("Enter a number : ").strip())
multiply_number = 0
while multiply_number <= 9 :
    result = enter_number * multiply_number
    print(f"{multiply_number} x {enter_number} = {result}")
    multiply_number += 1

