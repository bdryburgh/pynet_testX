#!/usr/bin/env python

from __future__ import print_function

name1 = "Connor McDavid"
name2 = "Cam Talbot"
name3 = "Oscar Kelfbom"

try: 
    name4 = raw_input("Enter the Fourth Name: ")
except NameError:
    name4 = input("Enter fourth name: ")


print()
print("{:>30}".format(name1))
print("{:>30}".format(name2))
print("{:>30}".format(name3))
print("{:>30}".format(name4))
print()

