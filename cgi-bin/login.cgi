#!/usr/bin/env python3

import cgi, cgitb, sys

form = cgi.FieldStorage()

username = form.getvalue('uname')
password = form.getvalue('psw')

# TO-DO: Validation for characters entered and length, etc.

filepath = "../../.local/lib/python3.6/site-packages"
sys.path.append(filepath)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["accounts"]

myquery = {"username": username}

account = mycol.find_one(myquery)

print("""Content-type: text/html\n""")
printString = ""
if (account == None or account['password'] != password):
  printString = "Username or password is incorrect"
  print("""
  <!DOCTYPE html>
  <html lang=en>
    <head>
        <link rel="stylesheet" href="../AntennaRangeWebpage/login/login.css">

        <ul id="navigationBar" class="navBar sticky">
            <li class="navButton header">Antenna Range Project</li>
            <li class="navButton header"></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/index.html">Home</a></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/AboutPage/aboutPage.html">About</a></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/ExperimentLaunch/experimentLaunchPage.html">Launch</a></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/ExperimentLibrary/eLibrary.html">Library</a></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/AntennaModels/models.html">Models</a></li>
            <li class="navButton"><a href="../AntennaRangeWebpage/ExternalResources/ExternalResources.html">Resources</a></li>
            <li class = "login active" class="navButton active"><a href="#Login">Login</a></li>
        </ul>
    </head>
    <body> 
  
        <h2>Login Form</h2> 
        <!--Step 1 : Adding HTML-->
        <form action="./login.cgi"> 
            <div class="imgcontainer"> 
                <img src=  "../AntennaRangeWebpage/login/logo.png" 
                     alt="Avatar" class="avatar"> 
            </div> 
            <div class="container" style="display:inline-block;border:solid #CF4520;border-radius:15px;border-width:2.5px;margin-left:1.5%;margin-right:1.5%;">""" + printString + """</div>
            <div class="container"> 
                <label><b>Username</b></label> 
                <input type="text" placeholder="Enter Username" name="uname" required> 
      
                <label><b>Password</b></label> 
                <input type="password" placeholder="Enter Password" name="psw" required> 
      
                <button type="submit">Login</button>
                <a class="login signup" href=../AntennaRangeWebpage/signup/signup.html>Sign Up</a>
                
            </div> 
      
        </form> 
      
    </body> 
  </html>
  """)
else:
  printString = "Hello " + account['name'] + "! You have successfully logged in."
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