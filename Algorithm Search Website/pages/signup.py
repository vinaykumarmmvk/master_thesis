#signup - webpage to create new user account
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
import streamlit_authenticator as stauth #streamlit user authenticator
import yaml #to add into yaml file
from header import navbar #customized navigation bar
from db_config import dbinit #To initialize mysql connection parameters
from yaml_config import get_config #to get configuration details needed for authentication
from yaml_config import get_auth #to get authenticator object with cookies fetched from config file

navbar("signup")#pass the header function with search as page name

mydb = dbinit() #intialization of db parameters

cursor = mydb.cursor() #Creating a cursor object using the cursor() method to execute mysql query

add_data = ("INSERT INTO users "
               "( user_name, user_fullname , user_password, email) "
               "VALUES (%s, %s, %s, %s)")

authenticator = get_auth() #to get authenticator object with cookies fetched from config file
config = get_config() #to get configuration details needed for authentication

try:
    #streamlit form to ask user for details to signup
    new_username = st.text_input("Username")
    new_email = st.text_input("Email")
    new_name = st.text_input("Name")
    new_password = st.text_input("password", type="password")
    new_password_repeat = st.text_input("Repeat Password", type="password")
    
    #once user clicks on register button
    if st.button('Register'):
        
        #name is validated by streamlit authenticator
        if authenticator.validator.validate_name(new_name):
            
            #username is validated by streamlit authenticator
            if authenticator.validator.validate_username(new_username):
                
                #email is validated by streamlit authenticator
                if authenticator.validator.validate_email(new_email):        
                    
                    #if user has entered all the details then enter condition
                    if len(new_email) and len(new_username) and len(new_name) and len(new_password) > 0:
                        
                        #check if the username already exists
                        if new_username not in authenticator.credentials['usernames']:
                            
                            #check if the password entered and repeated password match
                            if new_password == new_password_repeat:
                                    
                                    #generate hashed value of the password for security
                                    new_password = stauth.Hasher([new_password]).generate()
                                    
                                    #new user is created by adding it to users table
                                    user_data = (new_username, new_name, new_password[0], new_email)
                                    cursor.execute(add_data, user_data)
                                    mydb.commit()
                                    
                                    # data is also entered into yaml file
                                    record_to_add = dict(email=new_email,name=new_name, password=new_password[0])
                                    config["credentials"]['usernames'][new_username] = record_to_add

                                    with open('config.yaml', 'w') as file:
                                        yaml.dump(config, file, default_flow_style=False)

                                    #streamlit success message that new user was registered
                                    st.success("New user registered successfully!")
                            else:
                                st.error('Passwords do not match')
                        else:
                            st.error('Username already taken')
                    else:
                        st.error('Please enter an email, username, name and password')
                else:
                    st.error("Enter valid email")
            else:
                 st.error("enter valid username")
        else:
             st.error("enter valid name")

#Exception handle in case of any error
except Exception as e:
    st.error(e)