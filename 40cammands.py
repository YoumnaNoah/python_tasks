#speaking with cmd using python lab
import os
print("1-ls command: lists the content of the directory you are in")
y = os.popen("ls") #excute ls and store the output in a astring
y=y.read()
print(y)

print("2- pwd command: print the full path of the current directory") #ask about the l and p didn't workout
y_1= os.popen("pwd") #excute pwd and store the output in a astring
y_1=y_1.read()
print(y_1)

print("3- cd / command: change directory you are in to the root file")
y_2= os.chdir("/") #excute cd 
y_12= os.popen("pwd") #excute pwd and store the output in a astring
y_12=y_12.read()
print(y_12)

print("4- cd .. command: go back one directory")
os.system("cd ..") #excute cd.. 
                        #not working
y_11= os.popen("pwd") #excute pwd and store the output in a astring
y_11=y_11.read()
print(y_11)             
print("5- cd~ command: sends you back to home") #same as above
os.chdir("/home/youmna")

print("6- cd- command: sends you back to the previously opened directory wherever it is")
#dont know how to do it yet

                        
print("7- touch command:create new file ..created a file named grade.txt")
y_7= os.popen("touch /home/youmna/Documents/grade.txt")


print("8- gedit command: open the file if it exists and creat new one and open it if it doesn't..opened a file named grade.txt")
y_8=os.popen("gedit grade.txt")


print("9-cat command print the content") #ask about the l and p didn't workout
y_9= os.popen("cat test.py") #excute cat and store the output in a astring
y_9=y_9.read()
print(y_9)

print("10-cat command can also concatenate two files contents together and create a new merged file")
A=os.popen("cat grade.txt test.py > mergedfile") 
A=A.read()
print(A)

print("11- cp command: copy files and directories and their content")
A_1 = os.system("cp test.py /home/youmna/Documents")

print("12- mkdir creates a new directory")
os.system("mkdir Music/songs")

print("13- cp -R command: copy the directory")
os.system("cp -R /home/youmna/Music/songs /home/youmna/Documents") 

print("14- rmdir command: deletes an empty directory")
os.system("rmdir ./Music/songs") #ask about writing the path what will it remove

print("15- rm command: deletes files within a directory")
os.system("rm mergedfile")

print("16- locate command: find a file in the database system..also adding the -i can remove the case sensitive part")
A_2=os.popen("locate searchfile") #notworking
A_2= A_2.read()
print(A_2)

print("17- find command: find a file in a specific directory")
A_3=os.popen("find test.c") 
A_3= A_3.read()
print(A_3)

print("18- grep command: it lists to you all the files with word you are searching for and you can also search for a word inside a file")
print("searching for the word command in test.py file")

A_4=os.popen("grep command test.py") 
A_4= A_4.read()
print(A_4)

print("19- df command report the system disk usage shown in percentage and kilobyte")
A_5=os.popen("df -h") 
A_5= A_5.read()
print(A_5)

print("20- du command: check how much space a file or a directory takes up")
A_6=os.popen("du home/youmna/Documents") 
A_6= A_6.read()
print(A_6)

print("21- head command: allow you to view the first ten lines of a text..there are options to change the number of lines")
print("==> reading first 10 lines of test.py")
A_7=os.popen("head test.py") 
A_7= A_7.read()
print(A_7)

print("22- tail command: display the last ten lines of a file")
print("==> reading the last 10 lines of test.py")
A_8=os.popen("tail test.py") 
A_8= A_8.read()
print(A_8)

print("23- diff command: compare the content of two files line by line then displays the parts that do not match")
print("comparing the test.py with grade.txt")
A_9=os.popen("diff test.py grade.txt") 
A_9= A_9.read()
print(A_9)

print("24- tar command: archieves multiple files int TAR file..creating newarciive.tar ")
os.system("tar -cvf newarchive.tar /home/youmna/Documents")

print("25- chmod command: modifies a file or directory's read write and excute permissions")
os.system("chmod 777 test.py")

print("26- chown command: lets you change the ownership of a file or directory or a symbolic link to a specifies user name")
os.system("chown user2 new")




