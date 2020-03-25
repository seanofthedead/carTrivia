# Name: Sean R. Bedolla
# SSID: 1702054
# Assignment #: 2
# Submission Date: 3/21/2020
#
# Description of program:
# This is a trivia game about cars
#
print('*************************************************')
print('Welcome to the Car Trivia Quiz..')
print('Win by answering all three questions correctly')
print('*************************************************')
score = 0
ans = 'answer1','answer2','answer3'

    # QUESTION ONE
answer1 = input('Q1. Who designed what was considered the worlds first car? \n1. Henry Ford \n2. Ferdinand Porsche \n3. Karl Benz \n4. Louie Chevrolet \nEnter your answer (1,2,3, or 4): ')
if answer1 == '3' or answer1 == 'Karl Benz':
    score += 1
    print("You've done your homework! That is correct.")
    print('\n')
else:
    print('Incorrect!')
    print('\n')


    # QUESTION TWO
answer2 = input('Q2. What famous automaker is responsible for designing the volkswagen beetle? \n1. Mercedes Benz \n2. Porsche \n3. Volkswagen \n4. Bavarian Motor Works \nEnter your answer (1,2,3, or 4): ')
if answer2 == '2' or answer2 == 'Porsche':
    score += 1
    print("Great work! That is correct.")
    print('\n')
else:
    print('Incorrect!')
    print('\n')


    # QUESTION THREE
answer3 = input('Q3. Which car is considered to be the first "muscle car"? \n1. 1963 Buick Riviera \n2. 1964 Pontiac GTO \n3. 1964 Mustang \n4. 1962 Impala \nEnter your answer (1,2,3, or 4): ')
if answer3 == '1' or answer3 == '1963 Buick Riviera':
    score += 1
    print("Impressive! That is correct.")
    print('\n')
else:
    print('Incorrect!')
    print('\n')


    #IF YOU GET THEM WRONG
if score == 0:
    print('You answered 0 out of 3 questions incorrectly')   

elif score == 1:
    print('You answered 2 out of 3 questions incorrectly')
           
elif score == 2:
    print('You Answered 1 out of 3 questions incorrectly')
    
elif score == 3:
    print('Great! You answered all the questions correctly')
    print('Thank you for playing. Goodbye')

