# //    http://projecteuler.net/problem=1
# //    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# //    
# //    Find the sum of all the multiples of 3 or 5 below 1000.
numberList = [3,5]
limit = 1000
answer = 0
lcm = numberList[0] * numberList[1]

def sumMultiples(n):
	number = n
	numberOfTerms = limit/number
	lastNumInSequence = number*numberOfTerms
	if (lastNumInSequence>=limit):
		numberOfTerms-=1
		lastNumInSequence = number * numberOfTerms
	# result = numberOfTerms * (number + lastNumInSequence)/2
	return numberOfTerms * ((2*number)+(numberOfTerms-1)*number)/2

for i in numberList:
	answer += sumMultiples(i)

print answer - sumMultiples(lcm)
#233168