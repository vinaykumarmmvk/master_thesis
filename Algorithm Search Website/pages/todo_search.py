#todo search - list of algorithms not in database to be added by the user 
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit as st #streamlit framework alias as st
import pandas as pd #Data analysis library, to analyze results from mysql script
from agstyler import PINLEFT, PRECISION_TWO, draw_grid #to draw an responsive table
from page_redirect import open_page #redirect to url on button click
from header import navbar #customized navigation bar
from db_config import dbinit #To initialize mysql connection parameters
from db_config import fetchall_extensiontypes #to fetch all extension names
from db_config import get_extensionid #to get extension id from extension name
from db_config import get_extensionname #to get extension name from extension id
from db_config import get_userid #function to get userid
from db_config import retrieve_userskills #function to get user skillset

username = navbar("todo_search")#pass the header function with search as page name

username = "vkumarmm"
mydb = dbinit() #intialization of db parameters

#Retrieve user Id from username 
userId = get_userid(username) 

cursor = mydb.cursor()#Creating a cursor object using the cursor() method to execute mysql query

#insert query of user data into userTodo table
add_query = ("INSERT INTO userTodo (user_id , extension_id) VALUES (%s, %s)")

#skill set is initialized to empty list
skill_set = []

#fetch skill set of user and add it to list
skill_set = retrieve_userskills(userId)

#get all extension types
options = fetchall_extensiontypes()
#options selected initialized to empty list
options_selected = []
for i in range(len(skill_set)):
    for j in range(len(options)):
        #some skill set that are not there in the users skill set 
        #and then remove it from options set is user already has that skill set
        if skill_set[i] == options[j]:
            options.remove(skill_set[i])
            break


st.write("Your skill set:")
all_skillset = ""
for i in range(len(skill_set)):
     if i == 0:
        all_skillset = skill_set[i]
     else:
        all_skillset = all_skillset+", "+skill_set[i]

st.write(all_skillset)

#streamlit multiselect of options for user to add new skill set
options_selected = st.multiselect( 'Please select programming language/s', options,[])

#if an option is selected, check if the button is clicked
#then add the selected option to the user skill set
if len(options_selected) != 0:
    if st.button("Add Skill"):
        #option id initialized to empty set
        option_ids = []

        # get extension id of each selected option  
        # and add it to the option_ids set
        for i in range(len(options_selected)):
                skill_set.append(options_selected[i])
                x = options_selected[i]
                ext_id = get_extensionid(x)
                option_ids.append(ext_id)

                #update user skill set in database, execute query
                #and commit it to database
                add_data = (str(userId), str(option_ids[i]))
                cursor.execute(add_query, add_data)
                mydb.commit()

#if user has skill set then fetch search logs from searchData table,
#for which the result does not exists in database. So that user can add it. 
if len(skill_set)!=0:
    for i in range(len(skill_set)): 
        var = skill_set[i]
        extensionid = get_extensionid(var)  
        if i == 0:
            todo_query = "select * from searchData where result_exists = 0 and (extension_id  = '%s' "% extensionid
        else:
            todo_query = todo_query + " or extension_id  = '%s' "% extensionid
    todo_query = todo_query + ")"

    todo_set = pd.read_sql(todo_query, mydb)

    #programming language/skill set initialized to empty set
    progList = []

    #fetch the extension_id from the result set, get the extension_name from extension_id
    # and then add it into progList
    if len(todo_set) > 0:
        for x in range(len(todo_set)):  
            ext_name = get_extensionname(todo_set['extension_id'][x])
            progList.append(ext_name)

        #create a new column PL(Programming Language) in the result set intialized with progList 
        todo_set['PL'] = progList
        
        #formatter to modify default table column names
        #and to specify the width of each column
        formatter = {
        'searched_for': ('Program Name', {'width': 80}),
        'PL': ('Prog lang', {'width': 50}),
        'search_date': ('Search date', {'width': 120})
        }

        #function to draw table with checkbox, height specified and other parameters intialized
        data = draw_grid(
            todo_set.head(20),
            formatter=formatter,
            fit_columns=True,
            selection='single',  # or 'single', or None
            use_checkbox='True',  # or False by default
            max_height=300
        )
        
        #once option selected from the result set,
        #then user can add the algorithm code of the selected row. 
        if len(data.selected_rows) > 0:
            prog_name = data.selected_rows[0]["searched_for"]
            prog_lang = data.selected_rows[0]["PL"]
            open_page("../todo_program?key1="+prog_name+"&&key2="+prog_lang)

#close database connection 
mydb.close()


