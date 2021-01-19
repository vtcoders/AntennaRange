# Antenna Range - Refactor `main.py`

**Contents**<br>
[About](#about)<br>
[Maintainers](#maintainers)<br>
[Dependencies](#dependencies)<br>
[Usage](#usage)

## About
`main.py` controls the antenna. The file is stored on Tricorder and is written in python. <br>
The refactor involves making the script run autonomously as it needs to do the following
<ul>
  <li>Receive a configuration file from Rock to Tricorder</li>
  <li>Send the plots and results from Tricorder to Rock</li>
</ul>
Currently the script is able to take in a configuration file, perform error checking on the parameters, and sends those files to its dependencies. <br>
Further testing will involve testing this live on Tricorder and making sure it can communicate with Rock

## Maintainers
Backend Team includes:
<ul>
    <li>Neel Patel</li>
    <li>[Nathaniel Salazar](https://github.com/Nintendroid1)</li>
    <li>Amelia Whitehead</li>
    <li>Mannie</li>
</ul>

## Dependencies
Certain imports are necessary to test this script, specifically 
<ul>
  <li>MotorController</li>
  <li>NetworkListener</li>
  <li>PlotGraph</li>
  <li>RadioFlowGraph</li>
  <li>RadioListener</li>
</ul>
These files can be found on the canvas site under Files -> BuildOne -> server_7_20_2020 <br>
Test File is stored in `input.csv` and is based on the original, hard-coded values in the previous `main.py`

## Usage
To run `main.py` with the configuration file:<br>
```
python3 main.py input.csv
```
