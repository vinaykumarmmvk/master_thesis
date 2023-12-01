#view log - webpage to view log details selected from search logs
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
import pandas as pd #Data analysis library, to analyze results from mysql script
from header import navbar #customized navigation bar
from db_config import dbinit #To initialize mysql connection parameters
from page_redirect import open_page #to redirect to url after button click

username = navbar("view_log")#pass the header function with search as page name

#to get query parameter i.e program name passed from the view program
query_params = st.experimental_get_query_params() #streamlit get query parameters
searchId = query_params.get("key1")


mydb = dbinit() #intialization of db parameters

# pandas read searchData from mysql query
df = pd.read_sql("SELECT * FROM searchData WHERE search_id = %d " % (int(searchId[0])), mydb)

# streamlit subheader with search log id
st.subheader("Search Log id "+searchId[0])
st.write("**searched for**      : "+df["searched_for"][0])

searchedFor = df["searched_for"][0]
ext_id = df["extension_id"][0]

#search log details are displayed
st.write("Result Exists: "+str(df["result_exists"][0]))
st.write("Extension Id : "+str(df["extension_id"][0]))
st.write("Search Date : "+str(df["search_date"][0]))

# query to get occurence of the same search program name
dfCount = pd.read_sql("select * from searchData where searched_for like '%s' and extension_id =%s " % (searchedFor, int(ext_id)), mydb)
mydb.close() #close database connection
st.write("Count/frequency : "+str(dfCount.size))

#download log details as text file
download_data = "Searched for: "+searchedFor+"\n Extension Id:"+str(ext_id)+"\n Search Date:"+str(df["search_date"][0])+"\n Result exists: "+str(df["result_exists"][0])+"\n Frequency: "+str(dfCount.size)
st.download_button('Download', download_data, file_name=searchedFor+".txt")

# check if add button clicked, to add new algorithm
if st.button("Add"):
      open_page("/add_program")
