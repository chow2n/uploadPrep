import os
import shutil
import csv
import pandas as pd

# Input where to create upload folders
z = print ('Upload Location:')
uploadPath = input()

# Input the name of the upload
x = print ('Name of upload:')
uploadName = input()

# Create the upload folders for BugBuster
try:
    os.chdir (uploadPath)

    os.mkdir (uploadName)

    os.chdir (uploadPath + "\\" + uploadName)
    os.mkdir ('expected')
    os.mkdir ('files')
    os.mkdir ('output')

    os.chdir (uploadPath + "\\" + uploadName + "\\" + 'expected')
    os.mkdir (uploadName)

    os.chdir (uploadPath + "\\" + uploadName + "\\" + 'files')
    os.mkdir (uploadName)

    print ('Upload folders created.')
except FileExistsError:
    print ('File already exists.')

# Input the path for the upload files
y = print ('Clustered Files to Upload Path:')
uploadFiles = input()

# Create CSV of FileNames of upload files
fileNames = []
requestIDs = []

for path in os.listdir(uploadFiles):
    if os.path.isfile(os.path.join(uploadFiles, path)):
        fileNames.append(path)
        requestIDs.append(None)

fileNamesDict = {'Test_Filename': fileNames, 'requestId':requestIDs}

df = pd.DataFrame(fileNamesDict)

csvPath = uploadPath + "\\" + uploadName + "\\" + 'expected' + "\\" + uploadName + "\\"
df.to_csv(csvPath + uploadName + '.csv', sep = ',' , index = False)

# Copy upload files to upload folder
os.chdir(uploadFiles)
files = os.listdir(uploadFiles)
for file in files:
    shutil.copy(file, uploadPath + "\\" + uploadName + "\\" + 'files' + "\\" + uploadName)