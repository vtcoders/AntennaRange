#!/usr/bin/env python3

import cgi, cgitb, sys

form = cgi.FieldStorage()

# username = form.getvalue('uname')
# password = form.getvalue('psw')
fileNames = form.getlist('box')

# TO-DO: Validation for characters entered and length, etc.

filepath = "../../.local/lib/python3.6/site-packages"
sys.path.append(filepath)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["experiments"]

def print_thing():
    fileName1 = '../Data/experiments/03-Oct-2020_01_01_01.x3d'
    print(""" """ + fileName1 + """ """)

def print_thing2():
    print("""<inline id="x3dModel1" nameSpaceName="x3dModel1" mapDEFtoID="true" render="true" url=../AntennaRangeWebpage/ExperimentCompare/models/sample2_aopt.x3d"><unit category='length' conversionFactor='1.0' name='METERS'/></inline>""")

def compose_models():
    string_to_return = ""
    for i in range(len(fileNames)):
        modelId = "x3dModel" + str(i + 1)
        if i in range(len(fileNames)):
            url = "../Data/experiments/" + fileNames[i]
            string_to_return = string_to_return + """<inline id=""" + modelId + """ nameSpaceName=""" + modelId + """ mapDEFtoID="true" render="true" url='""" + url + """'><unit category='length' conversionFactor='1.0' name='METERS'/></inline>"""
        
    return string_to_return
    
