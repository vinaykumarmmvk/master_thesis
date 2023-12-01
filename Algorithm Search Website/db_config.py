#db_config - database intial configuration and mysql statements to get or set values into tables
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import mysql.connector #mysql connector to initialize database connection
import pandas as pd #Data analysis library, to analyze results from mysql script

#initialize mysql database connection with initial parameters 
def dbinit():
	mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "codesearch"
	)
	return mydb
	
#function to get extensionid from extension name in extension table
def get_extensionid(extension_name):
	mydb = dbinit()
	#fetch extension id from extension type
	df_extIds = pd.read_sql("select extension_id from extension where extension_type like '%s'"% (extension_name), mydb)
	ext_id = df_extIds['extension_id'][0]
	return ext_id

#function to get extension name from extensionid in extension table
def get_extensionname(extension_id):
	mydb = dbinit()
	df_extension = pd.read_sql("select extension_type from extension where extension_id = '%s'"% (extension_id), mydb)
	ext_name = df_extension['extension_type'][0]
	return ext_name

#function to get userid from user name in users table
def get_userid(user_name):
	mydb = dbinit()
	userId = (pd.read_sql("select user_id from users where user_name = '%s'"% (user_name), mydb))['user_id'][0]
	return userId

#function to get user skilled programming languges from userid in userTodo table
def retrieve_userskills(userId):
	mydb = dbinit()
	skill_set = []
	df = pd.read_sql("select extension_type from extension where extension_id IN (select extension_id from userTodo where user_id = '%s')"% (userId), mydb)
	for index in range(df['extension_type'].size):
		value = df['extension_type'][index]
		skill_set.append(value)
	return skill_set

#function to get all extension ids from extension table
def fetchall_extensionids():
	mydb = dbinit()
	#fetch extension id from extension type
	df_extIds = pd.read_sql("select extension_id from extension", mydb)
	ext_ids = []
	for x in range(len(df_extIds)-1): 
		ext_id = df_extIds['extension_id'][x]
		ext_ids.append(ext_id)
	return ext_ids

#function to get all extension names from extension table
def fetchall_extensiontypes():
	mydb = dbinit()
	#fetch extension id from extension type
	df_types = pd.read_sql("select extension_type from extension", mydb)
	ext_types = []
	for x in range(len(df_types)-1): 
		ext_type = df_types['extension_type'][x]
		ext_types.append(ext_type)
	return ext_types

#function to update new password in user table
def update_password(newpwd, username):
	mydb = dbinit()
	cursor = mydb.cursor()
	update_query = cursor.execute("Update users set user_password = '%s' where user_name = '%s'"%( newpwd, username))
	mydb.commit()
	cursor.close()
