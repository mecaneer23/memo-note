import sys, json

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

if __name__ == "__main__":
	while True:
		sysargv = input("MemopadNoteTaker>").split(" ")
		sysargv.insert(0, __name__)
		if sysargv[1] in ("--exit", "-e"):
			exit()
		main()