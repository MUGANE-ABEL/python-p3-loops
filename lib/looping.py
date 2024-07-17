#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i > 0:
        print (i)
        i -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    # code goes here!
    squared= []
    for interg in int_list:
        square= interg ** 2
        squared.append(square)
    return squared

def fizzbuzz():
    # code goes here!
    num = 1
    while num <= 100:
        if num%3 == 0 and num%5 == 0:
            print("FizzBuzz")
        elif num%3 == 0:
            print("Fizz")
        elif num%5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1
