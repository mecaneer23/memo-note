import sys
import json
import os, subprocess

flags = {
	"title": False,
	"note": False
}
message = None
possibleTitle = None

def flagHandler(flag):
	notes = open("notes.json").read()
	newNotes = ""
	for i in notes:
		if i not in ("\t", "\n"):
			if i == "\'":
				i = "\""
			newNotes += i
	notes = newNotes
	notes = json.loads(f"{notes}")
	flag = flag[1:]
	if flags["title"] == True:
		flags["title"] = False
		if flag in ["-add", "a"]:
			notes[message] = "none"
		elif flag in ("-remove", "r"):
			try:
				notes.pop(message)
			except KeyError:
				print("Sorry, that is not a valid title.")
	if flags["note"] == True:
		flags["note"] = False
		if flag in ("-add", "a"):
			notes[possibleTitle] = message
	elif flag in ["-title", "t"]:
		flags["title"] = True
	elif flag in ("-note", "n"):
		flags["note"] = True
	elif flag in ("-list", "l"):
		print(notes)
	elif flag in ("-show", "s"):
		print(notes[message])
	elif flag in ("-help", "h"):
		print("""[--title]	[-t]	set mode to title	-t -a MyMemo
[--note]	[-n]	set mode to note	-n -a "This is a memo"
[--add]		[-a]	add title or note	-t -a MyMemo
[--remove]	[-r]	remove title or note	-t -r MyMemo
[--list]	[-l]	list all notes		-l
[--show]	[-s]	show a specific note 	-s MyMemo
[--exit]	[-e]	exit program		-e""")
	with open("notes.json", "w") as f:
		printStr = ""
		for i in str(notes):
			if i == "\'":
				i = "\""
			printStr += i
		f.write(printStr)

def main():
	global message, possibleTitle
	try:
		if sysargv[-1]:
			argsExist = True
	except IndexError:
		print("Make sure to add flags or type [--help].")
		exit()
	if sysargv[-1][0] == "-":
		message = "none"
	else:
		message = sysargv[-1]
	if sysargv[-2][0] == "-":
		possibleTitle = "none"
	else:
		possibleTitle = sysargv[-2]
	for i in sysargv:
		if str(i)[0] == "-":
			flagHandler(i)


def mainNoFlags():
	mode = 0
	notes = open("notes.json").read()
	newNotes = ""
	for i in notes:
		if i not in ("\t", "\n"):
			if i == "\'":
				i = "\""
			newNotes += i
	notes = newNotes
	notes = json.loads(f"{notes}")
	for i in sysargv:
		if i in ["title", "t"]:
			mode = 1
		elif i in ["note", "n"]:
			mode = 2
		elif i in ["add", "a"]:
			if mode == 0:
				print("Please enter [title, note]")
			if mode == 1:
				pass
			if mode == 2:
				pass
		elif i in ["remove", "r"]:
			pass
		elif i in ["list", "l"]:
			pass
		elif i in ["show", "s"]:
			pass
		elif i in ["exit", "e"]:
			pass
		elif i in ["help", "h"]:
			pass
	with open("notes.json", "w") as f:
		printStr = ""
		for i in str(notes):
			if i == "\'":
				i = "\""
			printStr += i
		f.write(printStr)

if __name__ == "__main__":
	try:
		if sys.argv[-1]:
			sysargv = sys.argv
			mainNoFlags()
	except IndexError:
		while True:
			sysargv = input("MemopadNoteTaker>").split(" ")
			sysargv.insert(0, __name__)
			if sysargv[1] in ("--exit", "-e"):
				exit()
			main()