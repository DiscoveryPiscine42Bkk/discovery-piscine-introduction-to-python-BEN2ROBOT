#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    if sys.argv[1].islower() : 
        print("none")
    else : 
        print(sys.argv[1].lower())
else :
    print("none")