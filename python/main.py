print('hello world !')
print('hello world !')
#print('hello world !')

"""main
call
call
shift
"""
#string variable
name = 'Emeka'

#integer variable
age = 29

#float variable
grade = 4.45

#boolean variable
he_Is_Tall = True

#old string formatting
print(name + ' ' + ' is ' + str(age))

#New string formatting
print(f'{name} is {age} and his grade is {grade}')

#arithmetic operations
#nt and int
double_grade = grade*2
print(f'{name} grade multiplied by 2 is {double_grade}')

#int and string
print('s'* 10)

#comparison operator
A = 10
B = 15
C = 20
print(A == B)

#comparion for string
name_2 = 'emeka'
print(name.lower() == name_2.lower())

#comparison of logical operators
print(name == name_2 and A == B)
print( name.lower() == name_2.lower() or A == B) 

#code to calculate the average of three numbers
#declare the variables
x = 5
y = 10
z = 25

#calculate the average
average = (x + y + z) / 3

#printing the result
print(f'The average of the {x}, {y}, and {z} is {average}.')
