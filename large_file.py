import os

cwd = os.getcwd()  
files = ['{}{}'.format(dir_path,f) for f in os.listdir(dir_path) if f.endswith('.json')]
#files = [f.endswith('.txt') for f in os.listdir(cwd)]
for file in files:
	with open(file) as FileObj:
	    for line in FileObj:
          print line

	
	
#insert headers
echo 'Input Hash, URL,Classified Sentence,Name,ID,Path,ID Path,Source File' | cat - stream_test.csv > temp && mv temp stream_test.csv
