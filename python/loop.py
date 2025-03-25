#for and while loop practice
"""for i in range(10):
    print('Emeka')"""
    
#creating a list and adding items into the list using for loop
fruits = ['mango', 'apple', 'pineapple','tangerine', 'pawpaw']
"""for i in fruits:
    print(i)
"""
#break and paas in for loop
"""for i in fruits:
    if i == 'pineapple':
        break
    else:
        print(i)
        continue""" 
        

"""for i in fruits:
    if i == 'pineapple':
        pass
    else:
        print(i)
        continue  """

#using for loop to check number of people travelling and print their names     
"""Num_person = int(input('How many people are travelling? '))
passengers = []
for i in range(Num_person):
    Name = str(input('Enter the name/names: '))
    passengers.append(Name)
print(f'the {len(passengers)} passengers are: ')
for passenger in passengers:
    print(passenger)"""
    
"""Num_courses = int(input('How many courses are you offering as a freshman? '))
courses = []
for i in range(Num_courses):
    Crscode = str(input('Enter the course codes: '))
    courses.append(Crscode)
print(f'The {len(courses)} courses we are offering are:')
for course in courses:
    print(course) """
    

#while loop
"""action = ''
while action != 'quit':
    action = input('Enter the action: ')
    print(action)
else:
    print('goodbye')"""


#Create an empty list of fruits using a while loop ask for a fruit to add in the list, while the input
# is not equal to the list let it be adding fruit to the list esle let it stop
"""Name_fruit = input('Enter the names of Fruit you know: ')
fruit = []
while Name_fruit != 'watermelon':
    Name_fruit = input('Enter the names of Fruit you know: ')    
    fruit.append(Name_fruit)
else:
    print('Thank you goodbye')
print(f'the list containing names of Fruits are: {fruit}')
"""

"""numbers = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for num in numbers:
    sum = sum + num
print(sum)
average = sum / len(numbers)
print(f'The sum of the numbers is {sum}, and the average is: {average}')"""

"""Name_fruit = ''
fruit = []
while Name_fruit != 'watermelon':
    Name_fruit = input('Enter the names of Fruit you know: ').lower()    
    fruit.append(Name_fruit)
else:
    print('Thank you goodbye')
print(f'the list containing names of Fruits are: {fruit}')"""

#ask how many courses they are doing, ask the scores for each course, then calculate the average of the courses
# and print the results.

courses = None
Score_courses = []
Num_Courses = int(input('How many courses are you offering? '))
while len(Score_courses) != Num_Courses:
    courses = int(input('Enter your scores: '))
    Score_courses.append(courses)
else:
    print('Thank you that is all your score')
sum = 0
for num in Score_courses:
    sum = sum + num
average = sum / len(Score_courses)
print(f'The students average score is {average}')
if average >= 70:
    print('The students grade is A')
elif average >= 55 and average < 70:
    print('The students grade is B')
elif average >= 40 and average < 55:
    print('The students grade is C')
else:
    print('The students grade is F')
    
    

    