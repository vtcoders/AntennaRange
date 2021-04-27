#!/usr/bin/env python3

import cgi, cgitb, sys

form = cgi.FieldStorage()

filepath = "../../.local/lib/python3.6/site-packages"
sys.path.append(filepath)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["experiements"]


experiments = mycol.find({})

def print_experiments(experiments):
    for i in experiments:
        print(""" <li> <a href="#">""" + i['ExperimentName'] + " | " + i['Date'] + " | " + i['Facilitator'] + " | " + i['AntennaType'] + """</a></li> """)
    


print("""Content-type: text/html\n""")
print("""<html>
    <head>
        <link rel="stylesheet" href="../AntennaRangeWebpage/ExperimentLibrary/libformat.css">
        <script src="https://code.jquery.com/jquery-1.10.2.js"></script>

      <ul id="navigationBar" class="navBar sticky">
          <li class="navButton header">Antenna Range Project</li>
          <li class="navButton header"></li>
          <li class="navButton"><a href="../index.html">Home</a></li>
          <li class="navButton"><a href="../AboutPage/aboutPage.html">About</a></li>
          <li class="navButton"><a href="../ExperimentLaunch/experimentLaunchPage.html">Launch</a></li>
          <li class="navButton active"><a href="../ExperimentLibrary/eLibrary.html">Library</a></li>
          <li class="navButton"><a href="../AntennaModels/models.html">Models</a></li>
          <li class="navButton"><a href="../ExternalResources/ExternalResources.html">Resources</a></li>
          <li class="login" class="navButton "><a href="../login/login.html">Login</a></li>
      
      </ul>
        
    </head>
    <body>
        <main>
            <div class="title" style="color:#333;background-color:white;">
                <h3>Experiment Library 
                  <form action="../../cgi-bin/compareExperiments.cgi">
                    <input class= "compare" type="submit" value="Compare Experiments" />
                  </form>
                </h3>
                <div class="underline" style="background-color:#CF4520;color:rgb(238, 238, 238);"><br></div>
                <p> Experiments are listed in order from most recent to least recent.</p>
                
                <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for Experiment..">

                <ul id="myUL">
""")

print_experiments(experiments)

print("""
                    
                  
                </ul>
                       
            </div>

            <script>
                function myFunction() {
                  // Declare variables
                  var input, filter, ul, li, a, i, txtValue;
                  input = document.getElementById('myInput');
                  filter = input.value.toUpperCase();
                  ul = document.getElementById("myUL");
                  li = ul.getElementsByTagName('li');
                
                  // Loop through all list items, and hide those who don't match the search query...
                  for (i = 0; i < li.length; i++) {
                    a = li[i].getElementsByTagName("a")[0];
                    txtValue = a.textContent || a.innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                      li[i].style.display = "";
                    } else {
                      li[i].style.display = "none";
                    }
                  }
                }
                </script>


        </main>

        <footer>
        </footer>
    </body>
</html>

""")
