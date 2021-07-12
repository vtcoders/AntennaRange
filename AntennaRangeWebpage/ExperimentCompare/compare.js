
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
                        button.src = "./invisible.png";
                        document.getElementById(modelID).setAttribute("render", "false");
                    } // if
                    else // button.className === "invisible"
                    {
                        button.className = "visible";
                        button.src = "./visible.png";
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
                        button.src = "./invisible.png";
                    } // if
                    else // button.className === "invisible"
                    {
                        button.className = "visible";
                        button.src = "./visible.png";
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
