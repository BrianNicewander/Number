# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:51:39 2020

@author: Brian
"""

def main():
    total = 0.0
    avg = 0.0
    lowestNumber = 0.0
    highestNumber = 0.0
    numbersPicked = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 
               '12', '13', '14', '15', '16', '17', '18', '19', '20']
    
    
    for index in range(0,20):
        print("Please put in a number in spot", numbers[index])
        numbersPicked[index] = float(input("Please put in a number "))
        lowestNumber = min(numbersPicked)
        highestNumber = max(numbersPicked)
        total += numbersPicked[index]
        avg = total /20
    
    print("Your lowest number is", format(lowestNumber, '.2f'))
    print("Your highest number is", format(highestNumber, '.2f'))
    print("The total for all your numbers is", format(total, '.2f'))
    print("The average for all your numbers is", format(avg, '.2f'))
        
main()