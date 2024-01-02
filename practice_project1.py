# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:59:11 2024

@author: satha
"""
# Build out TripPlanner V1.0


def trip_planner_welcome(name):
    print("Welcome to tripplanner v1.0 " + name)


trip_planner_welcome("John")

def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time

estimate = estimated_time_rounded(3.6)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print("Your trip starts off in " +  origin)
    print("And you are traveling to " + destination)
    print("You will be traveling by " + mode_of_transport)
    print("It will take approximately " + str(estimated_time) + " hours")
    
destination_setup("Bangkok", "Khonkhaen", estimate)