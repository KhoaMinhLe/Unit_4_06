# Created by: Khoa Le
# Created on November 10 2017
# Created for ICS3U
# This program .

import ui

def check_strings(string_one, string_two):
# Checks if user strings are the same.
    
    string_one = string_input_one.upper()
    string_two = string_input_two.upper()
    
    if string_one == string_two:
        return True
    else:
        return False

string_input_one = raw_input("Enter string one:    ")
string_input_two = raw_input("Enter string two:    ")

answer = check_strings(string_input_one, string_input_two)

print answer
