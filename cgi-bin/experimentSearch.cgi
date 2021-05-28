#!/usr/bin/env python3

import cgi, cgitb, sys

form = cgi.FieldStorage()

filepath = "../../.local/lib/python3.6/site-packages"
sys.path.append(filepath)

experimentQuery = {"ExperimentName": {"$regex": ""},
                   "Date": {"$regex": ""},
                   "Facilitator": {"$regex": ""},
                   "AntennaType": {"$regex": ""}}

experimentName = form.getvalue('eName')
experimentDate = form.getvalue('eDate')
user = form.getvalue('uName')
antennaType = form.getvalue('aType')
filters = {"Experiment Name":experimentName, "Date":experimentDate, "Facilitator":user, "Antenna Type":antennaType}
if experimentName == None:
  experimentName = ""
if experimentDate == None:
  experimentDate = ""
if user == None:
  user = ""
if antennaType == None:
  antennaType = ""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["experiements"]

experimentQuery = {"ExperimentName": {"$regex": experimentName},
                   "Date": {"$regex": experimentDate},
                   "Facilitator": {"$regex": user},
                   "AntennaType": {"$regex": antennaType}}

experiments = mycol.find(experimentQuery)

def print_experiments(experiments):
    for i in experiments:
        print(""" <li><a><input type='checkbox' name='box' id='box' value=""" + i["FileName"] + """>""" + i['ExperimentName'] + " | " + i['Date'] + " | " + i['Facilitator'] + " | " + i['AntennaType'] + """</a></li> """)

def print_filters(filters):
  filter_found = False
  for filter in filters:
    if filters[filter] != None and isinstance(filters[filter], str):
      if not filter_found:
        print("""<div class="filterRow"><div class="filter" style="background-color:white;color:#630031;">Applied Filters:   </div>""")
        filter_found = True
      print("""<div class="filter">""" + filter + """:   """ + filters[filter] + """</div> """)
  if filter_found:
    print("""<div></div><br><br><br></div>""")


print("""Content-type: text/html\n""")
print("""<html>
    <head>
        <link rel="stylesheet" href="../AntennaRangeWebpage/ExperimentLibrary/libformat.css">
        <script src="https://code.jquery.com/jquery-1.10.2.js"></script>

      <ul id="navigationBar" class="navBar sticky">
          <li class="navButton header">Antenna Range Project</li>
          <li class="navButton header"></li>
          <li class="navButton"><a href="../AntennaRangeWebpage/index.html">Home</a></li>
          <li class="navButton"><a href="../AntennaRangeWebpage/AboutPage/aboutPage.html">About</a></li>
          <li class="navButton"><a href="../AntennaRangeWebpage/ExperimentLaunch/experimentLaunchPage.html">Launch</a></li>
          <li class="navButton active"><a href=#>Library</a></li>
          <li class="navButton"><a href="../AntennaRangeWebpage/AntennaModels/models.html">Models</a></li>
          <li class="navButton"><a href="../AntennaRangeWebpage/ExternalResources/ExternalResources.html">Resources</a></li>
          <li class="login" class="navButton "><a href="../AntennaRangeWebpage/login/login.html">Login</a></li>
      
      </ul>
        
    </head>
    <body>
        <main>
            <div class="title" style="color:#333;background-color:white;">
                <h3>Experiment Library</h3>
                <div class="underline" style="background-color:#CF4520;color:rgb(238, 238, 238);"><br></div>
                
                <ul id="myUL">
                <div class="row">
                  <div class="bigColumn"><input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search Experiments..."></div>

                  <div class="smallColumn">
                  <form action="../AntennaRangeWebpage/ExperimentLibrary/eLibrary.html">
                      <button type="submit" class="findButton"value="New Search" />New Search</button>
                  </form>
                  </div>
                  
                  <form action="./compareExperiments.cgi">
                  <div class="smallColumn">
                  <button id="viewButton" type="submit" class="findButton" value="View Experiments" />View Experiments</button>
                  </div>
                </div>
                

            """)
print_filters(filters)
print_experiments(experiments)
print("""
        </form>
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

                // This prevents more than 3 experiments from being selected for comparison CHANGE TO 5
                $('input[type=checkbox]').on('change', function (e) {
                if ($('input[type=checkbox]:checked').length > 3) {
                    $(this).prop('checked', false);
                    alert("You may select up to 3 experiments");
                }
                });

                $(document).ready(function () {
                  $('#viewButton').click(function() {
                    checked = $("input[type=checkbox]:checked").length;

                    if(!checked) {
                      alert("You must check at least one checkbox.");
                      return false;
                    }

                  });
              });

                </script>


        </main>

        <footer>
        </footer>
    </body>
</html>

""")
