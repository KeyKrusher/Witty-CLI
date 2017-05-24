# Code written by Jack Clark
# Copyright under M.I.T. License
import subprocess

class GitRepo(remote_origin):
	# All of these should only get run if they're in the current directory
	def git_initialize():
		subprocess.call("git init")
	def git_add():
		subprocess.call("git add .")
	def git_commit():
		commit = raw_input("Commit text: ")
		subprocess.call("git commit -m " + commit)
	def get_remote_origin(remote_origin):
		subprocess.call("git remote add origin " + remote_origin)
	def push_master():
		subprocess.call("git push -u origin master")

if __name__ == "__main__":
	# Test a full git push from scratch
	test_repo = GitRepo("https://github.com/KeyKrusher/TestRepo")
