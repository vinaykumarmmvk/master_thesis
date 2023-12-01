#OpenAI Search - Search result using OpenAI
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import openai # to use openai functions
import streamlit as st  # pip install streamlit, framework
from header import navbar #customized navigation bar
from datetime import datetime #To get date and time
from db_config import dbinit #To initialize mysql connection parameters
import random #to generate random value
import string #to use string variables and function
from concurrent.futures import ThreadPoolExecutor #useful for thread handling

navbar("openai_search")#pass the header function with search as page name

#openai.api_key = "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"
#openai key generated in openai website
openai.api_key = "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"

mydb = dbinit() #intialization of db parameters

cursor = mydb.cursor() #Creating a cursor object using the cursor() method to execute mysql query

#insert query to add data into fileDetails table
add_filequery = ("INSERT INTO fileDetails "
               "( file_name, file_description, user_id , extension_id, file_data, created_date) "
               "VALUES (%s, %s, 1, 8, %s, %s)")

# function to process request by calling openai function
def call_openai_api(chunk):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "PASS IN ANY ARBITRARY SYSTEM VALUE TO GIVE THE AI AN IDENITY"},
            {"role": "user", "content": f"OPTIONAL PREPROMPTING FOLLOWING BY YOUR DATA TO PASS IN: {chunk}."},
        ],
        max_tokens=1750,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0]['message']['content'].strip()

#function to split the text and process them parallel
def split_into_chunks(text, tokens=1500):
    words = text.split()
    chunks = [' '.join(words[i:i + tokens]) for i in range(0, len(words), tokens)]
    return chunks

#function to process the input text
def process_chunks(input_text):
    chunks = split_into_chunks(input_text)
    
    # Processes chunks in parallel
    with ThreadPoolExecutor() as executor:
        responses = list(executor.map(call_openai_api, chunks))

    return responses[0]

#get the input from user to be searched by openai
search_txt = st.text_input("Please enter detailed description of what you are looking for:")

#once user clicks on view button by submitting input text
if st.button('View'):
        
        #generate random file name
        fname = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        fname = "OpenAI_"+fname
        
        fdata = process_chunks(search_txt)
        st.write("Result:")
        st.write(fdata) #display search result to the user
        file_blob = fdata.encode('UTF-8') #convert result to blob file 
        
        current_dateTime= datetime.now() #get current date and time
        file_data = (fname, search_txt, file_blob, current_dateTime) #parameter values of file data to added    
        cursor.execute(add_filequery, file_data) #execute mysql insert query
        mydb.commit() #commit the changes to database
        cursor.close() #close cursor connection
        mydb.close() #close database connection
