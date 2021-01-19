import argparse
from mutagen.mp4 import MP4
import glob
import os

# Aendert den Titel einer MP4-Datei
def changeTitle(filename, newTitle):
    video = MP4(filename)
    video.tags["\xa9nam"] = [newTitle]
    video.save()

# Gibt den Titel einer MP4-Datei zurueck; wird nicht gebraucht
def getTitle(filename):
    video = MP4(filename)
    return video.tags["\xa9nam"][0]

# Es wird eine Liste mit allen Pfaden zu MP4-Dateien zurückgegeben
def getFiles(path, recursive=False):
    if recursive:
        return glob.glob(f"{path}/**/*.mp4", recursive=True)
    else:
        return glob.glob(f"{path}/*.mp4")
    

# Parser
parser = argparse.ArgumentParser(prog='mp4-title-changer.py',
                                description='cli to change all titles of the mp4-files to the name of the file')

parser.add_argument('-p',
                    '--path',
                    metavar='path',
                    type=str,
                    help='path of the directory of the mp4-files')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-c',
                    '--change',
                    action='store_true',
                    help='sets mode to change the titles of all mp4-files')

group.add_argument('-g',
                    '--get',
                    action='store_true',
                    help='sets mode to get all mp4-files')
                    
parser.add_argument('-r',
                    '--recursive',
                    action='store_true',
                    help='includes all subdirectories')

parser.add_argument('-v',
                    '--verbose',
                    action='store_true',
                    help='produces verbose output')

parser.add_argument('-d',
                    '--debug',
                    action='store_true',
                    help='shows debug messages')


args = parser.parse_args()

# Start program
if __name__ == "__main__":
    # Get all parsed variables
    path = args.path
    change = args.change
    get = args.get
    recursive = args.recursive
    verbose = args.verbose
    debug = args.debug

    if path == None:
        path = os.getcwd() + ""

    files = getFiles(path=path, recursive=recursive)

    if get:
        for file in files:
            try:
                title = getTitle(file)
                print(f"File: {file} Title: {title}")
            except:
                print(f"ERROR: {file}")
            
        if debug:
            print("")
            print("### Debug ###")
            print(f"Pfad: {path}; Change: {change}; Get: {get}; Recursive: {recursive}; Verbose: {verbose}; Debug: {debug}")

    elif change:
        for i in range(len(files)):
            file = files[i]
            filename = file.rsplit('/', 1)[1]
            title = filename.rsplit('.', 1)[0].title()
            try:
                changeTitle(file, title)
                print(f"File: {file}")
                print(f"Title: {title}")
                if i != len(files)-1:
                    print("")
            except:
                print(f"ERROR: {file}")
        if debug:
            print("")
            print("### Debug ###")
            print(f"Pfad: {path}; Change: {change}; Get: {get}; Recursive: {recursive}; Verbose: {verbose}; Debug: {debug}")