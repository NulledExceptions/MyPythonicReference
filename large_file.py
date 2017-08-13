import os

cwd = os.getcwd()  
files = [f.endswith('.txt') for f in os.listdir(cwd)]
for file in files:
	with open(file) as FileObj:
	    for line in FileObj:
          print line
