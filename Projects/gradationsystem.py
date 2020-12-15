import math
import os
import sys


def gradingstudent(grade):
    for i in grade:
        if i < 38:
            print(i)
        elif i % 5 < 3:
            print(i)
        else:
            print(i+(5-(i % 5)))


# main

grades_count = int(input())
grade = []

for _ in range(grades_count):
    grades_item = int(input())
    grade.append(grades_item)
print(grade)
result = gradingstudent(grade)
print(result)
