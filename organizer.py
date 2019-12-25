import os
from shutil import move

#PATHS
dir = os.getcwd()
folder = dir+'/organized'

#CHECKS IF FOLDER EXISTS AND CREATES IT IF DON'T
try:
    os.chdir(folder)
    os.chdir(dir)
except:
    os.mkdir(folder)

#ASSIGN ARRAY OF FILES IN THE CURRENT DIRECTORY
files = os.listdir()

#WHAT REMAINS AFTER PROCESSING
files.remove('organized')
files.remove('organizer.py')

#MOVES FILES TO ORGANIZED FOLDER
for f in files:
    file = dir+'/'+f
    destination = folder+'/'+f
    try:
        os.replace(file, destination)
    except PermissionError:
        print('Failed to move file "%s": being used by another process.' % f)

os.chdir(folder)

organized = os.listdir()

for f in organized:
    file = folder+'/'+f
    file, file_extension = os.path.splitext(folder+'/'+f)
    try:
        os.chdir(file_extension)
        os.chdir(folder)
    except:
        os.mkdir(file_extension)
    destination = folder+'/'+file_extension+'/'
    try:
        move(folder+'/'+f, destination)
        #os.replace(folder+'/'+f, destination)
    except PermissionError:
        print('Failed to move file "%s": being used by another process.' % f)
    print(file_extension)
