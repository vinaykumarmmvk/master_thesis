#search logs - webpage to show list of search logs of algorithms searched
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch


import streamlit as st #streamlit framework alias as st
import pandas as pd #Data analysis library, to analyze results from mysql script
from header import navbar #customized navigation bar
from db_config import dbinit #To initialize mysql connection parameters
from db_config import get_extensionid #to get extension id from extension name
from db_config import get_extensionname #to get extension name from extension id
from db_config import fetchall_extensiontypes #to fetch all extension names
from page_redirect import open_page #redirect to url on button click
from agstyler import PINLEFT, PRECISION_TWO, draw_grid #to draw an responsive table
from header import buttonstyle  #button css style with margin top

username = navbar("search_logs")#pass the header function with search as page name

buttonstyle()
mydb = dbinit() #intialization of db parameters

#streamlit radio select with option to view search logs in search algorithm page
# and search logs in OpenAI search page
search_type = st.radio(
    "Please select type of log/s",
    ('Search Page', 'OpenAI Search'))

#if user selected to view search logs in search algorithm page
if search_type == 'Search Page':
    
    #ask user for program name and programming language to be filtered from search logs
    prog_name = st.text_input("Enter program name")
    options = st.multiselect( 'Please select programming language/s',
    fetchall_extensiontypes(),[])
    
    #initialize selected option_ids to empty set 
    option_ids = []

    #write a query statement based on the user selected data to be filtered out
    query = "Select * from searchData"

    #flag initalized with 0 for the first where clause in select statement
    flag = 0
    
    #if user has entered program name
    if prog_name is not '':
        #checkbox returns true or false based on selection
        res_exists_bool = st.checkbox("Result exists")
        
        #Boolean datatype converted to 0 and 1  
        if res_exists_bool:
            res_exists = "1"
        else:
            res_exists = "0"

        if flag == 0:
            query = query + " WHERE searched_for like '%"+prog_name+"%'" 
            flag = 1
        else:
            query = query +" and searched_for like '%"+prog_name+"%'" 

        #if user wants to see the logs with  result exists or not
        query = query +" and result_exists like '%"+res_exists+"%'" 

    # if user has selected the programming language from multiselect    
    if len(options) != 0 :
        if flag == 0:
            query = query + " WHERE extension_id IN (select extension_id from extension where extension_type LIKE '%s'" % (options[0])
            flag = 1
        else:
            query = query + " and extension_id IN (select extension_id from extension where extension_type LIKE '%s'" % (options[0])

        
        for x in options:
            if len(options) > 0 :
                query =  query+" OR extension_type LIKE '%s'" % (x)
                option_ids.append(get_extensionid(x))

        query = query + ")"
   
    # execute search statement based on user selected conditions
    df_search = pd.read_sql(query, mydb)

    #if search has result set, display result
    if len(df_search) > 0:

        #intialize progList to empty list
        progList = []

        #get_extensionname from extension_id and add it to progList
        for x in range(len(df_search)):  
            ext_name = get_extensionname(df_search['extension_id'][x])
            progList.append(ext_name)

        #create a new column in result list and add the program language list
        df_search['PL'] = progList

    #formatter to modify default table column names
    #and to specify the width of each column         
    formatter = {
            'searched_for': ('Searched for', {'width': 120}),
            'result_exists': ('Result Exists', {'width': 80}),
            'PL': ('Programming Language', {'width': 80}),
            'search_date': ('Created date', {'width': 120})
    }
        
    if len(df_search) > 0:
        #function to draw table with checkbox, 
        #height specified and other parameters intialized
        data = draw_grid(
                df_search.head(1000),
                formatter=formatter,
                fit_columns=True,
                selection='single',  # or 'single', or None
                use_checkbox='True',
                max_height = 500,
                wrap_text = True,
                auto_height = True,
            )

        #once option selected from the result set,
        #then user can view log of the selected row.     
        if len(data.selected_rows) > 0:
            log_id = str(data.selected_rows[0]["search_id"])
            
            #log_id is passed as the query string to view_log page
            #check if view button was clicked
            if st.button('View'):
                open_page("/view_log?key1="+log_id) 
    
    #close database connection
    mydb.close()

#if user selected to view search logs in OpenAI search page
if search_type == 'OpenAI Search':
    st.write("openAI Search")
    #request user for search description to filter from the search logs
    search_description = st.text_input("Enter openAI Search description")

    query1= "Select * from fileDetails where file_name like 'OpenAI%' and extension_id = 8"
    
    if search_description is not '':
        query1 = query1+" and file_description like '%"+search_description+"%'"
        
    #exectue query statement and and store result in dataframe df    
    df = pd.read_sql(query1, mydb)

    #formatter to modify default table column names
    #and to specify the width of each column     
    formatter = {
            'file_name': ('File name', {'width': 120}),
            'file_description': ('Search description', {'width': 120}),
            'created_date': ('Searched date', {'width': 120})
    }
        
    if len(df) > 0:
        #function to draw table with checkbox, 
        #height specified and other parameters intialized
        data = draw_grid(
                df.head(1000),
                formatter=formatter,
                fit_columns=True,
                selection='single',  # or 'single', or None
                use_checkbox='True',  # or False by default
                max_height=300
            )

        #once option selected from the result set,
        #then user can view OpenAI log of the selected row.    
        if len(data.selected_rows) > 0:
            file_id = str(data.selected_rows[0]["file_id"])
            #file_id is passed as the query string to view_ailog page
            if st.button('View AILog'):
                open_page("/view_ailog?key1="+file_id) 

    #close database connection
    mydb.close()