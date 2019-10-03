#
# https://www.geeksforgeeks.org/working-zip-files-python/
#

import os
import zipfile

#Get project ID
## id = input ("Enter project ID value: ")

#Get Cache directory
## path = input ("Enter path to cache directory: ")
path = "C:\\Users\\dburns\\Desktop\\Desktop_04_2019\\Python\\testfodler"

#zip the directory with the caches
def zipdir(path, ziphandle):
    
    for root, directories, files in os.walk(path):
        for file in files:
            ziphandle.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('caches.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(path, zipf)
    zipf.close()
