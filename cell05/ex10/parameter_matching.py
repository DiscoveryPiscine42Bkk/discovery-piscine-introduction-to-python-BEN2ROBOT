#!/usr/bin/env python3
import sys
if len(sys.argv) != 2 :
    print ("none")
matching = sys.argv[1]
user_in = input("What was the parameter?")
if user_in == matching :
    print ("Good job!")
else :
    print ("Nope, sorry...")

