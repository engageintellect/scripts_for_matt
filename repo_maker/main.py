#!/usr/bin/env python3


import os
import subprocess
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

    
    ###################
    # INIT WEB-DRIVER #
    ###################

##=[ headless driver ]=# <--- MAKES BROWSER RUN SILENTLY IN THE BACKGROUND

#from selenium.webdriver.chrome.options import Options
#options = Options()
#options.add_argument('--headless')
#driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')

#=[ regular driver ]=# <--- MAKES BROWSER RUN IN FOREGROUND

driver = webdriver.Chrome()
driver.implicitly_wait(10)

    
    ###########
    # DISPLAY #
    ###########

def clear_display():
    os.system('clear')
    os.system('figlet github repo')
    print("\n")

clear_display()



    ###################
    # LOGIN TO GITHUB #
    ###################

##=[ github account info ]=#
user = subprocess.getoutput('echo $USER')
username = input("GITHUB USERNAME: ")
password = input("GITHUB PASSWORD: ")


clear_display()

driver.get("https://www.github.com/login")
driver.find_element_by_id("login_field").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("commit").click()


    ###################
    # CREATE NEW REPO #
    ###################

try:
    repo_name = sys.argv[1]
    print(f'REPO NAME: {repo_name}')
except:
    repo_name = input("REPO NAME: ")
finally:
    repo_description = input("REPO DESCRIPTION: ")
    repo_visability = input("PUBLIC OR PRIVATE REPO: ")
    if repo_visability.lower() == "private":
        driver.find_element_by_id("repository_visibility_private").click()


driver.get("https://www.github.com/new")
driver.find_element_by_name("repository[name]").send_keys(repo_name)
driver.find_element_by_name("repository[description]").send_keys(repo_description)
repo_address = str(driver.current_url)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable \
        ((By.CSS_SELECTOR, "button.btn.btn-primary.first-in-line"))).click()
    

    #############################
    # LINK LOCAL REPO TO REMOTE #
    #############################


#=[ local repo path ]=#
local_repo_path = input("ENTER LOCAL REPO PATH: ")
if local_repo_path == "":
    os.chdir(f'/home/{user}')
    os.mkdir(repo_name)
    os.chdir(repo_name)

else:
    print(os.getcwd())
    os.chdir(f"{local_repo_path}")


#=[ initialize local repository ]=#
os.system('git init')

# remote add repository
repo_address = f'https://github.com/{username}/{repo_name}.git'
os.system(f'git remote add origin {repo_address}\n')


    ######################
    # COMPLETION MESSAGE #
    ######################


#=[ add repo address to clipmenu ]=#
repo_address = str(driver.current_url)
os.system(f'echo {repo_address} | xclip')

print(f'GitHub repository "{repo_name}" has been created.')
print(f"Repository address: {repo_address}\n")

print(f'REPO "{repo_name}" SUCCESSFULLY CREATED, INITIALIZED, AND ADDED TO REMOTE BRANCH.')
print(f'READY FOR FIRST COMMIT...\n')


