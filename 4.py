# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
pals =[]
for i in range (100,999):
	for j in range(100,999):
		num3 = i*j
		if (str(num3)==str(num3)[::-1]):
			pals.append(num3)
pals.sort()
print pals[-1]