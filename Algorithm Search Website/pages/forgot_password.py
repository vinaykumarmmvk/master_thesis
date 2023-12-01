#forgot password - webpage to get recovery password
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
import smtplib #SMTP client session object that can be used to send mail 
from email.mime.text import MIMEText #MIME type is a standard data type in the body of an email
from header import navbar #customized navigation bar
from yaml_config import get_config #to get configuration details needed for authentication
from yaml_config import get_auth #to get authenticator object with cookies fetched from config file
from db_config import update_password #function to update new password in user table
from yaml_config import updateyaml_password #function to get updated new password from yaml file
from yaml_config import write_yaml #to write new configuration into yaml file

username = navbar("forgot_password")#pass the header function with forgot password as page name

#function to send email with new recovery password to requested user's email
def sendemail(email_receiver, new_password):
    try:
                email_sender= "manjunath.vinay2@gmail.com" #admin's emailid
                subject = "Algorithm Search user password recovery"
                pwd = "mtxm mnsh xlhz wfrk" #gmail app authentication code
                bodyContent = "Please find your recovery password  : "+new_password

                #MIME type is a standard data type in the body of an email
                msg = MIMEText(bodyContent)
                msg['From'] = email_sender
                msg['To'] = email_receiver
                msg['Subject'] = subject

                # smtp server object created with host as gmail and port number 587 
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_sender, pwd)
                server.sendmail(email_sender, email_receiver, msg.as_string())
                server.quit()

                st.success('Email sent successfully!')
                
    except Exception as e:
                st.error(f"Error log in mail : {e}")


#main functionality starts here

authenticator = get_auth() #to get authenticator object with cookies fetched from config file
config = get_config() #to get configuration details needed for authentication

try:
    #streamlit authenticator to get new recovery password
    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password('Forgot password')
    
    #if entered user name exits
    if username_of_forgotten_password:
        
        #streamlit write to show user name
        st.write("user name "+username_of_forgotten_password)
       
        write_yaml(config) #write configuration changes into yaml file
        
        newpwd = updateyaml_password(username_of_forgotten_password) #get updated email value by passing username
        update_query = update_password(new_random_password, username_of_forgotten_password) #get updated name value by passing username

        # Random password to be sent to user securely
        sendemail(email_of_forgotten_password, new_random_password)
        
    else:
        #if username not entered
        if username_of_forgotten_password == None:
             st.warning("Please enter Username") #streamlit warning message to request user to enter user name
        else:
            # if username does not exists in the user table
            st.error('Username not found')

#exception handle in case of any exceptions
except Exception as e:
    st.error(e) #streamlit to show error message

#streamlit markdown to show html hyperlink
st.markdown("""
    <a href="/forgot_username" target = "_self"> 
        Forgot Username 
    </a>
""", unsafe_allow_html=True)

