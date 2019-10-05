#
# https://www.geeksforgeeks.org/working-zip-files-python/
# https://pythonspot.com/tk-file-dialogs/
# https://pypi.org/project/py2exe/
# https://stackoverflow.com/questions/41578808/python-indexerror-tuple-index-out-of-range-when-using-py2exe
# https://stackoverflow.com/questions/1406145/how-do-i-get-rid-of-python-tkinter-root-window
# https://thispointer.com/python-how-to-move-files-and-directories/
# https://stackoverflow.com/questions/1406145/how-do-i-get-rid-of-python-tkinter-root-window
# 

import os
import zipfile
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import shutil
import subprocess
import platform
from tkinter import messagebox
from pymsgbox import *

#GUI for directory selection
root = Tk()
root.withdraw() #hide the root window

#Processing GUI
msg = tk.Tk()
msg.title("Compressing Files. Please Wait...")
canvas= Canvas(msg, width=350, height=50)
canvas.pack()
msg.withdraw()

if __name__ == '__main__':

    root.filename =  filedialog.askdirectory(initialdir = "/",title = "Please Select Cache Directory")
    path = (root.filename)

    #show message box
    msg.deiconify()

    #zip the directory with the caches
    def zipdir(path, ziphandle):
    
        for root, directories, files in os.walk(path):
            for file in files:
                ziphandle.write(os.path.join(root, file))

#zip process
zipf = zipfile.ZipFile('caches.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir(path, zipf)
zipf.close()

#kill message box
msg.withdraw()

#GUI to get output directory of zipfile
root.filename =  filedialog.askdirectory(initialdir = "/",title = "Please Select Target location to Extract to")
tpath = (root.filename)

#move zip file to target location
shutil.move("caches.zip", tpath)

#openFilelocation of zipped files
os.startfile(tpath)