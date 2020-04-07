"""
Author: Arijit Ghosh(sirpentagon@gmail.com)
Module: Showing how to install package inside AWS lambda, without creating Lambda Layer or Deployment packages. Here I have shown using request and Pandas module as an example.
Date: 7th April, 2020
"""

import os
import sys
import subprocess

def install(package):
    subprocess.check_call(["python", '-m', 'pip', 'install', package, "-t", "."])


def lambda_handler(event, context):
    # print (os.listdir(r"/tmp"))

    #Append temp to system path
    sys.path.append(r"/tmp")
    
    #Change dir and install required packages
    os.chdir(r"/tmp")
    print ("Installing gitpython........") 
    install('requests')
    install('pandas')
    # print (os.listdir(r"/tmp"))
    
    #Check all your packages present
    print (subprocess.check_call(["python", '-m', 'pip', 'freeze']))
    
    # Now import and work :)
    import requests
    r = requests.get('https://google.com')
    print (r.status_code)
    
    import pandas as pd
    data = ['Arijit', 'Ghosh']
    df = pd.DataFrame(data)
    print(df)