#edit profile page - webpage to edit user details
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
from header import navbar #customized navigation bar
from db_config import dbinit #To initialize mysql connection parameters
from yaml_config import get_config #to get configuration details needed for authentication
from yaml_config import get_auth #to get authenticator object with cookies fetched from config file
from yaml_config import updateyaml_email #to get updated yaml file with new email value
from yaml_config import updateyaml_name #to get updated yaml file with new name value
from yaml_config import write_yaml #to write new configuration into yaml file

username = navbar("edit_profile")#pass the header function with edit profile as page name

mydb = dbinit() #intialization of db parameters

cursor = mydb.cursor()#Creating a cursor object using the cursor() method to execute mysql query

authenticator = get_auth() #to get authenticator object with cookies fetched from config file
config = get_config() #to get configuration details needed for authentication

#check if user is logged in 
if username is not None:
        try:
            #to update user details
            if authenticator.update_user_details(username, 'Edit user details'):
                write_yaml(config) #write configuration changes into yaml file

                newemail = updateyaml_email(username) #get updated email value by passing username
                newname = updateyaml_name(username) #get updated name value by passing username

                #execute mysql update query with data entered as parameters
                cursor.execute("Update users set user_fullname = '%s',email = '%s' where user_name = '%s'"%(newname, newemail, username))
                mydb.commit() #commit added data into database 
                
                st.success('Entries updated successfully')#streamlit success message

        #exception handling
        except Exception as e:
            st.error(e)    