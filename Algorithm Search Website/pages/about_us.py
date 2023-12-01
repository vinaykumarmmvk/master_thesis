#about us page - details about the website developer
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
from header import navbar #customized navigation bar

username = navbar("about_us")#pass the header function with about as page name

#create 3 columns - col1 for image, mid is separator, col2 for text
col1, mid, col2 = st.columns([1,2,20])
with col1:
    st.write("#") #to give space
    st.image('dp_vinay.jpeg', width=100)
with col2:
    st.subheader("Vinay Kumar")#streamlit subheader component
    st.write("Masters student at Hof university")#streamlit component to write into webpage
    st.write("During my Master's thesis, I built algorithm search website. ")
    st.write("This project allowed me to gain knowledge in website development and optimizing code.")
    st.write("Email: mmvinaykumar.mm@gmail.com")

st.write("#") #to give space

#create 4 columns - col11 for image, mid1 is separator, col21 for text, col31 for margin
col11, mid1, col21, col31 = st.columns([5,1,20,20])
with col11:
    st.image('prof_Lano.jpg', width=90)
with col21:
    st.subheader("Prof. Dr. Ralph Lano")#streamlit subheader component
    st.write("Professor of Internet and Media Applications")
    st.write("Throughout the completion of my thesis, Prof. Lano has been instrumental \n in providing me with fresh ideas and valuable guidance.")