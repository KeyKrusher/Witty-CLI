# Code written by Jack Clark
# Copyright the M.I.T. License
# This code gets the operating system of the user
import os
import sys
"""
	Linux (2.x and 3.x)	'linux2'
	Windows	'win32'
	Windows/Cygwin	'cygwin'
	Mac OS X	'darwin'
	OS/2	'os2'
	OS/2 EMX	'os2emx'
	RiscOS	'riscos'
	AtheOS	'atheos'
"""

class GetOS():
	user_os = sys.platform

	Windows = ["win32", "cygwin"]
	Linux = ["linux2"]
	MacOS = ["darwin"]

	# def __init__(self, user_os, Windows, Linux, MacOS):
	# 	self.user_os = user_os
	# 	self.Windows = Windows
	# 	self.Linux = Linux
	# 	self.MacOS = MacOS

	def get_user_os(user_os):
		if user_os in Windows:
			return "Windows"
		elif user_os in Linux:
			return "Linux"
		elif user_os in MacOS:
			return "MacOS"
		else:
			return "OSError"
if __name__ == "__main__":
	# Test out the code
	MyOperatingSystem = GetOS()
	print MyOperatingSystem.get_user_os()