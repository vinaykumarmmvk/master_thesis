#add program page - webpage to add new algorithm
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
from header import navbar #customized navigation bar
username = navbar("add_program") #pass the header function with add program as page name

import pandas as pd #Data analysis library, to analyze results from mysql script
import sys #System parameters and functions
from datetime import datetime #To get date and time
from db_config import dbinit #To initialize mysql connection parameters
from db_config import get_extensionid #function to get extensionid 
from db_config import get_userid #function to get userid
from db_config import retrieve_userskills #function to get user skillset

mydb = dbinit() #intialization of db parameters

#Retrieve user Id from username 
userId = get_userid(username) 

#Retrieve the programming lang. the user is skilled/experienced 
skill_set = retrieve_userskills(userId)

cursor = mydb.cursor()#Creating a cursor object using the cursor() method to execute mysql query

#insert query to insert data entered by user into fileDetails table
add_query = ("INSERT INTO fileDetails "
               "( file_name, file_description , user_id, extension_id, file_data, created_date) "
               "VALUES (%s, %s, %s, %s, %s, %s)")

skill_setIds = [] #initialize skill set to empty array

#if user skill set is not empty
if len(skill_set) != 0:

   #streamlit for with key value as addprogform 
   with st.form(key='addprogform', clear_on_submit=True):
      prog_name = st.text_input("Enter program name") #streamlit text input component to enter program name
      prog_description = st.text_input("Description") #streamlit text input component to enter description

      #streamlit dropdown to select programming language
      option = st.selectbox('Please Select Programming language to edit:', skill_set)

      #file content is the code of program name in the selected programming language.
      prog_content = st.text_area("Please enter code here","", height=400)

      #streamlit submit button and it's state stored in variable
      submit_btn = st.form_submit_button("Add")

   #validate if program name is entered and programming language is selected
   if prog_name is not '' and len(option) != 0 :

      #if submit button is clicked
      if submit_btn:
         #Remove white spaces from the program name entered
         prog_name = prog_name.replace(" ", "")

         #check if program name already exists by passing it to a query
         df_file = pd.read_sql("select * from fileDetails where file_name = '%s'"% (prog_name), mydb)
         
         #if above result is not empty then program name already exists
         if df_file.size > 0:
            st.error("Program name already exists!")#streamlit error message
            sys.exit()#exit from executing the remaining part of code
         
         #blob file content stored in mysql converted to string type by encoding it
         prog_content_bin = prog_content.encode('UTF-8')

         #fetch extension id from extension type
         ext_id = get_extensionid(option)
   
         #current date time is recorded as the program is added to a new file
         current_dateTime = datetime.now()

         #update database table with the added data
         add_data = (prog_name, prog_description, str(userId), str(ext_id), prog_content_bin, current_dateTime)
         cursor.execute(add_query, add_data) #execute add query with add data parameters
         mydb.commit() #commit the changes done to database
         cursor.close() #close cursor connection
         st.success("Code added successfully!")

   else:
      #else statement executed when program name is not entered
      st.error("Please enter Program Name")

else:
   #give hyperlink to todo screen to update skills
   st.write("\n Please update your skill set to add/edit program.")