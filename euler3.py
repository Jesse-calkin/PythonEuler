# Project Euler problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?	

import math
numberToFactor = 600851475143
factors =[]

def factor(n):
	stack = []
	for i in range(2,int(math.ceil(math.sqrt(n)))):
		if (n%i==0):
			stack.append(i)
	return stack

for f in factor(numberToFactor):
	if not factor(f):
		factors.append(f)

print factors[-1]