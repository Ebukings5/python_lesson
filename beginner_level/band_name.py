#!/usr/bin/python3
# create a band generator
print("Welcome to my band name generator")
# Ask what city they grew up in
city = input("Which city did you grow up in?\n")
# Get pet name
pet = input("What is the name of your pet?\n")
# Use the f string and concatonate the variables
print(f"Your band name could be ", city + " " + pet)