#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:04:48 2021

@author: pmathieus
"""
# Background
# ​Please make your
# In Part A, we unrealistically assumed that your salary didn’t change. But you are an MIT graduate, and clearly you are going to be worth more to your company over time! So we are going to build on your solution to Part A by factoring in a raise every six months.
# In ​ps1b.py​, copy your solution to Part A (as we are going to reuse much of that machinery). Modify your program to include the following
# 1. Have the user input a semi-annual salary raise ​semi_annual_raise​ (as a decimal percentage) 2. After the 6t​h​ month, increase your salary by that percentage. Do the same after the 12t​h
# th​
# month, the 18​ month, and so on.
# Write a program to calculate how many months it will take you save up enough money for a down payment. LIke before, assume that your investments earn a return of ​r​ = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2
# 2. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
# 4. The semi­annual salary raise (semi_annual_raise)
# Hints
# To help you get started, here is a rough outline of the stages you should probably follow in writing your code:
# ● Retrieve user input.
# ● Initialize some state variables. You should decide what information you need. Be sure to be
# careful about values that represent annual amounts and those that represent monthly amounts.
# ● Be careful about when you increase your salary – this should only happen ​after​ the 6t​h,​ 12t​h​, 18t​h
# month, and so on.
# Test Case 1
# >>>
# Enter your starting annual salary:​ 120000
# Enter the percent of your salary to save, as a decimal:​ .05 
#Enter the cost of your dream home: ​500000
# Enter the semi­annual raise, as a decimal:​ .03
# Number of months:​ 142
# >>>
# Test Case 2
# >>>
# Enter your starting annual salary:​ 80000
# Enter the percent of your salary to save, as a decimal:​ .1 
#Enter the cost of your dream home: ​800000
# Enter the semi­annual raise, as a decimal:​ .03
# Number of months:​ 159
# >>>
# Test Case 3
# >>>
# Enter your starting annual salary:​ 75000
# Enter the percent of your salary to save, as a decimal:​ .05 
#Enter the cost of your dream home:​ 1500000
# Enter the semi­annual raise, as a decimal:​ .05
# Number of months:​ 261

annual_salary = input("Enter your annual salary? ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
total_cost = input("What is the cost of the house? ")
portion_down_payment = float(total_cost) * .25
current_savings = 0
monthly_salary = float(annual_salary)/12
monthly_saving = float(monthly_salary) * float(portion_saved)
months = 0
r = .04
semi_annual_raise = input("What is your semi annual raise? in decimal ")

# print(monthly_salary)
# print(portion_down_payment)
# print(monthly_saving)

while current_savings <= portion_down_payment:
    months += 1
    #every 6 months, it will increase salary and recalclate using new salary
    if months % 6 == 0:
        interest = float(current_savings) * r/12
        current_savings += (monthly_saving + interest)
        months +=1
        new_salary = float(annual_salary) + (float(annual_salary) * float(semi_annual_raise))
        annual_salary = new_salary
        new_monthly_salary = float(annual_salary)/12
        monthly_salary = new_monthly_salary
        new_monlthy_saving = float(monthly_salary) * float(portion_saved)
        monthly_saving = new_monlthy_saving
        interest = float(current_savings) * r/12
        current_savings += (monthly_saving + interest)
    else:
        interest = float(current_savings) * r/12
        current_savings += (monthly_saving + interest)

print("Number of Months", months)