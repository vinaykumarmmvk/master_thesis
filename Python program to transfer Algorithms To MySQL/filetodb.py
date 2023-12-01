#filetodb - to transfer all the algorithms into filedetails table
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import mysql.connector #mysql connector to initialize database connection
import pandas as pd #Data analysis library, to analyze results from mysql script
import streamlit as st #streamlit framework alias as st
from datetime import datetime #To get date and time
import os #To get operating system values

#mysql - initial connection parameters to be set
mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234",
                               database = "codesearch")

# alogorithm's folder path
rootpath = 'programs/'

#streamlit header of heading
st.header("file tranfer from Folder to MySQL")

#Reading blob data and converting it to str
df_data = pd.read_sql("select file_data from fileDetails where file_id = %s"% (str(8)), mydb)
fdata = df_data['file_data'][0]
st.write(fdata.decode('UTF-8'))#returns str type

progList = os.listdir(rootpath) #to read list of directories
userId = "1" #admin's userid

#add query to add algorithms into fileDetails
add_query = ("INSERT INTO fileDetails (file_name, user_id , extension_id, file_data, created_date) VALUES (%s, %s, %s, %s, %s)")

#function to get extensionid from extension_type
def getExtId(extType):
    extId = (pd.read_sql("select extension_id from extension where extension_type = '%s'"% (extType), mydb))['extension_id'][0]
    return extId

#fetch algorithms in the folder path
for prog in progList:
    fileList = os.listdir(rootpath+prog)
    st.subheader("Folder name : "+prog)
    for file in fileList:
        binaryData = ''

        # Convert digital data to binary format
        with open(rootpath+prog+"/"+file, 'rb') as fp:
            binaryData = fp.read()

        #get extension type by splitting it
        ext = file.split(".")
        extId = getExtId(ext[1])
        try:
            df = pd.read_sql("select file_id from fileDetails where extension_id = %s and file_name = '%s'"% (str(extId),prog), mydb)
            cursor = mydb.cursor()
            if df.size !=0:
                fileId = df['file_id'][0]
                df_data = pd.read_sql("select file_data from fileDetails where file_id = %s"% (str(fileId)), mydb)
                if df_data.size != 0:
                    st.write("data exists")
                else:
                    #insert binarydata into filedetails by passing fname as prog and extId
                    query = """Update fileDetails set file_data = %s where file_id = %s"""
                    cursor.execute(query ,params=(binaryData, str(fileId)))
                    st.write("File data added")
                
            else:
                st.warning("fileId not found for "+file)
                #insert entry in filedetails
                add_data = (prog, userId, str(extId), binaryData, datetime.now())
                cursor.execute(add_query, add_data)
                st.success("new row added")
            
            #commit changes
            mydb.commit()
            #close cursor connection
            cursor.close()
            st.write("Successfully tranferred file : "+file)
            
         #Handaling mysql connection exception
        except mysql.connector.Error as e:
            st.error(e)
        
        #handling keyerror wherein no other user other than admin can do this operation
        except KeyError as ke:
            st.error(ke.with_traceback)


#successfully trasfer message
st.success("Transfer complete")
#close database connection
mydb.close()

