#!/bin/python3

def main():
	import sys
	import json
	import os, subprocess
	# if os.name == 'nt':
	# 	import msvcrt
	# else:
	# 	try:
	# 		import getch
	# 	except ModuleNotFoundError:
	# 		print("You need to install getch. On debian/ubuntu, you can run \"./get_getch.sh\", otherwise, make sure you have pip3 (install python3-pip), and download getch (pip3 install getch)")

	# test if running in single instance or program mode
	if sys.argv[-1] == sys.argv[0]:
		# program mode
		while True:
			notes = open("notes.json").read()
			newNotes = ""
			for i in notes:
				if i not in ("\t", "\n"):
					if i == "\'":
						i = "\""
					newNotes += i
			notes = json.loads(f"{newNotes}")
			input_args = input(">>> ").lower().split(" ")
			if input_args[0] in ["help", "h"]:
				print("INPUT\t\tFUNCTION\t\tEXAMPLE\n[help, h]\tshows this message\th\n[add, a]\tadd title and note\ta MyMemo This is an example of a memo\n[remove, r]\tremove note\t\tr MyMemo\n[list, l, ls]\tlist all notes by title\tl\n[rawlist, rl]\tlist all notes\t\trl\n[show, s]\tshow a specific note\ts MyMemo\n[file, f]\tadd note to a text file\tf MyMemo\n[clear, c, cls]\tclear screen\t\tc\n[exit, e]\texit program\t\te\n")
			elif input_args[0] in ["add", "a"]:
				try:
					temp = ""
					for i in input_args[2:]:
						temp += str(i)+" "
					temp = temp[:-1]
					notes[input_args[1]] = temp
					print(f"Added title: {input_args[1]}, with note: {temp}")
				except IndexError:
					print("Make sure to add a title, as well as a memo")
					notes.pop(input_args[1])
			elif input_args[0] in ["remove", "r"]:
				try:
					notes.pop(input_args[1])
					print(f"Removed {input_args[1]}")
				except IndexError:
					print("Make sure to include a note to remove")
				except KeyError:
					print("Can't remove a note that doesn't exist")
			elif input_args[0] in ["list", "l", "ls"]:
				if str(notes.keys()) == "dict_keys([])":
					print("No stored memos")
				else:
					out = ""
					for i in str(notes.keys())[11:-2]:
						if i in ["\'", ","]:
							pass
						elif i == " ":
							out += i+"\n"
						else:
							out += i
					print(out)
			elif input_args[0] in ["rawlist", "rl"]:
				print(notes)
			elif input_args[0] in ["show", "s"]:
				try:
					print(notes[input_args[1]])
				except IndexError:
					print("Make sure to include a note to show")
				except KeyError:
					print("Can't show a note that doesn't exist")
			elif input_args[0] in ["file", "f"]:
				try:
					if sys.platform == "win32": # Windows
						with open("notes.bat", 'w') as g:
							g.write(f"echo {notes[input_args[1]]} >> {input_args[1]}.txt\nnotepad {input_args[1]}.txt")
						subprocess.call("notes.bat")
					elif sys.platform in ["linux2", "linux", "posix"]: # Linux
						with open("notes.sh", 'w') as g:
							g.write(f"#!/bin/bash\necho {notes[input_args[1]]} >> {input_args[1]}.txt\nvi {input_args[1]}.txt")
						subprocess.call("bash notes.sh")
					elif sys.platform == "darwin": # macOS
						with open("notes.sh", 'w') as g:
							g.write(f"#!/bin/sh\necho {notes[input_args[1]]} >> {input_args[1]}.txt\nopen -a TextEdit {input_args[1]}.txt")
						subprocess.call("bash notes.sh")
						pass
				except IndexError:
					print("Make sure to include a note")
				except KeyError:
					print("Can't make a file for a note that doesn't exist")
			elif input_args[0] in ["exit", "e"]:
				try:
					if input_args[1] == ["c"]:
						os.system('cls' if os.name == 'nt' else 'clear')
						exit()
				except IndexError:
					exit()
				exit()
			elif input_args[0] in ["ec"]:
				os.system('cls' if os.name == 'nt' else 'clear')
				exit()
			elif input_args[0] in ["clear", "c", "cls"]:
				os.system('cls' if os.name == 'nt' else 'clear')
			elif input_args == ['']:
				pass			
			else:
				print("Sorry, that is not a recognized command - input [help] for a list of commands")
			with open("notes.json", "w") as f:
				printStr = ""
				for i in str(notes):
					if i == "\'":
						i = "\""
					printStr += i
				f.write(printStr)
	else:
		# single instance mode
		notes = open("notes.json").read()
		newNotes = ""
		for i in notes:
			if i not in ("\t", "\n"):
				if i == "\'":
					i = "\""
				newNotes += i
		notes = json.loads(f"{newNotes}")
		input_args = sys.argv
		if input_args[1] in ["help", "h"]:
			print("INPUT\t\tFUNCTION\t\tEXAMPLE\n[help, h]\tshows this message\th\n[add, a]\tadd title and note\ta MyMemo This is an example of a memo\n[remove, r]\tremove note\t\tr MyMemo\n[list, l, ls]\tlist all notes by title\tl\n[rawlist, rl]\tlist all notes\t\trl\n[show, s]\tshow a specific note\ts MyMemo\n[file, f]\tadd note to a text file\tf MyMemo\n")
		elif input_args[1] in ["add", "a"]:
			try:
				temp = ""
				for i in input_args[3:]:
					temp += str(i)+" "
				temp = temp[:-1]
				notes[input_args[2]] = temp
				print(f"Added title: {input_args[2]}, with note: {temp}")
			except IndexError:
				print("Make sure to add a title, as well as a memo")
				notes.pop(input_args[2])
		elif input_args[1] in ["remove", "r"]:
			try:
				notes.pop(input_args[2])
				print(f"Removed {input_args[2]}")
			except IndexError:
				print("Make sure to include a note to remove")
			except KeyError:
				print("Can't remove a note that doesn't exist")
		elif input_args[1] in ["list", "l", "ls"]:
			if str(notes.keys()) == "dict_keys([])":
				print("No stored memos")
			else:
				out = ""
				for i in str(notes.keys())[11:-2]:
					if i in ["\'", ","]:
						pass
					elif i == " ":
						out += i+"\n"
					else:
						out += i
				print(out)
		elif input_args[1] in ["rawlist", "rl"]:
			print(notes)
		elif input_args[1] in ["show", "s"]:
			try:
				print(notes[input_args[2]])
			except IndexError:
				print("Make sure to include a note to show")
			except KeyError:
				print("Can't show a note that doesn't exist")
		elif input_args[1] in ["file", "f"]:
			try:
				if sys.platform == "win32": # Windows
					with open("notes.bat", 'w') as g:
						g.write(f"echo {notes[input_args[2]]} >> {input_args[2]}.txt\nnotepad {input_args[2]}.txt")
					subprocess.call("notes.bat")
				elif sys.platform in ["linux2", "linux", "posix"]: #Linux
						with open("notes.sh", 'w') as g:
							g.write(f"#!/bin/bash\necho {notes[input_args[2]]} >> {input_args[2]}.txt\nvi {input_args[2]}.txt")
						subprocess.call("bash notes.sh")
				elif sys.platform == "darwin": # macOS
					with open("notes.sh", 'w') as g:
						g.write(f"#!/bin/sh\necho {notes[input_args[2]]} >> {input_args[2]}.txt\nopen -a TextEdit {input_args[2]}.txt")
					subprocess.call("bash notes.sh")
					pass
			except IndexError:
				print("Make sure to include a note")
			except KeyError:
				print("Can't make a file for a note that doesn't exist")
		else:
			print("Sorry, that is not a recognized command - input [help] for a list of commands\n")
		with open("notes.json", "w") as f:
			printStr = ""
			for i in str(notes):
				if i == "\'":
					i = "\""
				printStr += i
			f.write(printStr)

if __name__ == "__main__":
	main()