print("""Content-type: text/html\n""")
html_to_print = """<html>
    <head>
        <Title>Experiment Workspace</Title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
        <link rel="stylesheet" href="../AntennaRangeWebpage/ExperimentCompare/compare.css">
        <script type='text/javascript' src='https://www.x3dom.org/download/x3dom.js'></script>
        <link rel='stylesheet' type='text/css' href='https://www.x3dom.org/download/x3dom.css'></link>

        <ul id="navigationBar" class="navBar sticky">
          <li class="navButton header">Antenna Range Project</li>
          <li class="navButton header"></li>
          <li class="navButton"><a href="../AntennaRangeWebpage/index.html">Home</a></li>
          <li class="navButton"><a href="../AntennaRangeWebpage/AboutPage/aboutPage.html">About</a></li>
          <li class="navButton"><a href="../AntennaRangeWebpage/ExperimentLaunch/experimentLaunchPage.html">Launch</a></li>
          <li class="navButton"><a href=#>Library</a></li>
          <li class="navButton"><a href="../AntennaRangeWebpage/AntennaModels/models.html">Models</a></li>
          <li class="navButton"><a href="../AntennaRangeWebpage/ExternalResources/ExternalResources.html">Resources</a></li>
          <li class="login" class="navButton "><a href="../AntennaRangeWebpage/login/login.html">Login</a></li>
      
      </ul>
    </head>
    <body>
        <main>
            <div class="colorContainer title" style="color:#333;background-color:white;">
                <h3>View Experiments</h3>
                <div class="underline" style="background-color:#CF4520;color:rgb(238, 238, 238);"><br></div>
                <p> Select experiments to view. If you cannot see models, click on the model window and press the 'A' key. For more navigational information, press the info icon in the top right corner of the model window. To toggle graph visibility on and off for each experiment, click its visibility button.</p>
            </div>
            <div class="colorContainer" style="width: 100%; height: 100%;">
                <div class="row">
                    <div class="column sideBar" style="color:#333;background-color:wwhite;">
                        <ul id="myUL">
                        <li>
                            <div class="row">
                                <div class="column largeColumn"><a href="#" id="drag1" draggable="true" ondragstart="drag(event)">Experiment 1: Nov 4, 2020 Sample 1<br></a></div>
                                <div class="column tinyColumn">
                                    <input type="image" onclick='visibilityButtonClicked(this, "x3dModel1")' src='../AntennaRangeWebpage/ExperimentCompare/visible.png' class="visible"></input>
                                </div>
                            </div>
                            <div class="row">
                                <div class="column largeColumn"><p>Transparency:
                                    <input type="number" min="0" max="100" step="100" value="0" class="sliderValue" id="tnumber1" onchange="updateValue('tslider1', this.value); updateTransparency('x3dModel1', this.value);">
                                    <input type="range" min="0" max="100" step="1" value="0" class="slider" style="padding-top:5px;" id="tslider1" onchange="updateValue('tnumber1', this.value); updateTransparency('x3dModel1', this.value);"></p></div>
                                
                            </div>
                        </li>
                        <li>
                            <div class="row">
                                <div class="column largeColumn"><a href="#" id="drag2" draggable="true" ondragstart="drag(event)">Experiment 2: Nov 14, 2020 Sample 2 <br></a></div>
                                <div class="column tinyColumn">
                                    <input type="image" onclick='visibilityButtonClicked(this, "x3dModel2")' src='../AntennaRangeWebpage/ExperimentCompare/visible.png' class="visible"></input>
                                </div>
                            </div>
                            <div class="row">
                                <div class="column largeColumn"><p>Transparency:
                                    <input type="number" min="0" max="100" step="100" value="0" class="sliderValue" id="tnumber2" onchange="updateValue('tslider2', this.value); updateTransparency('x3dModel2', this.value);">
                                    <input type="range" min="0" max="100" step="1" value="0" class="slider" style="padding-top:5px;" id="tslider2" onchange="updateValue('tnumber2', this.value); updateTransparency('x3dModel2', this.value);"></p></div>
                                
                            </div>
                        </li>
                        <li>
                            <div class="row">
                                <div class="column largeColumn"><a href="#" id="drag3" draggable="true" ondragstart="drag(event)">Experiment 3: Sample 3 <br></a></div>
                                <div class="column tinyColumn">
                                    <input type="image" onclick='visibilityButtonClicked(this, "x3dModel3")' src='../AntennaRangeWebpage/ExperimentCompare/visible.png' class="visible"></input>
                                </div>
                            </div>
                            <div class="row">
                                <div class="column largeColumn"><p>Transparency:
                                    <input type="number" min="0" max="100" step="100" value="0" class="sliderValue" id="tnumber3" onchange="updateValue('tslider3', this.value); updateTransparency('x3dModel3', this.value);">
                                    <input type="range" min="0" max="100" step="1" value="0" class="slider" style="padding-top:5px;" id="tslider3" onchange="updateValue('tnumber3', this.value); updateTransparency('x3dModel3', this.value);"></p></div>
                                
                            </div>
                        </li>
                        <li>
                            <div class="row">
                                <div class="column largeColumn"><a href="#" id="drag4" draggable="true" ondragstart="drag(event)">Experiment 4: Sample - not present <br></a></div>
                                <div class="column tinyColumn">
                                    <input type="image" onclick='visibilityButtonClicked(this, "x3dModel4")' src='../AntennaRangeWebpage/ExperimentCompare/visible.png' class="visible"></input>
                                </div>
                            </div>
                            <div class="row">
                                <div class="column largeColumn"><p>Transparency:
                                    <input type="number" min="0" max="100" step="100" value="0" class="sliderValue" id="tnumber4" onchange="updateValue('tslider4', this.value); updateTransparency('x3dModel4', this.value);">
                                    <input type="range" min="0" max="100" step="1" value="0" class="slider" style="padding-top:5px;" id="tslider4" onchange="updateValue('tnumber4', this.value); updateTransparency('x3dModel4', this.value);"></p></div>
                                
                            </div>
                        </li>
                        <li>
                            <div class="row">
                                <div class="column largeColumn"><a href="#" id="drag5" draggable="true" ondragstart="drag(event)">Experiment 5: Sample - not present <br></a></div>
                                <div class="column tinyColumn">
                                    <input type="image" onclick='visibilityButtonClicked(this, "x3dModel5")' src='../AntennaRangeWebpage/ExperimentCompare/visible.png' class="visible"></input>
                                </div>
                            </div>
                            <div class="row">
                                <div class="column largeColumn"><p>Transparency:
                                    <input type="number" min="0" max="100" step="100" value="0" class="sliderValue" id="tnumber5" onchange="updateValue('tslider5', this.value); updateTransparency('x3dModel5', this.value);">
                                    <input type="range" min="0" max="100" step="1" value="0" class="slider" style="padding-top:5px;" id="tslider5" onchange="updateValue('tnumber5', this.value); updateTransparency('x3dModel5', this.value);"></p></div>
                                
                            </div>
                        </li>
                        </ul>
                    </div>
                    <div class="column right" style="position: relative;">
                        <div class="row" style="padding: 5px; border: 3px solid #CF4520;">
                            3d Models:
                            <div class="popup" style=" float: right;"onclick="displayInfoPopup()">
                                <img src="../AntennaRangeWebpage/ExperimentCompare/InfoIcon.png" alt="infoIcon" style="padding: .5px; height: 17px; width: auto;"></img>
                                    <span class="popuptext" id="myPopup">
                                        <b>How to Navigate:</b><br><br>
                                        Rotate:                 Left/Left + Shift<br>
                                        Pan:                    Mid/Left + Ctrl<br>
                                        Zoom:                   Right/Wheel/Left + Alt<br>
                                        Set Center of Rotation: Double-click Left<br><br>
                                        Reset View:             r<br>
                                        Show all:               a<br>
                                        Upright:                u
                                    </span>
                            </div> 
                        </div>
                        <div style="margin-top: 5px;" id="x3dModelWindow">
                            <!--Put x3d model right here-->
                            <x3d width='100%' height='100%'> 
                                <scene>
                                    <navigationInfo avatarSize="[ .05, .05, .05 ]" type="examine" headlight="true" speed="1.0" id="navType"></navigationInfo>
                                    <Transform scale="1, 1, 1">
                                    """
