#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 13:10:15 2021

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
# print(monthly_salary)
# print(portion_down_payment)
# print(monthly_saving)

while current_savings <= portion_down_payment:
    months += 1
    interest = float(current_savings) * r/12
    current_savings += (monthly_saving + interest)

print("Number of Months", months)
    