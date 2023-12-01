#user profile - webpage to show user details
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
from header import navbar #customized navigation bar
import pandas as pd #Data analysis library, to analyze results from mysql script
from db_config import dbinit #To initialize mysql connection parameters
from page_redirect import open_page #to redirect to url after button click

username = navbar("user_profile")#pass the header function with search as page name

mydb = dbinit() #intialization of db parameters

#check if user is loggedin 
if username is not None:
    #read user details from users table
    query = "Select * from users where user_name is '%s"
    df = pd.read_sql("select * from users where user_name = '%s'"% (username), mydb)  

    #Display user details
    st.write("User Name: "+username)
    st.write("Full name: "+df['user_fullname'][0])
    st.write("Email: "+df['email'][0])

    #to edit user details
    if st.button("Edit Details"):
        open_page("/edit_profile")

    #to change current password
    if st.button("Change Password"):
        open_page("/update_password")