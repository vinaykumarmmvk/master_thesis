#view ailog - webpage to view openai log details selected from search logs
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
import pandas as pd #Data analysis library, to analyze results from mysql script
from header import navbar #customized navigation bar
from db_config import dbinit #To initialize mysql connection parameters

username = navbar("view_ailog")#pass the header function with search as page name

#to get query parameter i.e program name passed from the view program
query_params = st.experimental_get_query_params() #streamlit get query parameters
file_id = query_params.get("key1")

mydb = dbinit() #intialization of db parameters

#fetch log details from database
df_logdetails = pd.read_sql("SELECT * FROM fileDetails WHERE file_id = %d " % (int(file_id[0])), mydb)

#close database connection
mydb.close()

#show OpenAI log details
st.text_input("Search Description: ", value=str(df_logdetails["file_description"][0]), disabled=True)
st.write("Searched date : "+str(df_logdetails["created_date"][0]))
st.write("OpenAI response:")
fdata = df_logdetails["file_data"][0].decode('UTF-8')
st.write(fdata)

#setup download data with all the log details
download_data = "Search Description: "+str(df_logdetails["file_description"][0])+"\n Searched date : "+str(df_logdetails["created_date"][0]) + "OpenAI response:\n"+fdata

#streamlit download button
st.download_button('Download', download_data, file_name="openai_result.txt")

