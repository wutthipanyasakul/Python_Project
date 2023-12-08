

#Project 4: Magic 8-Ball 

#Instruction:
"""
    Write a magic8.py Python program that can answer any “Yes” or “No” question 
    with a different fortune each time it executes.

    Use:  the following 9 possible answers for our Magic 8-Ball:

        Yes - definitely
        It is decidedly so
        Without a doubt
        Reply hazy, try again
        Ask again later
        Better not tell you now
        My sources say no
        Outlook not so good
        Very doubtful

 """

#Project Starts
import random

#Task1: Generating a random number

#Step1: Ask for a person's name

name = input("What is your name? \n")


#Step2: Greet them
print("Hello, "+ name + "!")

#Step3: Ask them a yes/no question?

question = input("What do you want know?")

#Step4: Prepare for the answer container

answer =""

#Step5: Create a variable to store the random number from 1-12

random_number = random.randint(1,12)

#Task2: Control Flow

#Step6: Answer 1-12

#if a name is empty print only the question and the answer

if name =="": 
    #Task3: Seeing the result
    print(f"Question: {question}") 
    
    if random_number == 1 :
        answer = "Yes - definitely"
    elif random_number == 2:
        answer = "It is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    elif random_number == 10:
        answer = "You're better not to do it"
    elif random_number == 11:
        answer = "You will never do"
    elif random_number == 12:
        answer = "Sorry, you should stop diing now"
    else:
        answer = "Error"
        
    print("Wait ! Let me check. Your random number is: ", random_number)
    
    print(f"So the Magic 8-Ball's answer: {answer}")


 #if a question is empty, ask a user to ask the question first.
   
elif question =="": 
    #Task3: Seeing the result
    print(f"Hello, {name}.")
    print("Please ask any question to get a fortune!")

#if there are both name and question
else:
    if name and question:
        #Task3: Seeing the result
        print(f"{name} asks: {question}")
  
    if random_number == 1 :
        answer = "Yes - definitely"
    elif random_number == 2:
        answer = "It is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    elif random_number == 10:
        answer = "You're better not to do it"
    elif random_number == 11:
        answer = "You will never do"
    elif random_number == 12:
        answer = "Sorry, you should stop diing now"
    else:
        answer = "Error"
        
    print("Wait ! Let me check. Your random number is: ", random_number)

    print(f"So the Magic 8-Ball's answer: {answer}")
    
        




