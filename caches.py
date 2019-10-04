#
# https://www.geeksforgeeks.org/working-zip-files-python/
#
import os
import zipfile
from tkinter import filedialog
from tkinter import *

#GUI for directory selection
root = Tk()
root.filename =  filedialog.askdirectory(initialdir = "/",title = "Select Cache Directory")
path = (root.filename)

#zip the directory with the caches
def zipdir(path, ziphandle):
    
    for root, directories, files in os.walk(path):
        for file in files:
            ziphandle.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('caches.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(path, zipf)
    zipf.close()
