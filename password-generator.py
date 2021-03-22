#!/usr/bin/env python3

# random password generator

import random

size = input("Number of chars for new password? ")

def randompassword():
	chars = "23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ!@$_-+="
	#size = random.randint(8, 12)
	return ''.join(random.choice(chars) for x in range(int(size)))

# Printing output
print("\nNew passwords to choose from:")
print("=" * 29)
for i in range(1, 6):
	print(str(i) + ") " + randompassword())
