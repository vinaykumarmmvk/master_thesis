#home - details about the website
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
from header import navbar #customized navigation bar

username = navbar("home")#pass the header function with home as page name

st.subheader("Algorithm search website")

#create 3 columns - col1 and col2 for space, content_col for text 
col1 ,content_col, col2 = st.columns([1,20,1])
with content_col:
    st.write("A website that provides all the algorithms in different programming languages is a useful tool for developers. It allows developers to add and share their algorithms with other users. They can also develop new algorithms or upgrade the existing ones to improve their efficiency. If a user is searching for an algorithm that doesn't exist, developers can help the user add it to the website. ")
    st.write("The website provides a user interface (UI) to search for algorithms in various programming languages. If the algorithm is unavailable in the database, the user is redirected to the ChatGPT search result. The algorithm code is stored in a table as a BLOB file. ")
    st.write("When the user searches for a specific algorithm language, they are redirected to a view page with different programming languages. The user can download the code from this page. All search data is recorded in the database so that developers/admins can check which algorithms have no existing results in the database. They can then add the code for those missing algorithms.")
    st.write("Github link - https://github.com/vinaykumarmmvk/codeSearch")