#search algorithm - webpage to search for algorithm and show result
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
import pandas as pd #Data analysis library, to analyze results from mysql script
from datetime import datetime #To get date and time
from header import navbar #customized navigation bar
from db_config import dbinit #To initialize mysql connection parameters

navbar("search_algorithm")#pass the header function with search algorithm as page name

from db_config import get_extensionid #to get extension id from extension name
from db_config import get_extensionname #to get extension name from extension id
from db_config import fetchall_extensiontypes #to fetch all extension names

from page_redirect import open_page #redirect to url on button click
from agstyler import PINLEFT, PRECISION_TWO, draw_grid #to draw an responsive table

#button css style with margin top
from header import buttonstyle 
buttonstyle()

mydb = dbinit() #intialization of db parameters

cursor = mydb.cursor()#Creating a cursor object using the cursor() method to execute mysql query

#insert query of user searched data into searchData table
add_data = ("INSERT INTO searchData "
               "( searched_for, result_exists , extension_id, search_date) "
               "VALUES (%s, %s, %s, %s)")

#initialize result exits of user searched algorithm to false
result_exists = 0

#options_id fetch id from table of respective programming lang
option_ids = []

@st.cache_data
def addsearchdata(pname, res_exists, curr_dateTime):
    # This function will only be run the first time it's called
       
    for x in option_ids:
            if len(option_ids) > 0 :
                search_data = (pname, res_exists, str(x), curr_dateTime)
                cursor.execute(add_data, search_data)
                mydb.commit()

#main functionality starts here
#streamlit text input to ask user to enter program name to be searched
prog_name = st.text_input("Enter program name",key="1")

#streamlit multiselect to select from list of programming languages
options = st.multiselect( 'Please select programming language/s',
fetchall_extensiontypes(),[])

#fetch current date and time ie to register in table with searched datetime
current_dateTime = datetime.now()

#check if the user has entered the program name and selected progaramming language 
if prog_name is not '' and len(options) != 0 :

    #query to retrieve result set from table based on user entered program name and program language
    query="SELECT * FROM fileDetails WHERE file_name LIKE '%"+prog_name+"%'" +" and extension_id IN (select extension_id from extension where extension_type LIKE '%s'" % (options[0])

    #from programming lang/extension name we fetch the extension id 
    # and add it to option_ids set
    for x in options:
        if len(options) > 0 :
            query =  query+" OR extension_type LIKE '%s'" % (x)
            ext_id = get_extensionid(x)
            option_ids.append(ext_id)

    query = query + ")"
    
    #pandas to execute read query statement
    df = pd.read_sql(query, mydb)

    #initalize programList to empty
    progList = []

    #from extension_id in the result set, get the extension_name of it
    #, add it to progList and create a new column in resultset and add the same
    if len(df) > 0:
        for x in range(len(df)):  
            ext_name = get_extensionname(df['extension_id'][x])
            progList.append(ext_name)

    df['PL'] = progList

    #formatter to modify default table column names
    #and to specify the width of each column
    formatter = {
        'file_name': ('File Name', {'width': 120}),
        'PL': ('Prog lang', {'width': 100}),
        'created_date': ('Created date', {'width': 120})
    }
    
    if len(df) > 0:
        result_exists = 1
        
        #function to draw table with checkbox, 
        #height specified and other parameters intialized
        data = draw_grid(
            df.head(20),
            formatter=formatter,
            fit_columns=True,
            selection='single',  # or 'single', or None
            use_checkbox='True',  # or False by default
            max_height=300
        )
        
        #once option selected from the result set,
        #then user can view the algorithm code of the selected row. 
        if len(data.selected_rows) > 0:
            if st.button("View"):
                file_name = data.selected_rows[0]["file_name"]
                open_page("../view_program?key1="+file_name)
    
    # if the result does not exists in database,
    # the user is shown with below warning and OpenAI Search button redirecting it to OpenAI Search page
    else:
        st.warning("Result does not exists!")
        if st.button("OpenAI Search"):
            open_page("../openAISearch")

    #add searched data to searchData table
    addsearchdata(prog_name, result_exists, current_dateTime) 

#close cursor and database connection
cursor.close()
mydb.close()