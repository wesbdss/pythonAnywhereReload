import requests
import os 
from dotenv import load_dotenv
import asyncio
import threading
import datetime
load_dotenv()

#print(os.getenv("python_anywhere_email"))
#print(os.getenv("python_anywhere_password"))
url = "https://www.pythonanywhere.com/"
token = os.getenv("python_anywhere_api_token")
username = os.getenv("python_anywhere_username")
domain_name = os.getenv("python_anywhere_domain_name")

def reload_webapp():
    response = requests.post('{url}/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(username=username,url=url,domain_name=domain_name),headers={'Authorization': 'Token {token}'.format(token=token)})
    print(response.content)
    last_register = datetime.datetime.now()
    requests.post('{url}/api/v0/user/{username}/webapps/{domain_name}/disable/'.format(username=username,url=url,domain_name=domain_name),headers={'Authorization': 'Token {token}'.format(token=token)})
    while True:
        if datetime.datetime.now() > last_register + datetime.timedelta(days=31):
            last_register = datetime.datetime.now()
            response = requests.post('{url}/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(username=username,url=url,domain_name=domain_name),headers={'Authorization': 'Token {token}'.format(token=token)})
            print("AutoReload: ", response.content)
            
        
t = threading.Thread(target=reload_webapp)
t.start()
