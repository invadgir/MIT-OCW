#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:04:48 2021

@author: pmathieus
"""

annual_salary = input("Enter your annual salary? ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
total_cost = input("What is the cost of the house? ")
portion_down_payment = float(total_cost) * .25
current_savings = 0
monthly_salary = float(annual_salary)/12
monthly_saving = float(monthly_salary) * float(portion_saved)
months = 0
r = .04
semi_annual_raise = input("What is your semi annual raise? in decimal")

# print(monthly_salary)
# print(portion_down_payment)
# print(monthly_saving)

while current_savings <= portion_down_payment:
    months += 1
    if months/6 == INT():
        raise = annual_salary += (annual_salary * semi_annual_raise)
        print(raise)
    #     interest = float(current_savings) * r/12
    #     current_savings += (monthly_saving + interest)
    # interest = float(current_savings) * r/12
    # current_savings += (monthly_saving + interest)

print("Number of Months", months)