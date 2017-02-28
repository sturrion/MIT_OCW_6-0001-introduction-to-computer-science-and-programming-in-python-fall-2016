#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:13:40 2017

@author: sturrion
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
monthly_saved = (annual_salary / 12.0) * portion_saved

total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25

current_savings = 0.0
annual_return = 0.04
months = 0

while current_savings < portion_down_payment:
    months += 1
    monthly_return = current_savings * (annual_return / 12)
    current_savings += monthly_return + monthly_saved

print("Number of months:", months)
