#simple div

str_command = input("Что вы хотите посчитать?")
str_command.replace(' ', '')

hp_ops = tuple('^')
mp_ops = tuple('*/')
lp_ops = ('+', '-')
supported_ops = hp_ops + mp_ops + lp_ops
digits_chars = tuple(map(str, range(10))) + tuple('.,-')

sign_A = '' 
sign_B = ''

str_A = ''
str_B = ''
variables = ['']
operations = []

for i, letter in enumerate(str_command):
	if letter in '+-*/^' and (i>0) and variables[len(operations)] != '':
		operations.append(letter)
		variables.append('')
	else:
		index = len(operations)
		variables[index] = variables[index] + letter

variables = list(map(float, variables))
result = variables[0]

for i, operation in enumerate(operations):
	if type(result) == str:
		break

	var_A = result
	var_B = variables[i + 1]

	if operation in '+-*/':
		if var_B == 0 and operation == '':
			result = 'Inf'
		else:
			result = eval('{0}{1}{2}'.format(var_A, operation, var_B))
	elif operation == '^':
		result = var_A**var_B
	else:
		result = unknown

print("Result:"  + str(result))