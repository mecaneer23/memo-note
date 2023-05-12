import os
if os.name == 'nt':
	import msvcrt
else:
	try:
		import getch
	except ModuleNotFoundError:
		print("You need to install getch. On debian/ubuntu, you can run \"./get_getch.sh\", otherwise, make sure you have pip3 (install python3-pip), and download getch (pip3 install getch)")