html_to_print = html_to_print + compose_models()
html_to_print = html_to_print + """
                                    </Transform>
                                </scene> 
                            </x3d>
                            <div onload="setSortType();"></div>
                        </div>
                        <br><br>
                    </div>
                </div>
                <div style="display:none;">
                THE BELOW FEATURE HASN'T BEEN FINISHED YET :)
                <div class="row">
                    <br><br>
                    <div id="drop3" ondrop="drop(event);" ondragover="allowDrop(event);" class="column sixSplitFirst">Categories<br>Experiment Name: <br>Date: <br> Mast Angle: <br>Arm Angle: <br>Transmission RSSI: <br>Background RSSI: </div>
                    <div id="drop4" ondrop="drop(event);" ondragover="allowDrop(event);" class="column sixSplit">
                        Drop Here
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                    <div id="drop5" ondrop="drop(event);" ondragover="allowDrop(event);" class="column sixSplit">
                        Drop Here
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                    <div id="drop6" ondrop="drop(event);" ondragover="allowDrop(event);" class="column sixSplit">
                        Drop Here
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                    <div id="drop7" ondrop="drop(event);" ondragover="allowDrop(event);" class="column sixSplit">
                        Drop Here
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                    <div id="drop8" ondrop="drop(event);" ondragover="allowDrop(event);" class="column sixSplit">
                        Drop Here
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                </div>
                
                <div id="sliders" class="column sliders">[insert sliders here]</div>
                </div>
            </div>

            <script>

                function displayInfoPopup() {
                    var popup = document.getElementById("myPopup");
                    popup.classList.toggle("show");
                }

                function updatePopup(id)
                {
                    var popup = document.getElementById(id);
                       if(popup.style.display == 'block')
                          popup.style.display = 'none';
                       else
                          popup.style.display = 'block';
                }

                // used to change the value displayed in text box next to slider
                function updateValue(id, val)
                {
                    document.getElementById(id).value=val; 
                }

                // used to change the transparency of x3d model
                function updateTransparency(x3dmodelid, val)
                {
                    // setSortType(); // set sortKey attribute of Appearance so models load in descending order
                    var name = document.getElementById(x3dmodelid).getAttribute('nameSpaceName');
                    var id = name.concat('__AntennaRange_MA_Pelt');
                    var transparency = val / 100;
                    var transparencyString = transparency.toString();
                    if (document.getElementById(id))
                        document.getElementById(id).setAttribute('transparency', transparencyString);
                    x3dom.reload();
                }

                // used to change rendering order of models to fix transparency issues
                function setSortType()
                {
                    helperSetSortType('x3dModel1');
                    helperSetSortType('x3dModel2');
                    helperSetSortType('x3dModel3');
                    helperSetSortType('x3dModel4');
                    helperSetSortType('x3dModel5');
                }

                // helper method for setSortKeys()
                function helperSetSortType(x3dModelID)
                {
                    var name = document.getElementById(x3dModelID).getAttribute('nameSpaceName');
                    var id = name.concat('__AntennaRange_Appearance');
                    if (document.getElementById(id))
                    {
                        document.getElementById(id).setAttribute('sortType', 'transparent');
                        console.log(document.getElementById(id).getAttribute('sortType'));
                    }
                    else
                    {
                        console.log("Meh, nothing was found :(");
                    }
                    x3dom.reload();
                }

                function visibilityButtonClicked(button, modelID)
                {
                    // Change class of visibility button for looks and filtering
                    if (button.className === "visible")
                    {
                        button.className = "invisible";
                        button.src = "../AntennaRangeWebpage/ExperimentCompare/invisible.png";
                        document.getElementById(modelID).setAttribute("render", "false");
                    } // if
                    else // button.className === "invisible"
                    {
                        button.className = "visible";
                        button.src = "../AntennaRangeWebpage/ExperimentCompare/visible.png";
                        document.getElementById(modelID).setAttribute("render", "true");
                    } // else
                }

                function graphsRefresh()
                {
                    // for // look at eLibrary
                };

                function checkButtonClicked(button)
                {
                    if (button.className === "visible")
                    {
                        button.className = "invisible";
                        button.src = "../AntennaRangeWebpage/ExperimentCompare/invisible.png";
                    } // if
                    else // button.className === "invisible"
                    {
                        button.className = "visible";
                        button.src = "../AntennaRangeWebpage/ExperimentCompare/visible.png";
                    } // else
                    graphsRefresh();
                }

                function dataRefresh()
                {
                    
                };

                function allowDrop(ev) {
                     ev.preventDefault();
                };

                function drag(ev) {
                ev.dataTransfer.setData("text/plain", ev.target.id);
                };

                function drop(ev)
                {
                    justForExample = ["Experiment 1", "Feb 3, 2020", "35", "120.2", "132.23", "1.23"]
                    divs = ev.target.getElementsByTagName('div');
                    for (var i = 0; i < divs.length; i++)
                    {
                        divs[i].textContent = justForExample[i];
                    }
                    updateSliders(exp);
                }

                function updateSliders(experiment, mastAngle, armAngle, tRSSI, bRSSI)
                {

                }

                /**
                function drop(ev) {
                ev.preventDefault();
                var data = ev.dataTransfer.getData("text");
                ev.target.appendChild(document.getElementById(data));
                ev.target.className = "column evenLeft blue";
                };
                **/
            </script>

        </main>

        <footer>
        </footer>
    </body>
</html>"""

print(html_to_print)