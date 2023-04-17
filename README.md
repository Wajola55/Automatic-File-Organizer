### Automatic File Organizer


This Python script organizes files in a specified source directory into different folders based on their file
types and then moves them to a specified destination directory.

First, the script imports the required libraries: os, shutil, and glob.
It then defines the source and destination directories, as well as a dictionary containing 
the file types and their associated file extensions.

The script iterates through the file types and extensions, and for each file type,
it creates a folder in the destination directory if it does not already exist. 
It then loops through the file extensions for that file type and searches for matching files in the source directory. 
If a matching file is found, the script prints a message indicating the file is being moved and then moves the file
from the source directory to the appropriate folder in the destination directory.
