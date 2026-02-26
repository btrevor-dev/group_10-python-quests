#!/usr/bin/python3

def personalized_greeting(name, quest):
    print(f"Greetings, {name}! Your quest to '{quest}' awaits!")

user_name = input("Enter your name: ")
user_quest = input("Enter your quest: ")

personalized_greeting(user_name, user_quest)
