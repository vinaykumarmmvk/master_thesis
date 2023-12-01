#update password - webpage to change current user password
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
from header import navbar #customized navigation bar
from yaml_config import get_config #to get configuration details needed for authentication
from yaml_config import get_auth #to get authenticator object with cookies fetched from config file
from db_config import update_password #function to update new password in user table
from yaml_config import updateyaml_password #function to get updated new password from yaml file
from yaml_config import write_yaml #to write new configuration into yaml file

username = navbar("update_password")#pass the header function with search as page name

# login and password change page using streamlit authentication

authenticator = get_auth() #to get authenticator object with cookies fetched from config file
config = get_config() #to get configuration details needed for authentication

#check if user is logged in
if username != "":
    try:
        #streamlit authenticator to reset password
        if authenticator.reset_password(username, 'Change password'):
            write_yaml(config) #write configuration changes into yaml file
                
            newpwd = updateyaml_password(username) #get updated email value by passing username
            update_query = update_password(newpwd, username)  #update password in user table

            #streamlit success message to show password changed
            st.success('Password modified successfully')
    
    #Exception handler for reset password
    except Exception as e:
        st.error(e)    

#session expired
else:
     st.warning("Session expired please login again!")