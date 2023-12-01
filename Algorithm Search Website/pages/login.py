#login - user account login 
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch


import streamlit as st  # pip install streamlit
from header import navbar #customized navigation bar
from header import setusername # set loggedin username
from page_redirect import open_pageself # function to redirect in same tab
from yaml_config import get_config #to get configuration details needed for authentication
from yaml_config import get_auth #to get authenticator object with cookies fetched from config file

username = navbar("login")#pass the header function with login as page name

authenticator = get_auth() #to get authenticator object with cookies fetched from config file
config = get_config() #to get configuration details needed for authentication

#streamlit authenticator with login form and validator
name, authentication_status, username = authenticator.login("Login", "main")

#if authentication failed display streamlit error message
if authentication_status == False:
    st.error("Username/password is incorrect")

#if username/password not entered display streamlit error message showing the same 
if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status == True and username is not None:
    st.success("login success"+username)#display success message of loggedin user
    setusername(username) #store loggedin username in session
    open_pageself("/home") #redirect to home page after loggedin

#streamlit markdown to display html hyperlink to signup
st.markdown("""
    <a href="/signup" target = "_self"> 
        Sign Up 
    </a>
""", unsafe_allow_html=True)

#streamlit markdown to display html hyperlink to forgot password page
st.markdown("""
    <a href="/forgot_password" target = "_self"> 
        Forgot Password 
    </a>
""", unsafe_allow_html=True)