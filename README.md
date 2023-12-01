# master_thesis
Master thesis project
Steps to install the Algorithm search website

Step 1: 
	Open MySQL Workbench and run all the mysql statements in “createquery.sql” file.
	
Step 2:
	Goto folder “Python program to transfer Algorithms To MySQL”, Open cmd and type “python filetodb.py’. This will transfer all algorithms to fileDetails table as BLOB file.
	
Step 3:
Open Visual Studio Code, Notepad++ or any other editor.

Step 4: 
Goto File -> Open Folder -> Select the Algorithm search website folder

Step 5: 
In the command prompt go to the folder path. 
Enter command at the terminal:  $ py -m streamlit run home.py
