import arcpy
import pythonaddins
import sys
sys.path.append(r"C:\Python27\Lib\site-packages")
from portalpy import *

#Ash 2/17: Import modules to read a webpage
import shutil, os, time, datetime, math, urllib
from array import array

#Ash 2/17: Rest endpoint url (for any organization)
list_services_path1 = r"http://services.arcgis.com"
list_services_path2 = r"ArcGIS/rest/services?f=pjson"  #Converted to JSON format

#Ash 2/17: ESS specific org ID. How do we find out this info for all orgs?
ESS_org_ID = "//Wl7Y1m92PbjtJs5n//"

#Ash 2/17: Output location for Nohe
output = r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Output\output.txt"


global portalLogin
global portalID
#Get bad syntac error when declaring global portalLogin = () or portalLogin = portalpy.Portal()

class SignOn(object):
    """Implementation for test_addin.signonbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        global portalLogin
        """  While the GPToolDialog runs asynchronously from the tool, it does have the option
            to import the global variable and then  reassign the variable to the
            portal object.  This allows our users to access the portal object in
            other classes that we create from this.
        """
        pythonaddins.GPToolDialog(r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Tools\Toolbox.tbx", "SignOn")

        #Ash 2/17: Creates an output.txt file that contains the names of all services in the organization.

        FILE = open(output, "w")

        filehandle = urllib.urlopen(list_services_path1 + ESS_org_ID + list_services_path2)
        for lines in filehandle.readlines():
            #[16:-5]      "name" : "      
            if '"name"' in lines:
                FILE.write(lines[16:-5])
                FILE.write('\n')

        FILE.close()
        
        print "Check your output folder for a list of services in your organization."

class folderList(object):
    """Implementation for test_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        global portalLogin
        print "These are the folders you have currently on this Portal username:"
        for i in portalLogin.folders(portalID):
            print i['title']

class newFolder(object):
    """Implementation for test_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Tools\Toolbox.tbx", "createFolderCU")


class portalpyUsers(object):
    """Implementation for test_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        for i in portalLogin.users(['username', 'fullName']):
            print i

class deleteUser(object):
    """Implementation for test_addin.button_3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Tools\Toolbox.tbx", "deleteUser")
