def fib(n):    # write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

# fib(3)
# fib(n=3)

# python's fucked up function argument system https://docs.python.org/3/tutorial/controlflow.html#special-parameters

def variableArgs(*args):
	print(args)

# variableArgs(1)
# variableArgs(1, [2], { 'map': 'value' }, 'I am a cow')


def reverse(string):
	current = len(string) - 1
	reversed = ''
	while current >= 0:
		reversed += string[current]
		current -= 1

	return reversed

print(reverse('hello'))

