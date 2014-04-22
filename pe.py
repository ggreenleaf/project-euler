def one(n):
	total = 0
	for i in range(0,n):
		if i%3==0 or i%5==0:
			total+=i
	return total

#fib memoization for prob2
def fib_memory(n,dic):
	if n < 3:
		return 1
	else: 
		if dic.has_key(n-1) and dic.has_key(n-2):
			return dic[n-1] + dic[n-2]
		else:
			dic[n] = fib_memory(n-1,dic) + fib_memory(n-2,dic)
			return fib_memory(n-1,dic) + fib_memory(n-2,dic)

def two():
	fib_terms = {}
	fib_memory(100,fib_terms)
	sum = 0
	for term in fib_terms:
		if fib_terms[term] > 4000000:
			return sum
		if not fib_terms[term]%2:
			sum += fib_terms[term]


	