#logout - webpage to sign out from logged in user 
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st  # pip install streamlit
from header import navbar #customized navigation bar
from header import setusername # set loggedin username
from page_redirect import open_pageself # function to redirect in same tab
from yaml_config import get_config #to get configuration details needed for authentication
from yaml_config import get_auth #to get authenticator object with cookies fetched from config file


username = navbar("logout")#pass the header function with logout as page name

authenticator = get_auth() #to get authenticator object with cookies fetched from config file
config = get_config() #to get configuration details needed for authentication

#streamlit display confirmation message of logout 
st.write("Are you sure you want to logout?")

try:
    #if yes button clicked by user
    if st.button("Yes"):
        #reset all the variable values in session state
        st.session_state['logout'] = True
        st.session_state['name'] = None
        st.session_state['username'] = None
        st.session_state['authentication_status'] = None
        setusername("")
        #after logged out redirect to home page
        open_pageself("/home")

#exception handle to any logout issues
except Exception as e:
    st.warning(e)

#if cancel button clicked redirect to home page without logging out
if st.button("Cancel"):
    open_pageself("/home")