#!/usr/bin/env python3

import cgi, cgitb, sys

form = cgi.FieldStorage()

name = form.getvalue('name')
username = form.getvalue('uname')
password = form.getvalue('psw')

# TO-DO: Validation for characters entered and length, etc.

filepath = "../../.local/lib/python3.6/site-packages"
sys.path.append(filepath)

import pymongo

def create_user(name, username, password):
    new_user = {'name':name, 'username':username, 'password':password,
    'group':'ADMIN', 'organization':'Virginia Tech'} # TO-DO fix group and organization
    return new_user

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["accounts"]

myquery = {"username": username}

account = mycol.find_one(myquery)

print("""Content-type: text/html\n""")
printString = ""
if (account != None):
  printString = "Username already exists"
  print("""<html>
    <head>
        <link rel="stylesheet" href="../AntennaRangeWebpage/signup/signup.css">

        <ul id="navigationBar" class="navBar sticky">
            <li class="navButton header">Antenna Range Project</li>
            <li class="navButton header"></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/index.html">Home</a></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/AboutPage/aboutPage.html">About</a></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/ExperimentLaunch/experimentLaunchPage.html">Launch</a></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/ExperimentLibrary/eLibrary.html">Library</a></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/AntennaModels/models.html">Models</a></li>
            <li class="navButton"><a href="../AntennaRangeWebpage//ExternalResources/ExternalResources.html">Resources</a></li>
            <li class="login navButton"><a href="../AntennaRangeWebpage/login/login.html">Login</a></li>
        </ul>
    </head>
    <body> 
  
        <h2>Login Form</h2> 
        <!--Step 1 : Adding HTML-->
        <form action="./signup.cgi" method="post"> 
            <div class="imgcontainer"> 
                <img src=  "../AntennaRangeWebpage/signup/logo.png" 
                     alt="VT Logo" class="avatar"> 
            </div>
            <div class="container" style="display:inline-block;border:solid #CF4520;border-radius:15px;border-width:2.5px;margin-left:1.5%;margin-right:1.5%;">""" + printString + """</div>
            <div class="container"> 

                <label><b>Enter your name:</b></label> 
                <input type="text" placeholder="Enter Name" name="name" required> 

                <label><b>Choose a username:</b></label> 
                <input type="text" placeholder="Enter Username" name="uname" required> 
      
                <label><b>Choose a password:</b></label> 
                <input type="password" placeholder="Enter Password" name="psw" required> 
      
                <button type="submit">Create Account</button>
                <a class="login login_button" href=../AntennaRangeWebpage/login/login.html>Log In</a>
            </div> 
      
        </form>
    </body> 
    </html>
    """)
else:
    new_user = create_user(name, username, password)
    mycol.insert_one(new_user)
    printString = "Hello " + name + "! Your account has been successfully created"
    print(
    """
    <!DOCTYPE html>
    <html lang=en>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>

    <h1 style="color:white;background-color:black">""" + printString + """</h1>

    <h2>
    Thank you for logging on to the Antenna Range! This feature is yet to be fully implemented but will be soon!
    </h2>



    </body>
    </html>
    """)