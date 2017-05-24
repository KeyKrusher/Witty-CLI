import os
import sys
from OSGetter import GetOS
import ScreenStuff

# Get user OS
os_getter = GetOS()
user_os = os_getter.get_user_os()
# Start the actual good stuff
clear_screen()
# Sweet introduction
print "__      __       .__                                  __            __      __.__  __    __          ._."
print "/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   /  \    /  \__|/  |__/  |_ ___.__.| |"
print "/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   /  \    /  \__|/  |__/  |_ ___.__.| |"
print "\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  \   \/\/   /  \   __\   __<   |  || |"
print " \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  \        /|  ||  |  |  |  \___  | \|"
print "  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/    \__/\  / |__||__|  |__|  / ____| __"
print "       \/       \/          \/            \/     \/                        \/                  \/      \/"
print "\n\n"

check_for_cd = raw_input("Are you in the current directory that you want to push to github? (y/n): ")

if check_for_cd.lower() == "y":
	remote_origin = "Remote origin?: "
else:
	directory_to_goto = raw_input("What is the directory?: ")
	try:
		os.chdir(directory_to_goto)
	except OSError:
		if user_os == "Windows":
			os.system("cls")
		elif user_os == "MacOS":
			os.system("clear")
		elif user_os == "Linux":
			os.system("clear")
		else:
			print "Unsupported Operating System."
		print "Invalid Directory!"
		print "\nThe program will now exit!"
		time.sleep(3)
		exit(1)
# __name__ should be __main__ btw
if __name__ == "__main__":
	directory_to_nav = raw_input("Path to directory: ")
	os.chdir(directory_to_nav)
	remote_origin = raw_input("Remote Origin")
