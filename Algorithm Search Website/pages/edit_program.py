#edit program page - webpage to edit existing algorithm
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
from header import navbar #customized navigation bar
import pandas as pd #Data analysis library, to analyze results from mysql script
from datetime import datetime #To get date and time
from db_config import dbinit #To initialize mysql connection parameters
from db_config import get_extensionid #function to get extensionid 
from db_config import get_userid #function to get userid
from db_config import retrieve_userskills #function to get user skillset

username = navbar("edit_program")#pass the header function with edit program as page name

mydb = dbinit() #intialization of db parameters

#to get query parameter i.e program name passed from the view program
query_params = st.experimental_get_query_params() #streamlit get query parameters
part_filename = query_params.get("key1")

#Retrieve user Id from username 
userId = get_userid(username)

#get user skillset by passing userId
skill_set = retrieve_userskills(userId)


cursor = mydb.cursor()#Creating a cursor object using the cursor() method to execute mysql query

#mysql insert query string
addfileedit_query = ("INSERT INTO fileEditDetails "
               "( file_id, edit_description , user_id, edited_date) "
               "VALUES (%s, %s, %s, %s)")

addfile_query = ("INSERT INTO fileDetails "
               "( file_name, file_description , user_id, extension_id, file_data, created_date) "
               "VALUES (%s, %s, %s, %s, %s, %s)")

#query string value assigned to file name variable
fname = part_filename[0]

st.subheader(fname) #streamlit subheader component


#show streamlit dropdown program language list based on the skill set of the user
option = st.selectbox('Please Select Programming language to edit:', skill_set)

#streamlit text input to enter edit description details
editDescription = st.text_input("Please enter edit description")

#READ file content inside the tab cond. 
#if file not found or empty keep tab empty
#user specalized with specific lang. show him with add or edit option

#streamlit subheader component
st.subheader(option)

#function to get extension id from extension name i.e programming language selected 
extId = get_extensionid(option)

#try catch block to handle exception
try:
   #pandas to filter file data field from select mysql query
   df_file = pd.read_sql("select file_data from fileDetails where extension_id = %s and file_name = '%s'"% (extId, fname), mydb)
   
   #if result exists from the query
   if df_file.size != 0:
      df_data = df_file['file_data'][0].decode('UTF-8') #decodes BLOB type to string type
   else:
      df_data = ""

   prog_content = st.text_area("Edit", df_data, height=400) #streamlit text area to edit code for algorithm 


except Exception as e:
            prog_content = st.text_area("Edit","", height=400) #streamlit text area with empty value
            st.error(f"Error log : {e}")

#check if streamlit submit button is clicked
if st.button("Submit"):
   if editDescription != '':
      #once submit update the c,c++,java... files with the changed content
      #open file, write changes

      #fetch current data and time and initialize it to a variable
      current_dateTime = datetime.now()

      #string type encoded to binary type to store in table as BLOB type
      prog_content_bin = prog_content.encode('UTF-8')
      
      #try statement to check if the file entry already exists 
      try:
         #pandas read query to get fileId from filename and extensionid
         fileId = (pd.read_sql("select file_id from fileDetails where file_name = '%s' and extension_id = '%s'"% (fname,extId), mydb))['file_id'][0]
         
         if fileId > 0:
              #update file data
              query = """Update fileDetails set file_data = %s where file_id = %s"""
              cursor.execute(query ,params=(prog_content_bin, str(fileId)))
              st.success("File updated")

      #catch statement to handle if the file entry doesn't exists 
      except Exception as e:
            
            #create an entry in fileDetails and then fetch fileid
            addfile_data = (fname, editDescription, str(userId), extId, prog_content_bin ,current_dateTime)
            cursor.execute(addfile_query, addfile_data)

            #pandas read sql query to get the file_id of the added new file data
            fileId = (pd.read_sql("select file_id from fileDetails where file_name = '%s' and extension_id = '%s'"% (fname,extId), mydb))['file_id'][0]
            
            st.success("file entry added") #streamlit success message showing entry added
      
      #file edit parameters
      fileedit_data = (str(fileId), editDescription, str(userId), current_dateTime)
      
      #add file edit details into fileeditdetails table
      cursor.execute(addfileedit_query, fileedit_data)
      
      mydb.commit() #commit changes to mysql database
      cursor.close() #close cursor connection

      #streamlit success message to show that exection was success
      st.success("Algorithm code updated successfully!") 

   #else statement executed when edit description is empty
   else:
      st.error("Please enter edit description") #streamlit error message to enter edit description