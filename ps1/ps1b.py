#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:37:26 2017

@author: sturrion
"""

annual_salary = int(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
monthly_saved = (annual_salary / 12.0) * portion_saved

total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25

semi_annual_rise = float(input("Enter the semi-annual raise, as a decimal: "))

current_savings = 0.0
annual_return = 0.04
months = 0

while current_savings < portion_down_payment:
    months += 1
    monthly_return = current_savings * (annual_return / 12)
    current_savings += monthly_return + monthly_saved
        
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_rise
        monthly_saved = (annual_salary / 12.0) * portion_saved

print("Number of months:", months)
