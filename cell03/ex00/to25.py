#!/usr/bin/env python
enter_number = int(input("Enter a number less than 25 : ").strip())
if enter_number > 25:
    print("Error")
else:
    while enter_number <= 25:
        print(f"Inside the loop, my variable is {int(enter_number)}")
        enter_number += 1



