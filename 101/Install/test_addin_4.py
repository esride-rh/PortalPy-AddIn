import arcpy
import pythonaddins
import sys
sys.path.append(r"C:\Python27\Lib\site-packages")
from portalpy import *

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
