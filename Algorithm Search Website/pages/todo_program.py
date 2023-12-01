#todo program - to add new program listed in todo search
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
import pandas as pd #Data analysis library, to analyze results from mysql script
import sys #System parameters and functions
from datetime import datetime #To get date and time
from header import navbar #customized navigation bar
from db_config import dbinit #To initialize mysql connection parameters
from db_config import get_extensionid #to get extension id from extension name
from db_config import get_userid #to get userid from username

username = navbar("todo_program")#pass the header function with search as page name

mydb = dbinit() #intialization of db parameters

userId = get_userid(username)

cursor = mydb.cursor()

#insert query to add new algorithm into fileDetails table
add_query = ("INSERT INTO fileDetails "
               "( file_name, file_description , user_id, extension_id, file_data, created_date) "
               "VALUES (%s, %s, %s, %s, %s, %s)")


#initialize all parameters with empty value
filePath = ""
filename = ""
prog_content = ""
prog_description = ""
option = ""
extId = ""

#to get query parameter i.e program name passed from the view program
query_params = st.experimental_get_query_params() #streamlit get query parameters
prog_name = query_params.get("key1")[0]
prog_lang = query_params.get("key2")[0]

#check if program name and programming language is null
if prog_name is None:
   prog_name = ""

if prog_lang is None:
   prog_lang = ""

#get extensionid from extensiontype
if prog_lang != "":
   extId = get_extensionid(prog_lang)

#add program form shown to user to fill in the form
with st.form(key='addprogform',clear_on_submit=True):
      prog_name = st.text_input("Program name", prog_name, disabled=True)
      prog_lang = st.text_input("Programming Language", prog_lang, disabled= True)
      
      #get program description details
      prog_description = st.text_input("Description")

      #file content is the code of program name in the selected programming language.
      prog_content = st.text_area("Please enter code here","", height=400)

      #submit the form
      submit_btn = st.form_submit_button("Add")

if prog_name is not '' and prog_lang is not '' :
   #if submit button clicked
   if submit_btn:
         #Remove white spaces from the program name entered
         prog_name = prog_name.replace(" ", "")

         #check if program name already exists
         df_file = pd.read_sql("select * from fileDetails where file_name = '%s' and extension_id = %s "% (prog_name, extId), mydb)
         
         #current date time is recorded as the program is added to a new file
         current_dateTime = datetime.now()

         #convert string content to binary to insert into mysql database
         prog_content_bin = prog_content.encode('UTF-8')

         #show streamlit warning message that record already exists
         if df_file.size > 0:
            st.warning("Data already added!")
            sys.exit()

         #add row in fileDetails table with the user added data
         add_data = (prog_name, prog_description, str(userId), str(extId), prog_content_bin, current_dateTime)
         cursor.execute(add_query, add_data)
         
         #update searchData table with the result_exists of the program name added
         query = """Update searchData set result_exists = 1 where file_name = '%s' and extension_id = %s"""
         cursor.execute(query ,params=(prog_name, extId))
         
         mydb.commit() #commit changes to database
         cursor.close() #close cursor connection
         st.success("Code added successfully!")
         
#condition error message if Program Name/Program language is not entered
else:
   st.error("Please enter Program Name/Program language")
   