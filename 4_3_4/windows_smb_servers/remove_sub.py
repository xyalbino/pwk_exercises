#!/usr/bin/env python
if __name__ == '__main__':

	contents, edited = [], []
	
	
	try:
		with open("./windows_smb_servers", "r") as read_file:
			for line in read_file:
				contents.append(line.strip())
	except:
			print("something went wrong..")
	finally:
			read_file.close()
	
	for line in contents:
		edited_line = line.replace("445/", "")
		edited.append(edited_line)

	for line in edited:
		print(line)
	
