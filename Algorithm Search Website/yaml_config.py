#yaml_config - has functions to set, get and write from an yaml file
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

#open yaml file and load data into config object
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

#returns authenticator object
def get_auth():
    #streamlit authenticator is set with parameters
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    return authenticator

#returns config object
def get_config():
    return config

#write yaml file with new changes
def write_yaml(newconfig):
    with open('config.yaml', 'w') as file:
        yaml.dump(newconfig, file, default_flow_style=False)
                
# returns new email value of the user
def updateyaml_email(username):
    newemail = config['credentials']['usernames'][username]['email']
    return newemail

# returns new name value of the user
def updateyaml_name(username):
    newname = config['credentials']['usernames'][username]['name']
    return newname

# returns new password value of the user
def updateyaml_password(username):
    newpwd = config['credentials']['usernames'][username]['password']
    return newpwd