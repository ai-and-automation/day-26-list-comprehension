# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 26 - Intermediate - List Comprehension
# November 13, 2024

import random

# List comprehension:
# new_list = [new_item for n in numbers] # note: new_item should have same name as n

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(f"new_list = {new_list}")

# Same operation can be done with one line with list comprehension (works with lists, ranges, strings and tuples)
new_list2 = [n + 1 for n in numbers]
print(f"new_list2 = {new_list2}")

# This list comprehension converts a string into a list
name = "Eugene"
new_list3 = [letter for letter in name]
print(f"new_list3 = {new_list3}")

# Python sequences are list, range, string, tuple

# Challenge
range_list = [num * 2 for num in range(1, 5)]
print(f"range_list = {range_list}")

# Conditional list comprehension
# new_list = [new_item for item in list if test]
# Example
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(f"short_names = {short_names}")
# Challenge
long_names_cap = [name.upper() for name in names if len(name) > 5]
print(f"long_names_cap = {long_names_cap}")

# Exercise - Filtering Even Numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)

# Exercise - Data Overlap
# 💪 This exercise is HARD 💪
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# e.g. if file1.txt contained:
# 1
# 2
# 3
# and file2.txt contained:
# 2
# 3
# 4
# result = [2, 3]
#
# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop.
# new_list = [new_item for n in numbers]
# new_list = [new_item for n in numbers]
with open("file1.txt") as file1:
    numbers_list_1 = file1.readlines() # readlines() converts each line an item in a list
    numbers_list_1 = [int(line.strip()) for line in numbers_list_1] # .strip() used to remove \n
with open("file2.txt") as file2:
    numbers_list_2 = file2.readlines()
    numbers_list_2 = [int(line.strip()) for line in numbers_list_2]
# print(f"numbers_list_1: \n {numbers_list_1}") # test
# print(f"numbers_list_2: \n {numbers_list_2}") # test
# print(type(numbers_list_1[0])) # test
# new_list = [new_item for item in list if test]
result = [num1 for num1 in numbers_list_1 if num1 in numbers_list_2]
print(result)

# Dictionary Comprehension - new dictionary based on existing list or dictionary or range or tuple
# new_dict = {new_key:new_value for item in list} - new dictionary based on a list
# new_dict = {new_key:new_value for (key,value) in dict.items()} - new dictionary based on a dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items() if test} - new dictionary based on a dictionary with an if statement

# Example of creating a dictionary based on a list:
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print(f"students_scores = {students_scores}")
passed_students = {student:score for (student,score) in students_scores.items() if score >= 65}
print(f"passed_students = {passed_students}")
print(f"passed_students.items() = {passed_students.items()}") # .items() converts dictionary into tuples

# Dictionary Comprehension 1 - passed:
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.  *
# *Do NOT** Create a dictionary directly.
# Try to use Dictionary Comprehension instead of a Loop.
#
# To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.
print("Dictionary Comprehension 1")
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence.split()
print(f"words_list = {words_list}")
print(len(words_list[0])) # test
result = {word:len(word) for word in words_list}
print(f"result = {result}")

# Dictionary Comprehension 2 - passed
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula:
# (temp_c * 9/5) + 32 = temp_f
# Celsius to Fahrenheit chart
# **Do NOT** Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
print("Dictionary Comprehension 2")
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
weather_f = {day:(temp_c*9/5)+32 for (day,temp_c) in weather_c.items()}
print(f"weather_f = {weather_f}")
print("\n")

# How to Iterate over a Pandas DataFrame
print("Iterate over a Pandas DataFrame")
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)
print("\n")

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(f"student_data_frame: \n{student_data_frame}")

# Loop through data frame - not the best way to do this
for (key, value) in student_data_frame.items():
    print(key)
    print(value)
print("\n")

# Loop though rows of a data frame
print("Loop though rows of a data frame")
for (index, row) in student_data_frame.iterrows():
    print(row)
for (index, row) in student_data_frame.iterrows():
    print(row.student)
for (index, row) in student_data_frame.iterrows():
    print(row.score)

# Dictionary comprehension for pandas data frame:
# {new_key:new_value for (index, row) in df.iterrows()}