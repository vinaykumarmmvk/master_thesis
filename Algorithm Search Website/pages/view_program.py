#view program - webpage to view algorithm selected from search algorithm
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
import pandas as pd #Data analysis library, to analyze results from mysql script
from header import navbar #customized navigation bar
from db_config import dbinit #To initialize mysql connection parameters
from db_config import fetchall_extensionids #to fetch all extension ids
from db_config import fetchall_extensiontypes #to fetch all extension names
from page_redirect import open_page #redirect to url on button click

username = navbar("view_program")#pass the header function with search as page name

mydb = dbinit() #intialization of db parameters

#to get query parameter i.e program name passed from the view program
query_params = st.experimental_get_query_params() #streamlit get query parameters
part_filename = query_params.get("key1")

st.write("#")
st.subheader("View Algorithm - "+part_filename[0])

# whitespace for increasing width of tabs
whitespace = 7

# fetch all programming langauges
progList = fetchall_extensiontypes()
# steamlit tabs for different programming languages
tab1, tab2, tab3, tab4 ,tab5 ,tab6 ,tab7  = st.tabs([s.center(whitespace,"\u2001") for s in progList])

#query parameter initialized to fname
fname = part_filename[0]

#fetch all extension ids from extension table
extIds = fetchall_extensionids()

#file data initialized to empty set
fdata = []

# fetch file data of each programming language and add it into fdata set
for extId in extIds:
   df_file = pd.read_sql("select file_data from fileDetails where extension_id = %s and file_name = '%s'"% (str(extId),fname), mydb)
   if df_file.size != 0:
      #to convert blob type to string type
      df_data = df_file['file_data'][0].decode('UTF-8')
   else:
      df_data = ""
   fdata.append(df_data)

#below are internal navigation tabs within a page 
#for different progarmming languages
with tab1:
   st.subheader("Java")
   st.code(fdata[0], language='java')
   download_data = fdata[0]
   ext = ".java"
   #streamlit download button with file data fetched from database
   st.download_button('Download', download_data, file_name=fname+ext)

with tab2:
   st.subheader("C")
   st.code(fdata[1], language='c')
   download_data = fdata[1]
   ext = ".c"
   #streamlit download button with file data fetched from database
   st.download_button('Download', download_data, file_name=fname+ext)

with tab3:
   st.subheader("C++")
   st.code(fdata[2], language='c')
   download_data = fdata[2]
   ext = ".cpp"
   #streamlit download button with file data fetched from database
   st.download_button('Download', download_data, file_name=fname+ext)

with tab4:
   st.subheader("C#")
   st.code(fdata[3], language='c')
   download_data = fdata[3]
   ext = ".cs"
   #streamlit download button with file data fetched from database
   st.download_button('Download', download_data, file_name=fname+ext)

with tab5:
   st.subheader("JS")
   st.code(fdata[4], language='js')
   download_data = fdata[4]
   ext = ".js"
   #streamlit download button with file data fetched from database
   st.download_button('Download', download_data, file_name=fname+ext)

with tab6:
   st.subheader("python")
   st.code(fdata[5], language='py')
   download_data = fdata[5]
   ext = ".py"
   #streamlit download button with file data fetched from database
   st.download_button('Download', download_data, file_name=fname+ext)

with tab7:
   st.subheader("PHP")
   st.code(fdata[6], language='php')
   download_data = fdata[6]
   ext = ".php"
   #streamlit download button with file data fetched from database
   st.download_button('Download', download_data, file_name=fname+ext)

#check if user is loggedin
if username != "":
   #if edit button is clicked
   if st.button("Edit"):
      open_page("/edit_program?key1="+fname)
   
   #if add button is clicked
   if st.button("Add"):
      open_page("/add_program")
