# -*- coding: utf-8 -*-
"""
By: July Tatiana Ramírez Herrera
Challenge: Exponential function approximation

"""


"""
                    Part One of the Challenge:
    
Here we calculate exponential function WITHOUT using math.exp.

1. Build a program that given x and n would approximate e^x using the identity above.
That is only using sums, multiplications and divisions (exponentials are not allowed
by definition). You can use any programing language you like (it could be excel if
you want).

"""

import numpy as np
import matplotlib.pyplot as plt
import math
from decimal import Decimal

print("************* EXPONENTIAL FUNCTION APPROXIMATION CALCULATOR *************")
print("")
print("-------------------Part Two of the Challenge-------------------")
print("")

print("Please enter an N integer which will be the final index of summation")
n = input ("N = " )
print("")

print("Please enter a number for which you want to run the exponential summation e^{x} ")
x = input ("X = " )
print("")

n = int(n)
x = int(x)

sumatoria = 0.0

for n in range (0, n):
    factorial = math.factorial(n)
    potencia = x**n
    nth_term = float(potencia)/factorial
    sumatoria = sumatoria + nth_term

print("The result is approximately: ")
print (sumatoria)


"""
                    Part Two of the Challenge:
    
Here we calculate exponential function using math.exp only to compare with the summation result.

2. What should be the value of n in order to calculate up to 9 decimals?

Answer: It depends of the X value, so an N number of summation to calculate up to 9 decimals could be different for e^{2} and for e^{10}  

"""
print("")
print("")
print("-------------------Part Two of the Challenge-------------------")
print("")
x_Value = input ("Please write an X value for exponential function: " )
x_Value = float(x_Value)
e =(math.exp(x_Value))

e = float(round(e,9))

n_Value = 0
sumatoria_2 = 0

sumatoria_2 = 0.0

"""
Sigma summation with the x_Value given 
To find an approximation to e value up to 9 decimals 
And to find an N value to reach that approximation 
"""
while ( sumatoria_2 < e):
    factorial_2 = float(math.factorial(n_Value))
    potencia_2 = x_Value**n_Value
    potencia_2 = round(potencia_2, 9)
    n_term = float(potencia_2)/factorial_2
    n_term = round(n_term, 9)
    sumatoria_2 = sumatoria_2 + n_term
    sumatoria_2 = round(sumatoria_2, 9)
    n_Value += 1

sumatoria_2 = round(sumatoria_2, 9)

print("")
print("*** RESULTS OF PART-TWO ***")
print("")
print("What should be the value of n in order to calculate up to 9 decimals? ") 
print(n_Value)
print("")
print("The value of the summation up to 9 decimals is: ")
print(sumatoria_2)   
print("Given that value of e^{" + str(x_Value) + "} is equal to: ")
print(e)
print("")

