#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: May 25, 2022
# This program we generate random number (0-100)
# then we store them in a list and display the the largest
# number in the list. 

# import math random
import random

# function to find max value in the list
def find_max_value(list_of_number):
    
    # initialized
    max_num = -1
    # loop through the array to find max_num
    for counter in range (0, len(list_of_number), 1) : 
        if  list_of_number[counter] > max_num:
            max_num = list_of_number[counter]
    return max_num

def main():
    # list size variable
    max_size = 10
    # empty list
    list_of_number = []
     # loop to generate random number and append it to list

    for counter in range(0, max_size, 1):
        # set random number between 0-100
        random_number = random.randint(0, 100)
        list_of_number.append(random_number)
        print(random_number, "added to the list in position", counter)
    # calling the function
    max_value = find_max_value(list_of_number)
    print("The max number is ", max_value)


if __name__ == "__main__":
    main()
