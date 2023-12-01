#forgot username - webpage to get username
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
from header import navbar #customized navigation bar
from yaml_config import get_config #to get configuration details needed for authentication
from yaml_config import get_auth #to get authenticator object with cookies fetched from config file

username = navbar("forgot_username")#pass the header function with forgot username as page name

authenticator = get_auth() #to get authenticator object with cookies fetched from config file
config = get_config() #to get configuration details needed for authentication

try:
    #streamlit authenticator to get username
    username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username('Forgot username')
    
    #check if username exists in users table
    if username_of_forgotten_username:
        #username found and streamlit write to display username
        st.write("Please find your username - "+username_of_forgotten_username)
        
    else:
        #check if user entered email
        if len(email_of_forgotten_username) == 0:
             st.warning("Please enter Email")

        #if user email is is not found in users table
        else:
            st.error('Email not found')

#exception handler in case of any error
except Exception as e:
    st.error(e)