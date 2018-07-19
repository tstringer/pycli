## NOTE:
Before proceeding to what this file contains, it must be noted that this file is optional and is not compulsory for the functioning of the app being developed here. This file simply expected to contain notes and guidelines related to the app's development, launch etc. It is purely on the developer/team/commuinity what they collectively feel is suitable to be written into this file.

# Python CLI  structure
## Why?
This repo serves as a good reference point for a simple and basic CLI
structure. This can either be consumed visually or cloned in which case you
should change `pycli` to whatever your CLI name will be.

## What this repository/folder represents?
**Source:** [ https://medium.com/@trstringer/the-easy-and-nice-way-to-do-cli-apps-in-python-5d9964dc950d ]

Everything contained in this folder (except for this 'ReadMe' file and any other such file contained in any of the subfolders) is a compulsory component for correct functioning of the app that is being represented by this folder. We can think of this being the view of the app from a developer's perspective. i.e. This is all what a developer will ever care about regarding this app - just like what a user normally cares about is the look-and-feel/output/(whether a desktop icon is provided or not) etc.

### Directory hierarchy:

     (root/parent-folder)
     
     |-----ReadMe.md (optional as aforementioned)

     |-----install.sh
     
     |-----setup.py

     |-----component_1

     |-----component_2

     |-----component_3
     
     |-----Other Files if required as per the design/architecture of the cli app.

The above hierarchy  presents a pretty generalized model of structring your app's developement. It assumes for
simplicity that your software is structured the same way it was architected/designed. For instance, if your
software has been designed to be comprised of 5 major components (each having their internal modular structure)
that interact with each-other in a pre-designed/desired manner, sprouting the functionality of your app, your
developement structuring is expected to have 5 folders - each corresponding to one major component.

In our example (kind of a hello-world app), we have the following structure:
      
      pycli-(root-folder)
      
      |----- ReadMe.txt
      
      |----- install.sh
      
      |----- setup.py
      
      |----- pycli
      
            |----- __init__.py
            
            |----- __main__.py
            
            |----- classmodule.py
            
            |----- functionmodule.py
