import os
from os import path
import sys
import shutil
import time
from os import listdir

Firstpath = input("Enter your file path:")
while path.exists(Firstpath)==False:
	print("Incorrect file path")
	Firstpath = input("Enter your file path again:")

Name=path.basename(Firstpath)



if path.exists(Firstpath):
	Newname =input("Enter your new file name:")
	Currentpath=Firstpath.replace(Name,Newname)
	Safe=Currentpath
	Lastpath=path.dirname(Currentpath)
	print("Old path:"+Firstpath)
	print("New path:"+Currentpath)
	os.rename(Firstpath,Currentpath)
#	for index,file in enumerate(subfolder):
#		print(file)
#		newpath=path.realpath(npath)+"\\"+Newname
#		print(newpath)
#		os.rename(npath+"\\"+file,newpath+str(index))

else:
	print("File not found\n")

DirectoryPath = set()
Filecount=0
while path.exists(Currentpath):
	if len(listdir(Currentpath))!=0:
		folderlist = listdir(Currentpath) # Get all subfiles
	else:
		folderlist=listdir(path.dirname(Currentpath))
		Currentpath=Lastpath
		Lastpath=path.dirname(Lastpath)

	for index,file in enumerate(folderlist):
		filePath = Currentpath+"\\"+file
		if(Currentpath == path.dirname(Safe) and Filecount>0):
			time.sleep(1)
			print("Complete!")
			sys.exit()
			exit()
		else:
			if filePath not in DirectoryPath:
				Filecount=Filecount+1
				filename = Currentpath + "\\"+Newname+str(Filecount)
				os.rename(filePath,filename)
				DirectoryPath.add(filename)
				Lastpath=Currentpath
				Currentpath=filename
				break
			elif filePath in DirectoryPath:
				if folderlist.index(file) == len(folderlist)-1:
					folderlist=listdir(path.dirname(Currentpath))
					Currentpath=Lastpath
					Lastpath=path.dirname(Lastpath)
					break
				else:
					continue




