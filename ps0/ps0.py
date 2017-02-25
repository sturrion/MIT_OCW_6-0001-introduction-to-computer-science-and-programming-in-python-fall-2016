#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 22:12:02 2017

@author: silvia
"""
import numpy

#Asks the user to enter a number “x”  
num_x = int(input("Enter number x: "))
#Asks the user to enter a number “y”
num_y = int(input("Enter number y: "))
#Prints out number “x”, raised to the power “y”. 
print("x**y= ", num_x ** num_y)
#Prints out the log (base 2) of “x”.
print("log(x) =", numpy.log2(num_x))
