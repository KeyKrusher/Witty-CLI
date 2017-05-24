# Code written by Jack Clark
# Copyright 2017(c) the M.I.T. License
# This code handles all of the Screen FX
import os
import sys

def clear_screen(user_os):
	if user_os == "Windows":
		os.system("cls")
	elif user_os == "MacOS":
		os.system("clear")
	elif user_os == "Linux":
		os.system("clear")
	else:
		print "Unkown Operating System."