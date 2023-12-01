#header - consists mainly of navigation bar and header styles to be set
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
#Streamlit html component to execute html type
from streamlit.components.v1 import html
import time

#getter and setter of username
def setusername(val):
    global username
    username = val

def getusername():
    try:
        return username 
    except Exception as e:
        return ""
    
#function to add navigation bar to the web page
def navbar(page):
    #streamlit page configuration in order to close default navigation bar and wide layout
    st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

    time.sleep(1)#page takes some time to close the default sidebar, so the delay is applied
    
    headerstyle()
    usrname = getusername()
    
    #check if user is loggedin or loggedout
    if usrname != "":
        navbar_loggedIn(page)

    else:
        navbar_loggedOut(page)

    setheader(page)
    return usrname

#function to set streamlit header based on the page name
def setheader(pagename):
    match pagename:
        case "about_us":
            st.header("About Us")

        case "add_program":
            st.header("Add Algorithm")

        case "edit_profile":
            st.header("Edit Profile")

        case "edit_program":
            st.header("Edit Algorithm")

        case "forgot_passoword":
            st.header("Forgot Password")

        case "forgot_username":
            st.header("Forgot Username")

        case "logout":
            st.header("Logout")

        case "signup":
            st.header("SignUp")

        case "openai_search":
            st.header("OpenAI Search")

        case "search_algorithm":
            st.header("Search Algorithm")

        case "search_logs":
            st.header("Search Logs")

        case "todo_program":
            st.header("Todo Program")

        case "todo_search":
            st.header("Todo Search")

        case "update_password":
            st.header("Update Password")

        case "user_profile":
            st.header("User Profile")

        case "view_ailog":
            st.header("View OpenAI Log")

        case "view_log":
            st.header("View Log")

        case "home":
            st.header("Home")
    
#header style with margin bottom
def headerstyle():
    st.markdown("""
    <style>
        iFrame{
        margin-bottom : -140px;           
        }          
    </style>""", unsafe_allow_html=True)

#buttonstyle with margin top for better alignment
def buttonstyle():
    st.markdown("""
    <style>
    .row-widget.stButton {
        margin-top: 140px;
    }</style>""", unsafe_allow_html=True)
    
#navigation bar style properties set
def setnavbarstyle():
    navbarstyle ="""
    <style>
    body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    }

    .topnav {
    overflow: hidden;
    background-color: #333;
    }

    .topnav a {
    float: left;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 50px;
    text-decoration: none;
    font-size: 18px;
    }

    .topnav a:hover {
    background-color: #ddd;
    color: black;
    }

    .topnav a.active {
    background-color: #04AA6D;
    color: white;
    }

    h2 {
    margin-top: -120px;
    }

    </style>
    </head>
    """
    return navbarstyle

#navigation bar javascript properties of loggedout user
def navbarjs_loggedOut():
    js_code ="""
    var home_ele = document.getElementById("home");
    var about_ele = document.getElementById("about");
    var search_ele = document.getElementById("search");
    var login_ele = document.getElementById("login");

    switch(curr_page){
        case "home":
            home_ele.classList.add("active");
            break;

        case "about_us":
            about_ele.classList.add("active");
            break;

        case "search_algorithm":
            search_ele.classList.add("active");
            break;

        case "login":
            login_ele.classList.add("active");
            break;

    }

    </script>
    """
    return js_code

#navigation bar of loggedout user
def navbar_loggedOut(page):
    navbarstyle = setnavbarstyle()
    nav_links =f"""
    <div class="topnav">
    <a id="home" href="/home" target="_target">Home</a>
    <a id="about" href="/about_us" target="_target">About Us</a>
    <a id="search" href="/search_algorithm" target="_target">Search Algorithm</a>
    <a id="login" href="/login" target="_target">Log In</a>
    </div>
    <script>
    var curr_page = "{page}";
    """

    js_code = navbarjs_loggedOut()

    html(navbarstyle+nav_links+js_code)

#navigation bar javascript properties of loggedin user
def navbarjs_loggedIn():
    js_code ="""
    var home_ele = document.getElementById("home");
    var about_ele = document.getElementById("about");
    var search_ele = document.getElementById("search");
    var searchlogs_ele = document.getElementById("searchlogs");
    var todosearch_ele = document.getElementById("todosearch");
    var profile_ele = document.getElementById("profile");
    var logout_ele = document.getElementById("logout");

    switch(curr_page){
        case "home":
            home_ele.classList.add("active");
            break;

        case "about":
            about_ele.classList.add("active");
            break;

        case "search_algorithm":
            search_ele.classList.add("active");
            break;

        case "searchlogs":
            searchlogs_ele.classList.add("active");
            break
            
        case "todo":
            todosearch_ele.classList.add("active");
            break
            
        case "profile":
            profile_ele.classList.add("active");
            break
        
        case "logout":
            logout_ele.classList.add("active");
            break;

    }

    </script>
    """
    return js_code

#navigation bar of loggedin user
def navbar_loggedIn(page):

    navbarstyle = setnavbarstyle()

    nav_links =f"""
    <div class="topnav">
    <a id="home" href="/home" target="_target">Home</a>
    <a id="about" href="/about_us" target="_target">About Us</a>
    <a id="search" href="/search_algorithm" target="_target">Search Algorithm</a>
    <a id="searchlogs" href="/search_logs" target="_target">Search Logs</a>
    <a id="todosearch" href="/todo_search" target="_target">Todo</a>
    <a id="profile" href="/user_profile" target="_target">Profile</a>
    <a id="logout" href="/logout" target="_target">Log Out</a>
    </div>
    <script>
    var curr_page = "{page}";
    """
    js_code = navbarjs_loggedIn()

    html(navbarstyle+nav_links+js_code)

