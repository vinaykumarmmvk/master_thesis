show databases; #to see list of all tables 

create database codesearch; #to create new database with the name codesearch

use codesearch; #select codesearch database to perform operation on it

#create users table with below column names
CREATE TABLE users (
user_id int NOT NULL AUTO_INCREMENT,
user_name varchar(255),
user_password  varchar(255),
email varchar(255),
PRIMARY KEY (user_id)
);

#create extenstion table with below column names
create table extension (
extension_id int NOT NULL,
extension_type varchar(255),
primary key(extension_id)
);

#create fileDetails table with below column names
create table fileDetails (
file_id int NOT NULL AUTO_INCREMENT,
file_name varchar(255),
code_id int NOT NULL,
extension_id int NOT NULL,
created_date TIMESTAMP,
PRIMARY KEY (file_id),
foreign key (code_id) references programCode(code_id),
foreign key (extension_id) references extension(extension_id)
);

#create fileEditDetails table with below column names
create table fileEditDetails (
edit_id int NOT NULL AUTO_INCREMENT,
file_id int NOT NULL,
edit_description varchar(255) NOT NULL,
user_id int NOT NULL,
edited_date TIMESTAMP,
PRIMARY KEY (edit_id),
foreign key (user_id) references users(user_id),
foreign key (file_id) references filedetails(file_id)
);

#create userTodo table with below column names
create table userTodo (
todo_id int NOT NULL AUTO_INCREMENT,
user_id int NOT NULL,
extension_id int NOT NULL,
PRIMARY KEY (todo_id),
foreign key (user_id) references users(user_id),
foreign key (extension_id) references extension(extension_id)
);

#create searchData table with below column names
create table searchData (
search_id int NOT NULL AUTO_INCREMENT,
searched_for varchar(255),
result_exists boolean NOT NULL,
extension_id int NOT NULL,
search_date TIMESTAMP,
PRIMARY KEY (search_id),
foreign key (extension_id) references extension(extension_id)
);

##create openAI table with below column names
create table openAI (
openAI_id int NOT NULL AUTO_INCREMENT,
search_description varchar(255),
file_id int NOT NULL,
PRIMARY KEY AUTO_INCREMENT (openAI_id),
foreign key (file_id) references fileDetails(file_id)
);

#shows list of table within the database
show tables;

# to check if the tables were created successfully run the below scripts
# it gives you details of the created table
show create table users;
show create table extension;
show create table fileDetails;
show create table fileEditDetails;
show create table userTodo;
show create table searchData;
show create table openAI;