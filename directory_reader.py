# Directory Size and file reader code. 
# Saves directory size and file names to results.txt within created results sub folder

import os
from os import path
from asyncore import write

def main():
    #Obtains the scripts directory path
    script_dir = os.path.dirname(__file__)

    #Checks if results folder already exists within current directory, if so skips creating it, if not then it creates it
    if os.path.isdir('results') == False:
        os.mkdir("results")

    #Adds results.txt file path to a results folder where the script is ran from
    rel_path = "results\\results.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    #Gets all files and folders in the current directory
    dir_list = os.listdir(script_dir)

    #Gets the size of the files in current directory in bytes (does not include sub directories)
    dir_size = sum(os.path.getsize(f) for f in dir_list if os.path.isfile(f))

    #Opens results file and creates it if it's not already present.
    
    with open(abs_file_path, 'w+') as myfile:
        #Writes the total size of the files in bytes at the start
        myfile.write("Directory Size is: " + str(dir_size) + "bytes\n")

        #Adds heading for file names
        myfile.write("Files List:\n")
        myfile.write("--------------\n")

        #Writes each file name into the results text file
        for f in dir_list:
            if os.path.isfile(f):
                myfile.write("%s\n" % f)

    #Closes the files
    myfile.close()
    

#Main function runs on start up if this script is main script i.e. not called by another script
if __name__ == "__main__":
    main()